# coding:utf-8
import json
import re
import time
from itertools import cycle
from flask import Flask, jsonify, request
import aiohttp
import requests
import asyncio
from urllib.parse import quote
from pars_re import parse2result
from jingdong_2 import compute
from requests.packages import urllib3; urllib3.disable_warnings()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


task = {
        'platform': 'jingdong_2',
        'parse_rule': None,
        'params': {},
        'data': None,
        'url':None
        }

proxys = cycle([
    'http://zdm:zdm123@114.67.89.210:20000',
    'http://zdm:zdm123@114.67.89.210:20001',
    'http://zdm:zdm123@114.67.89.210:20002',
    'http://zdm:zdm123@114.67.89.210:20003',
    'http://zdm:zdm123@114.67.89.210:20004',
    'http://zdm:zdm123@114.67.89.210:20005',
    'http://zdm:zdm123@114.67.89.210:20006',
    'http://zdm:zdm123@114.67.89.210:20007',
    'http://zdm:zdm123@114.67.89.210:20008',
    'http://zdm:zdm123@114.67.89.210:20009',
])



async def crawler(url, referer=None):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    if referer:
        headers['referer'] = referer
    if 'wq.jd.com/item/view' in url:
        headers['user-agent'] = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
    if 'login' in url:pass
        # headers['Cookie'] = 'shshshfpa=5955ca00-b23e-d936-e76c-88fe9f121b1b-1534729078; shshshfpb=03e138f54ae61d81709c27b7224d541168cd36cff9a0b291a5b7a1b762; __jdc=122270672; __jdv=122270672|direct|-|none|-|1534729078736; __jdu=153472907873578071159; wlfstk_smdl=lj6qvx5u50s9otmmd9ceim5m495z8q6u; _pst=jd_7513385b8b2b6; logintype=wx; unick=%E5%A4%9A%E5%A4%9A%E9%94%85; pin=jd_7513385b8b2b6; npin=jd_7513385b8b2b6; _tp=tTcdAc30N1tApI%2BUQ3EsWlZrH6TccBAynKJkpbOSPs4%3D; pinId=72sCuqRjh2oZ7_CgAWFiabV9-x-f3wj7; 3AB9D23F7A4B3C9B=7W2LWUT6OCAHL6ZJE5O6657E2WUIYI6XXDIVBB3G4ORHZB2SI6BLGEQ4WWWPM7CTBPXDJDW6T32NPQGVK6GHBZO5JE; __jda=122270672.153472907873578071159.1534729079.1534731437.1534740844.3; user-key=2df14580-7458-4bae-9cd7-c95e46d47f94; ipLoc-djd=1-2810-6501-0.138516622; ipLocation=%u5317%u4eac; __tak=fe140e8a4cfe1df9c677e2bd814dc2ea62e20e0ce54310966957289481d7328bc71244543e2947b4eb864627a82735611ac3d2f3e3a86a9fe95e53cf8317d9680e82cbf25c5429d38acacb73e8ea09b6; cn=4; mba_muid=153472907873578071159; mobilev=html5; sid=39abe90a0b315a6f2bfe409c88da066e; shshshfp=805a9f88db05a00ea48d3c3b54f7c7e2; shshshsID=0d69209d0a8ff6cb0ea7d8484e38fab6_32_1534748140350; __jdb=122270672.41.153472907873578071159|3.1534740844; thor=B04E0C9789016B80176055BD7DA71D101C8099AEB76B9D52B1F2A99631A992D81DC1DD380BC203B93803EE240FACD3B5B8217336D3F0B1052ABC5F3F0A8A1C87D3C73CFB7CDDB35B618D5A548ED324BDC43EDB8BE9FAA1BF9F04BF59F9B77A3681AEDF7CCA23264D3BF73EE26B64A4256566361EC5F8895BBA4A299F8F21E3DDAA70CD17BCB38E10B80AA38A58C591D64E40C1073A165BFEE2DA218B70C41180'
    async with aiohttp.ClientSession() as session:  # read_timeout=1
        async with session.get(url, headers=headers, verify_ssl=False, proxy= next(proxys)) as response:  # timeout=1
        # async with session.get(url, headers=headers) as response:
            tet = await response.read()
    try:
        text = tet.decode('utf-8')
    except:
        text = tet.decode('gb18030', errors='ignore')
    return text


