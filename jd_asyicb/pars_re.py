import re
from parse_engine.parse import ParseData


def parse(msg):
    parse_data = ParseData(
        msg['platform'],
        msg['parse_rule'],
        msg['params'])
    return parse_data.main(msg['data'])

def parse2result(msg):
    result = {
       'platform': msg['platform'],
       'data': parse(msg),
    }
    # domain = re.search('://(\S+?)/', msg['url']).group(1)
    # if domain in ['item.jd.com', 'wq.jd.com', 'c0.3.cn','pm.3.cn']:
    #     result['url'] = msg['url']
    return result