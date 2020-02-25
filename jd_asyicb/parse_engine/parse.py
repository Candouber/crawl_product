import re
import json
import traceback
import html.parser
from urllib.parse import unquote
from lxml import etree


def parse_result(data):
    if isinstance(data, list):
        if not data:
            data = None
        elif len(data) == 1:
            if isinstance(data[0], dict):
                pass
            else:
                data = str(data[0]).strip()
    return data


def encode(data, rule):
    encoding, decoding = rule.split(',')
    return data.encode(encoding).decode(decoding)


def parse_unquote(data):
    return unquote(data)


def parse_unescape(data):
    if not data:
        return data
    return html.parser.HTMLParser().unescape(data)


def read_rules(filename):
    with open('rules/' + filename, 'r', encoding='utf8') as f:
        return f.readlines()


def parse_rules(lines):
    keywords = {}
    for line in lines:
        if '===' in line:
            break
        line = line.strip()
        if not line:
            continue
        if line.startswith('[') and line.endswith(']'):
            keyword = line[1:-1]
            keywords[keyword] = []
            continue
        _, engine, rule = line.split('#', 2)
        keywords[keyword].append(((engine, rule)))
    return keywords


def parse_any(data, rules):
    results = []
    if isinstance(data, dict):
        data = data.values()
    for item in data:
        found = True
        for i, rule in enumerate(rules):
            if rule == '*':
                item = parse_any(item, rules[i + 1:])
                break
            elif rule.startswith('?'):
                if rule[1:] in item:
                    item = item[rule[1:]]
                else:
                    found = False
                    break
            else:
                item = item[rule]
        if found:
            results.append(parse_result(item))
    return results


class ParseError(Exception):

    def __init__(self, data, keyword, engine, rule, tb):
        super().__init__()
        self.message = {
            'data': data,
            'keyword': keyword,
            'engine': engine,
            'rule': rule,
            'tb': tb
        }


class ParseData(object):

    def __init__(self, platform, parse_rule, params):
        content = read_rules(r'{}/{}.rules'.format(platform, parse_rule))
        self.keywords = parse_rules(content)
        self.params = params

    def _repl(self, matchobj):
        for param in matchobj.groups():
            if not isinstance(self.params[param], str):
                self.params[param] = str(self.params[param])
            return self.params[param]

    def _parse_json(self, row, rules):
        if isinstance(row, str):
            data = row[row.find('{'):row.rfind('}') + 1]
            data = json.loads(data)
        elif isinstance(row, dict):
            data = row
        else:
            print('不支持的JSON数据类型')
            return None
        rules = re.sub(r'!([\w\d_]+)', self._repl, rules)
        for i, rule in enumerate(rules.split('/')):
            if rule == '*':
                return parse_any(data, rules.split('/')[i + 1:])
            elif rule.startswith('?'):
                if rule[1:] in data:
                    data = data[rule[1:]]
                else:
                    return None
            else:
                data = data[rule]
        return data

    def _parse_html(self, data, rule):
        if '!' in rule:
            rule = re.sub(r'!([\w\d_]+)', self._repl, rule)
        result = []
        # print(data)
        for item in etree.HTML(str(data)).xpath(rule):
            if isinstance(item, etree._Element):
                temp = etree.tostring(item, encoding='unicode')
                result.append(temp.strip())
            elif isinstance(item, str):
                result.append(item.strip())
            else:
                print('xpath解析后的结果为未知类型')
        return result

    def _parse_re(self, data, line):
        yes, symbol, row_flags, rule = line.split('#', 3)
        if yes == 'Y':
            rule = re.sub(symbol + r'([\w\d_]+)', self._repl, rule)
        flags = 0
        for i in row_flags:
            if i == 'I':
                flags = flags | re.I if flags else re.I
            elif i == 'S':
                flags = flags | re.S if flags else re.S
            elif i == 'M':
                flags = flags | re.M if flags else re.M
        return re.findall(rule, data, flags=flags)

    def _parse2(self, data, engine, rule, keyword):
        try:
            if engine == 'JSON':
                result = self._parse_json(data, rule)
            elif engine == 'HTML':
                result = self._parse_html(data, rule)
            elif engine == 'RE':
                result = self._parse_re(data, rule)
            elif engine == 'ENCODE':
                result = encode(data, rule)
            elif engine == 'UNQUOTE':
                result = parse_unquote(data)
            elif engine == 'UNESCAPE':
                result = parse_unescape(data)
            else:
                result = None
                print('解析规则写错了：', engine)
            return parse_result(result)
        except:
            print(traceback.format_exc())
            raise ParseError(data,
                             keyword,
                             engine,
                             rule,
                             traceback.format_exc())

    def _parse1(self, data, engine, rule, keyword):
        if data is None:
            result = None
        elif isinstance(data, list):
            row = data
            result = []
            for item in row:
                temp = self._parse2(item, engine, rule, keyword)
                if temp:
                    result.append(temp)
            result = parse_result(result)
        else:
            result = self._parse2(data, engine, rule, keyword)
        return result

    def main(self, data):
        results = {}
        for keyword, rules in self.keywords.items():
            results[keyword] = data
            for line in rules:
                engine, rule = line
                results[keyword] = self._parse1(
                    results[keyword],
                    engine,
                    rule,
                    keyword)
        return results