def html_parse(id):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'cookie': "__jda=122270672.1576649310771988572971.1576649311.1576649311.1576649311.1; __jdv=122270672|direct|-|none|-|1576649310774; __jdc=122270672; __jdu=1576649310771988572971;"
    }

    page_url = 'https://item.jd.com/{}.html'.format(id)
    res_page = requests.get(page_url, headers=headers
                            , proxies={"all":next(proxys)}
                            , verify=False).content
    try:
        res_page = res_page.decode('utf-8')
    except:
        res_page = res_page.decode('gb18030', errors='ignore')
    result = {'platform': 'jingdong_2', 'parse_rule': 'jd_x_html', 'params': {}, 'data': res_page, 'url': page_url}
    page_parse = parse2result(result)
    try:
        msg = page_parse['data']
    except:
        return None
    try:
        msg['property_map'] = list(map(lambda x: json.loads(x), msg['property_map']))
    except:
        pass
    if msg['img_urls']:
        msg['img_urls'] = list(map(lambda x: 'https:%s' % x, msg['img_urls']))
    msg['shop_url'] = 'https:' + msg['shop_url'] if msg['shop_url'] and not msg['shop_url'].startswith('https') else \
        msg['shop_url']
    f = None
    a = len(msg['spec_param']) if msg['spec_param'] else 0
    for i in range(a):
        if msg['spec_param'][i].endswith('：'):
            msg['spec_param'][i] += msg['spec_param'][i + 1]
            f = i + 1
    msg['spec_param'].remove(msg['spec_param'][f]) if f else f
    try:
        spec_param_extra = list(map(lambda x: x.replace('\xa0', ''), msg.get('spec_param_extra'))) if msg.get(
            'spec_param_extra', None) else []
    except:
        pass
    try:
        msg['spec_param'] += spec_param_extra if spec_param_extra else []
    except:
        pass
    msg.pop('spec_param_extra')
    vender_id = msg.pop('vender_id')
    main_skuid = msg.pop('main_skuid')
    main_skuid = main_skuid[0] if isinstance(main_skuid, list) else main_skuid
    vid = msg.pop('vid')
    cat = msg.pop('cat')
    if cat:
        msg['cat_id'] = cat.split(',')[0]
        msg['root_cat_Id'] = cat.split(',')[1]

    for score_name in ['shop_desc_score', 'shop_service_score',
                       'shop_logistics_score', 'item_description_score']:
        score = msg.pop('%s2' % score_name)
        if not msg[score_name]:
            msg[score_name] = score
    page_parse['data'] = msg
    return msg, {"skuid": id, "vender_id": vender_id, "cat": cat, "main_skuid": main_skuid, "vid": vid, "shop_id": msg['shop_id']}


async def detail_parse(sku_ids):
    global task
    task_detail = task.copy()
    skuid = sku_ids['skuid']
    main_skuid = sku_ids['main_skuid']
    detail_img_url = 'https://dx.3.cn/desc/{}?cdn=2&callback=showdesc'.format(main_skuid if main_skuid is not None else skuid)
    task_detail['parse_rule'] = 'jd_x_detail'
    task_detail['url'] = detail_img_url
    task_detail['data'] = await crawler(detail_img_url, 'https://item.jd.com/{}.html'.format(skuid))
    detail_result = parse2result(task_detail)
    return detail_result


async def price_parse(sku_ids):
    global task
    task_price = task.copy()
    skuid = sku_ids['skuid']
    vender_id = sku_ids['vender_id']
    cat = sku_ids['cat']

    price_url = 'https://c0.3.cn/stock?skuId=%s&area=1_72_2799_0&venderId=%s&cat=%s&buyNum=1' % (skuid, vender_id, cat) + '&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=1'
    task_price['parse_rule'] = 'jd_x_price'
    task_price['url'] = price_url
    task_price['data'] = await crawler(price_url, 'https://item.jd.com/{}.html'.format(skuid))
    price_url_crawler = parse2result(task_price)

    data = price_url_crawler['data'].copy()
    quantity_has = data.pop('quantity_has') if data.get('quantity_has', None) else None
    price_result = {}
    price_result['data'] = {'info': {},}
    price_result['data']['info']['def'] = data
    if quantity_has:
        price_result['data']['quantity_has'] = False if quantity_has in ['无货', '采购中'] else True
    return price_result


async def pin_parse(sku_ids):
    global task
    task_pin = task.copy()
    skuid = sku_ids['skuid']
    pin_url = 'https://wq.jd.com/pingou_api/BatGetPingouInfo?skuids={}&source=pc&platform=6&origin=1'.format(skuid)
    task_pin['parse_rule'] = 'jd_x_pin'
    task_pin['url'] = pin_url
    task_pin['data'] = await crawler(pin_url, 'https://item.jd.com/{}.html'.format(skuid))

    pin_url_crawler = parse2result(task_pin)

    if not pin_url_crawler['data']['pingou_price']:
        pin_url_crawler['data'] = {'info': {'def': {'pingou_price': {}}}}
    else:
        info = {'info': {'def': {'pingou_price': {'pin_price': pin_url_crawler['data']['pingou_price'], 'lefttime': pin_url_crawler['data'].get('lefttime')}}}}
        pin_url_crawler['data'] = info
    return pin_url_crawler


def order_price(msg):
    pick_one = msg['data']['pick_one'].copy() if msg['data']['pick_one'] else []
    tags = msg['data']['tags'].copy() if msg['data']['tags'] else []
    sku_coupon = msg['data']['sku_coupon'].copy() if msg['data']['sku_coupon'] else []
    description = msg['data']['description'] if msg['data']['description'] else None
    msg['data'] = {'description': description, 'prom_info': [], 'coupon': []}

    for pick in pick_one:
        if '，' in pick['content'] and pick['name'] in ['满减', '跨店铺满减进行中', '跨自营/店铺满减']:
            content = pick['content'].split('，') if '每满' not in pick['content'] else pick['content'].split('；')
            for i in content:
                try:
                    msg['data']['prom_info'].append(
                        {'prom_name': pick['name'], 'start_time': int(float(pick['st']) * 1000),
                         'end_time': int(float(pick['d']) * 1000), 'prom_id': pick['pid'], 'prom_msg': i})
                except:
                    continue

        elif '；' in pick['content'] and pick['name'] in ['活动预告', '多买优惠', '跨店铺满折进行中', '跨自营/店铺满折']:
            content = pick['content'].split('；')
            for i in content:
                try:
                    msg['data']['prom_info'].append(
                        {'prom_name': pick['name'], 'start_time': int(float(pick['st']) * 1000),
                         'end_time': int(float(pick['d']) * 1000), 'prom_id': pick['pid'], 'prom_msg': i})
                except:
                    continue
        elif '，' in pick['content'] and pick['name'] in ["加价购", ]:
            content = pick['content'].split('，')
            for i in content[:-1]:
                try:
                    msg['data']['prom_info'].append(
                        {'prom_name': pick['name'], 'start_time': int(float(pick['st']) * 1000),
                         'end_time': int(float(pick['d']) * 1000), 'prom_id': pick['pid'],
                         'prom_msg': '%s，%s' % (i, content[-1])})
                except:
                    continue
        else:
            try:
                msg['data']['prom_info'].append({'prom_name': pick['name'], 'start_time': int(float(pick['st']) * 1000),
                                                 'end_time': int(float(pick['d']) * 1000),
                                                 'prom_id': pick['pid'], 'prom_msg': pick['content']})
            except:
                continue

    for tag in tags:
        try:
            msg['data']['prom_info'].append({'prom_name': tag['name'], 'start_time': int(float(tag['st']) * 1000),
                                             'end_time': int(float(tag['d']) * 1000),
                                             'prom_id': tag['pid'], 'prom_msg': tag['content']})
        except:
            continue

    for coupon in sku_coupon:
        try:
            discount_json = coupon.get('discountJson', None)
            if discount_json:
                high = int(discount_json['high'])
                for dis in discount_json['info']:
                    try:
                        qua = int(dis['quota'])
                        minu = float(dis['discount'])
                        start_time = int(time.mktime(time.strptime(coupon['beginTime'] + ' 00:00:00',
                                                                   '%Y-%m-%d %H:%M:%S'))) * 1000 if isinstance(
                            coupon['beginTime'], str) else coupon['beginTime']
                        end_time = int(time.mktime(
                            time.strptime(coupon['endTime'] + ' 23:59:59', '%Y-%m-%d %H:%M:%S'))) * 1000 if isinstance(
                            coupon['endTime'], str) else coupon['endTime']
                        msg['data']['coupon'].append(
                            {'coupon_name': coupon['name'], 'start_time': start_time, 'end_time': end_time,
                             'coupon_batch_id': coupon['batchId'], 'coupon_Key': coupon['key'],
                             'coupon_type': coupon['couponType'], 'coupon_limit_type': coupon['limitType'],
                             'gt': qua, 'minus': minu,
                             'coupon_url': 'https:%s' % coupon['url'] if coupon['url'] else None,
                             'coupon_discountDesc': discount_json,
                             'coupon_money_limit': high,
                             'coupon_prom_type': 2 if len(discount_json['info']) == 1 else 4})
                    except:
                        continue
            else:
                if isinstance(coupon['beginTime'], str):
                    start_time = coupon['beginTime'] + ' 00:00' if not re.findall('\d+:\d+', coupon['beginTime']) else \
                        coupon['beginTime']
                else:
                    start_time = coupon['beginTime']
                if isinstance(coupon['endTime'], str):
                    end_time = coupon['endTime'] + ' 23:59' if not re.findall('\d+:\d+', coupon['endTime']) else coupon[
                        'endTime']
                else:
                    end_time = coupon['endTime']
                start_time = int(time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M'))) * 1000 if isinstance(
                    start_time, str) else start_time
                end_time = int(time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M'))) * 1000 if isinstance(end_time,
                                                                                                            str) else end_time
                msg['data']['coupon'].append(
                    {'coupon_name': coupon['name'], 'start_time': start_time, 'end_time': end_time,
                     'coupon_batch_id': coupon['batchId'], 'coupon_Key': coupon['key'],
                     'coupon_type': coupon['couponType'], 'coupon_limit_type': coupon['limitType'],
                     'gt': coupon['quota'], 'minus': coupon['discount'],
                     'coupon_url': 'https:%s' % coupon['url'] if coupon['url'] else None,
                     'coupon_discountDesc': discount_json,
                     'coupon_money_limit': None, 'coupon_prom_type': 3 if coupon['quota'] == 0 else 1})
        except:
            continue
    return msg


async def prom_parse(sku_ids):
    global task
    task_prom = task.copy()
    skuid = sku_ids['skuid']
    vender_id = sku_ids['vender_id']
    cat = sku_ids['cat']
    shop_id = sku_ids['shop_id']
    prom_url = 'https://cd.jd.com/promotion/v2?skuId={}&area=1_72_2799_0&shopId={}&venderId={}&cat={}'.format(skuid, shop_id, vender_id, quote(cat))

    task_prom['parse_rule'] = 'jd_x_prom'
    task_prom['url'] = prom_url
    task_prom['data'] = await crawler(prom_url, 'https://item.jd.com/{}.html'.format(skuid))

    prom_result = parse2result(task_prom)
    prom_result = order_price(prom_result)

    return prom_result


async def comment_parse(sku_ids):
    global task
    task_comment = task.copy()
    skuid = sku_ids['skuid']
    comment_url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds={}'.format(skuid)
    task_comment['parse_rule'] = 'jd_x_comment'
    task_comment['url'] = comment_url
    task_comment['data'] = await crawler(comment_url, 'https://item.jd.com/{}.html'.format(skuid))
    comment_result = parse2result(task_comment)
    return comment_result


async def video_parse(sku_ids):
    global task
    task_video = task.copy()
    skuid = sku_ids['skuid']
    vid = sku_ids['vid']
    if vid:
        video_url = 'https://c.3.cn/tencent/video_v3?vid={}'.format(vid)
        task_video['parse_rule'] = 'jd_x_video'
        task_video['url'] = video_url
        task_video['data'] = await crawler(video_url, 'https://item.jd.com/{}.html'.format(skuid))
        video_result = parse2result(task_video)
    else:
        video_result = {'platform': 'jingdong_2', 'data': {'video_url': None}}
    return video_result


async def mobile_parse(sku_ids):
    global task
    task_mobile = task.copy()
    skuid = sku_ids['skuid']
    moble_url = 'http://pm.3.cn/prices/pcpmgets?skuids={}&origin=2'.format(skuid)
    task_mobile['parse_rule'] = 'jd_x_moble_price'
    task_mobile['url'] = moble_url
    task_mobile['data'] = await crawler(moble_url)
    mobile_result = parse2result(task_mobile)
    data = mobile_result['data'].copy()
    mobile_result['data'] = {'info': {'def': data}}

    return mobile_result


async def wechat_parse(sku_ids):
    global task
    task_wechat = task.copy()
    skuid = sku_ids['skuid']
    wechet_url = 'http://wq.jd.com/item/view?sku={}'.format(skuid)
    task_wechat['parse_rule'] = 'jd_x_wechat_price'
    task_wechat['url'] = wechet_url
    task_wechat['data'] = await crawler(wechet_url)
    wechat_result = parse2result(task_wechat)
    data = wechat_result['data'].copy()
    wechat_result['data'] = {'info': {'def': data}}
    return wechat_result


async def earnest_parse(sku_ids):
    global task
    task_earnest = task.copy()
    skuid = sku_ids['skuid']
    earnest_url = 'https://yuding.jd.com/presaleInfo/getPresaleInfo.action?callback=jQuery&sku={}'.format(skuid)
    task_earnest['parse_rule'] = 'jd_x_earnest'
    task_earnest['url'] = earnest_url
    task_earnest['data'] = await crawler(earnest_url,  'https://item.jd.com/{}.html'.format(skuid))
    msg = parse2result(task_earnest)

    if "error" in msg['data']['info'] or msg['data']['info'] is None:
        msg['data'] = {'info': {'def': {'earnest_info': {}}}}
    else:
        obj = json.loads(msg['data']['info'])['ret']
        info = {'info': {'def': {'earnest_info': {
            'start_time': int(time.mktime(time.strptime(obj['presaleStartTime'], '%Y-%m-%d %H:%M:%S'))) * 1000,
            'end_time': int(time.mktime(time.strptime(obj['presaleEndTime'], '%Y-%m-%d %H:%M:%S'))) * 1000,
            'earnest': obj['earnest'],
            'current_price': obj['currentPrice'],
            "deposit_worth": obj["depositWorth"],
            "current_price": obj["currentPrice"],
            "original_price": str(obj["jdPrice"]),
            "platform_price": obj["oriPrice"],

        }}}}
        msg['data'] = info


    return msg


def get_jingdong_price_page(id):
    sa = time.time()
    page_parse, sku_ids = html_parse(id)
    # print(page_parse)
    print('基本页面时间', time.time() - sa)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    sa = time.time()
    tasks = [
        asyncio.ensure_future(detail_parse(sku_ids)),
        asyncio.ensure_future(price_parse(sku_ids)),
        asyncio.ensure_future(pin_parse(sku_ids)),
        asyncio.ensure_future(prom_parse(sku_ids)),
        asyncio.ensure_future(comment_parse(sku_ids)),
        asyncio.ensure_future(video_parse(sku_ids)),
        asyncio.ensure_future(mobile_parse(sku_ids)),
        asyncio.ensure_future(wechat_parse(sku_ids)),
        asyncio.ensure_future(earnest_parse(sku_ids)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('其他请求时间', time.time() - sa)

    # tasks = [
    #     gevent.spawn(detail_parse,sku_ids),
    #     gevent.spawn(price_parse,sku_ids),
    #     gevent.spawn(pin_parse,sku_ids),
    #     gevent.spawn(prom_parse,sku_ids),
    #     gevent.spawn(comment_parse,sku_ids),
    #     gevent.spawn(video_parse,sku_ids),
    #     gevent.spawn(mobile_parse,sku_ids),
    #     gevent.spawn(wechat_parse,sku_ids),
    #     gevent.spawn(earnest_parse,sku_ids)
    # ]
    # res = gevent.joinall(tasks)
    result_obj = {'platform': 'jingdong_2',}
    info = {'def': {}}

    for i in tasks: # for i in res:
        result = i.result()  # result = i.value
        info['def'].update(result['data']['info']['def']) if 'info' in result['data'] else result_obj.update(result['data'])
    result_obj.update(page_parse['data'])
    result_obj['info'] = info
    result_obj['url'] = 'https://item.jd.com/{}.html'.format(id)
    result_obj['id'] = id
    sa = time.time()
    result = compute(result_obj)
    print('价格计算时间', time.time() - sa)
    sa = time.time()
    loop.close()
    print('关闭loop时间', time.time() - sa)
    return json.dumps(result, ensure_ascii=False)



def get_base_info(iid):  # 获得基础信息
    page_parse, _ = html_parse(iid)

    del_data = ["brand_id", "cat3_id", "cat_id",
                "item_description_score", "root_cat_Id",
                "shop_desc_score", "shop_logistics_score",
                "shop_service_score", "start_sale_qty", "shop", "shop_id", "shop_url"]
    for i in del_data:
        if i in page_parse: page_parse.pop(i)


    return page_parse


def get_item_detail_imgs(iid):  # 获得详情图片
    _, sku_ids = html_parse(iid)
    loop = asyncio.new_event_loop()
    detail = asyncio.ensure_future(detail_parse(sku_ids), loop=loop)
    loop.run_until_complete(detail)
    detail = detail.result().get("data", {}).get("detail", [])
    # for i in enumerate(detail):
    #     detail[i[0]] ="http:" + i[1]
    return ["http:" + i for i in detail]


def get_item_prices(iid):
    _, sku_ids = html_parse(iid)
    loop = asyncio.new_event_loop()
    normal_price = asyncio.ensure_future(price_parse(sku_ids), loop=loop)
    pin_price = asyncio.ensure_future(pin_parse(sku_ids), loop=loop)

    loop.run_until_complete(asyncio.gather(normal_price, pin_price, loop=loop))

    normal_price = normal_price.result()
    prices = normal_price.get("data", {}).get("info", {}).get("def", {})
    quantity_has = normal_price.get("data", {}).get("quantity_has")
    pin_price = pin_price.result().get("data", {}).get("info", {}).get("def", {}).get('pingou_price', {}).get('pin_price')
    prices["pin_price"] = pin_price

    return {"prices": prices, 'quantity_has': quantity_has}


def get_item_yushou(iid):
    # _, sku_ids = html_parse(iid)
    loop = asyncio.new_event_loop()
    yushou_price = asyncio.ensure_future(earnest_parse({"skuid": iid}), loop=loop)
    loop.run_until_complete(yushou_price)
    yushou_price = yushou_price.result().get("data", {}).get("info", {}).get("def", {})
    return yushou_price


def get_item_prom(iid):
    _, sku_ids = html_parse(iid)
    loop = asyncio.new_event_loop()
    prom_detail = asyncio.ensure_future(prom_parse(sku_ids), loop=loop)
    loop.run_until_complete(prom_detail)
    return prom_detail.result().get("data", {})


def get_item_comment(iid):
    loop = asyncio.new_event_loop()
    comment = asyncio.ensure_future(comment_parse({"skuid": iid}), loop=loop)
    loop.run_until_complete(comment)
    return comment.result().get("data", {})


def get_item_video(iid):
    _, sku_ids = html_parse(iid)
    loop = asyncio.new_event_loop()
    video_info = asyncio.ensure_future(video_parse(sku_ids), loop=loop)
    loop.run_until_complete(video_info)
    return video_info.result().get("data", {})


@app.route("/<string:sort>/<string:func>")
def hello(sort, func):
    iid = request.args.get("id")
    if not iid or not iid.isdigit(): return jsonify({"msg":"id参数为空或者错误", "status": 400, "data": {}})
    if func == "base": return jsonify({"msg":"ok", "status": 200, "data": get_base_info(int(iid))})
    elif func == "detail": return jsonify({"msg":"ok", "status": 200, "data": get_item_detail_imgs(int(iid))})
    elif func == "price": return jsonify({"msg":"ok", "status": 200, "data": get_item_prices(int(iid))})
    elif func == "yushou": return jsonify({"msg":"ok", "status": 200, "data": get_item_yushou(int(iid))})
    elif func == "prom": return jsonify({"msg":"ok", "status": 200, "data": get_item_prom(int(iid))})
    elif func == "comment": return jsonify({"msg":"ok", "status": 200, "data": get_item_comment(int(iid))})
    elif func == "video": return jsonify({"msg":"ok", "status": 200, "data": get_item_video(int(iid))})

    return jsonify({"msg":"路径错误", "status": 400, "data": {}})



if __name__ == '__main__':
    app.run(port=8888)
    sa = time.time()
    # print(get_base_info(7874705))
    # print(get_item_detail_imgs(7874705))
    # print(get_item_prices(10824068895))
    # print(get_item_yushou(7874705))
    # print(get_item_prom(7874705))
    # print(get_item_comment(7874705))
    # print(get_item_video(8441388))

    # print(get_jingdong_price_page(7874705))
    print(time.time() - sa)
    # get_jingdong_price_page(31243589138)
    # get_jingdong_price_page(30411584308)