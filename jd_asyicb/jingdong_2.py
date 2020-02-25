import json
import re
from time import time


def get_min_price(json_str):
    obj = json.loads(json_str)
    price_info = obj['info']['def']
    plant_form = float(price_info['platform_price'])
    vip_price = float(price_info['vip_price']) if price_info['vip_price'] else None
    return plant_form, vip_price


def get_now_prom(json_str):
    obj = json.loads(json_str)
    return [prom for prom in obj['prom_info'] if
            prom['start_time'] <= int(time()) * 1000 <= prom['end_time']], [coup for coup in obj['coupon'] if coup['start_time'] <= int(time()) * 1000 <= coup['end_time']]


def get_now_future(json_str):
    obj = json.loads(json_str)
    future_prom = [prom for prom in obj['prom_info'] if prom['start_time'] > int(time()) * 1000 if
                   prom['prom_name'] in ['活动预告', '多买优惠', '跨店铺满折进行中', '跨自营/店铺满折', '满减', '跨店铺满减进行中', '跨自营/店铺满减']]
    future_coupon = [coup for coup in obj['coupon'] if coup['start_time'] > int(time()) * 1000]
    can_sum = []
    for p in future_prom if future_prom else []:
        can_sum.append([p, {}])
        for i in obj['coupon']:
            if p['start_time'] <= i['end_time']:
                can_sum.append([p, i])
        pass
    for c in future_coupon if future_coupon else []:
        can_sum.append([{}, c])
        for i in obj['prom_info']:
            if c['start_time'] <= i['end_time']:
                can_sum.append([i, c])
    return can_sum if can_sum else []

def get_pin_future(json_str, ed):
    obj = json.loads(json_str)
    future_prom = [prom for prom in obj['prom_info'] if prom['start_time'] > int(time()) * 1000 if
                   prom['prom_name'] in ['活动预告', '多买优惠', '跨店铺满折进行中', '跨自营/店铺满折', '满减', '跨店铺满减进行中', '跨自营/店铺满减']]
    future_coupon = [coup for coup in obj['coupon'] if coup['start_time'] > int(time()) * 1000]
    can_sum = []
    for p in future_prom if future_prom else []:
        can_sum.append([p, {}])
        for i in obj['coupon']:
            if p['start_time'] <= i['end_time'] and ed <= i['end_time']:
                can_sum.append([p, i])
        pass
    for c in future_coupon if future_coupon else []:
        can_sum.append([{}, c])
        for i in obj['prom_info']:
            if c['start_time'] <= i['end_time'] and ed <= i['end_time']:
                can_sum.append([i, c])
    return can_sum if can_sum else []



def manzhe(prom_msg, price):
    if '立减最低' in prom_msg:
        man = int(re.findall("满(\d+)件", prom_msg)[0])
        free = int(re.findall("立减最低(\d+)件", prom_msg)[0])
        if free > man: man, free = free, man
        return float('%.2f' % round(float(price) * ((man - free) / man), 2))
    else:
        zhekou = re.findall('打(\d+\.?\d*)', prom_msg)
        zhekou = float(zhekou[0]) if zhekou else 1
        # 让折扣成为小于等于1大于0的数字
        if zhekou and zhekou > 10:
            zhekou = zhekou / 100
        elif zhekou and 1 < zhekou < 10:
            zhekou = zhekou / 10
        return float('%.2f' % round(float(price) * zhekou, 2))


def manjian(prom_msg, price):
    xuan = re.findall('(\d+)元选(\d+)件', prom_msg)
    if '每满' in prom_msg:
        man = re.findall(r'每满(\d+\.?\d*)', prom_msg)
        sheng = re.findall(r'，可减(\d+\.?\d*)', prom_msg)
        max_d = re.findall(r'最多可减(\d+\.?\d*)', prom_msg)
        if not man:
            return float(price)
        # 文本转浮点
        man = float(man[0])
        sheng = float(sheng[0])
        price = float(price)
        jian_money = sheng * (price // man)
        if max_d:
            max_d = float(max_d[0])
            jian_money = max_d if jian_money >= max_d else jian_money

        # 判断是否符合满减条件
        price = price - jian_money
    elif xuan:
        yuan = float(xuan[0][0])
        xuan = float(xuan[0][1])
        return float('%.2f' % (yuan / xuan))

    else:
        man = re.findall(r'满(\d+\.?\d*)', prom_msg)
        sheng = re.findall(r'减(\d+\.?\d*)', prom_msg)
        if not man:
            return float(price)
        # 文本转浮点
        man = float(man[0])
        sheng = float(sheng[0])
        price = float(price)
        # 判断是否符合满减条件
        if price >= man:
            price = price - sheng
    return float('%.2f' % price)





class get_price(object):
    def __init__(self, info):
        self.info = info
        price_get = get_min_price(info)
        self.plant_price = price_get[0]
        self.vip_price = price_get[1]
        self.prom_now = get_now_prom(info)
        self.prom_future = get_now_future(info)
        self.mobile_price = json.loads(info)['info']['def']['mobile_price']
        self.wechat_price = json.loads(info)['info']['def']['wechat_price']
        self.earnest_info = json.loads(info)['info']['def']['earnest_info'] if json.loads(info)['info']['def'].get('earnest_info') else None
        self.pingou = json.loads(info)['info']['def']['pingou_price'] if json.loads(info)['info']['def'].get('pingou_price') else None
        self.fan_price = json.loads(info)['info']['def']['fan_price']

    def get_min_price_now_prom(self, price, plt):
        price_now = [(price, None, None, None, None, plt), ]
        for i in self.prom_now[0]:
            if i['prom_name'] in ['活动预告', '多买优惠', '跨店铺满折进行中', '跨自营/店铺满折']:
                # try:
                price_now.append((manzhe(i['prom_msg'], price), i['prom_id'], i['prom_msg'], i['start_time'], i['end_time'], plt))
                # except:pass
            elif i['prom_name'] in ['满减', '跨店铺满减进行中', '跨自营/店铺满减']:
                # try:
                price_now.append((manjian(i['prom_msg'], price), i['prom_id'], i['prom_msg'], i['start_time'], i['end_time'], plt))
                # except:pass
        price_now.sort(key=lambda x: x[0])

        prom_price_m = price_now[0]
        return prom_price_m

    def get_min_price_now_coupon(self, price_now_t, plt):
        up_info = price_now_t[2]
        jian = 1
        zhe = re.findall('(\d+)件', up_info) if up_info else up_info
        xuan = re.findall('(\d+)元选\d+件', up_info) if up_info else up_info
        if zhe:
            try:
                jian = int(zhe[0])
            except:pass
        price_now = price_now_t[0]

        price_min = [(price_now_t[0], {}, None, None, plt)]
        sum_price = price_now * jian if not xuan else int(xuan[0])  # 计算总价格
        for c in self.prom_now[1]:
            if c['gt'] <= sum_price:
                if c['coupon_prom_type'] in [2, 4]:
                    try:
                        discount = c['minus']
                        high = c['coupon_money_limit']
                        minus = price_now * jian * (1 - discount)
                        minus = minus if minus <= float(high) else float(high)
                        price_min.append((round((price_now * jian - minus) / jian, 2), c, c['start_time'], c['end_time'], plt))
                    except Exception as e:continue
                else:
                    price_min.append((round(price_now - c['minus'] / jian, 2), c, c['start_time'], c['end_time'], plt))

        price_min.sort(key=lambda x: x[0])
        return price_min[0]

    def get_min_price_future(self, price, pin_futrue=None):
        can_sum = self.prom_future if not pin_futrue else pin_futrue
        price = float(price)
        price_f = []
        for i in can_sum:
            prom_info = i[0]
            coupon_info = i[1]
            price_p = price, None
            prom_dis = price, {}, 0, 10 ** 25
            if prom_info.get('prom_name', None) in ['活动预告', '多买优惠', '跨店铺满折进行中', '跨自营/店铺满折']:
                prom_dis = (manzhe(prom_info['prom_msg'], price), prom_info['prom_id'], prom_info['start_time'],
                            prom_info['end_time'], prom_info['prom_msg'])
                price_p = prom_dis[0], prom_dis[4]
            elif prom_info.get('prom_name', None) in ['满减', '跨店铺满减进行中', '跨自营/店铺满减']:
                prom_dis = (manjian(prom_info['prom_msg'], price), prom_info['prom_id'], prom_info['start_time'],
                            prom_info['end_time'], prom_info['prom_msg'])
                price_p = prom_dis[0], prom_dis[4]

            if coupon_info:
                jian = 1
                zhe = re.findall('(\d+)件', price_p[1]) if price_p[1] else price_p[1]
                xuan = re.findall('(\d+)元选\d+件', price_p[1]) if price_p[1] else price_p[1]
                if zhe:
                    try:
                        jian = int(zhe[0])
                    except:
                        pass
                price_a_prom = prom_dis[0], {}, prom_dis[2], prom_dis[3]
                sum_price = price_p[0] * jian if not xuan else int(xuan[0])
                if coupon_info['gt'] <= sum_price:
                    if coupon_info['coupon_prom_type'] in [2, 4]:
                        try:
                            discount = coupon_info['minus']
                            high = coupon_info['coupon_money_limit']
                            minus = price_p[0] * jian * (1 - discount)
                            minus = minus if minus <= float(high) else float(high)
                            price_a_prom = (round((price_p[0] * jian - minus) / jian, 2), coupon_info, coupon_info['start_time'], coupon_info['end_time'])
                        except Exception as e:
                            continue
                    else:
                        price_a_prom = (round(price_p[0] - coupon_info['minus'] / jian, 2), coupon_info, coupon_info['start_time'], coupon_info['end_time'])
                price_f.append((price_a_prom[0], max([prom_dis[2], price_a_prom[2]]),
                                min([prom_dis[3], price_a_prom[3]]), prom_dis, price_a_prom))
            else:
                price_f.append((prom_dis[0], prom_dis[2], prom_dis[3], prom_dis, {}))
        price_f.sort(key=lambda x: x[0])
        if price_f:
            result = price_f[0]
            if result[2] == 10 ** 25:
                return None, None, None
            return result[0], result[1], result[2]
        return None, None, None

    def get_now_all_info(self):
        prom_info = self.get_min_price_now_prom(self.plant_price, 'PC')
        coupon_info = self.get_min_price_now_coupon(prom_info, 'PC')
        plant_all = [self.plant_price, prom_info, coupon_info]
        # if not self.vip_price: return plant_all
        plant_all_v = None
        if self.vip_price:
            prom_info_v = self.get_min_price_now_prom(self.vip_price, 'PC')
            coupon_info_v = self.get_min_price_now_coupon(prom_info_v, 'PC')
            plant_all_v = [self.vip_price, prom_info_v, coupon_info_v]
        plant_all_m = None
        if self.mobile_price:
            prom_info_m = self.get_min_price_now_prom(float(self.mobile_price), 'mobile')
            coupon_info_m = self.get_min_price_now_coupon(prom_info_m, 'mobile')
            plant_all_m = [float(self.mobile_price), prom_info_m, coupon_info_m]

        plant_all_w = None
        if self.wechat_price:
            prom_info_w = self.get_min_price_now_prom(float(self.wechat_price), 'wechat')
            coupon_info_w = self.get_min_price_now_coupon(prom_info_w, 'wechat')
            plant_all_w = [float(self.mobile_price), prom_info_w, coupon_info_w]

        plant_all_earn = None
        if self.earnest_info and self.earnest_info['earnest']:
            if int(self.earnest_info['start_time']) <= time() * 1000 <= int(self.earnest_info['end_time']):
               plant_all_earn = [float(self.earnest_info['current_price']),(float(self.earnest_info['current_price']), None, None, self.earnest_info['start_time'], self.earnest_info['end_time'],'PC'), (float(self.earnest_info['current_price']), None, None, None,'PC')]

        plant_all_pin = None
        if self.pingou:
            # st = int(time() * 1000)
            ed = int((time() + int(self.pingou['lefttime'])) * 1000)
            prom_info_pin = list(self.get_min_price_now_prom(float(self.pingou['pin_price']), 'mobile'))
            if prom_info_pin[4]: prom_info_pin[4] = ed if prom_info_pin[4] > ed else prom_info_pin[4]
            coupon_info_pin = list(self.get_min_price_now_coupon(prom_info_pin, 'mobile'))
            if coupon_info_pin[1]: coupon_info_pin[1]['end_time'] = ed if coupon_info_pin[1]['end_time'] > ed else coupon_info_pin[1]['end_time']
            plant_all_pin = [float(self.pingou['pin_price']), prom_info_pin, coupon_info_pin]

        plant_all_fan = None
        if self.fan_price:
            prom_info_fan = self.get_min_price_now_prom(float(self.fan_price), 'PC')
            coupon_info_fan = self.get_min_price_now_coupon(prom_info_fan, 'PC')
            plant_all_fan = [float(self.fan_price), prom_info_fan, coupon_info_fan]

        info_all= [plant_all, plant_all_v, plant_all_m, plant_all_w, plant_all_earn, plant_all_pin, plant_all_fan]
        info_all = [i for i in info_all if i]
        info_all.sort(key=lambda x: x[2][0]) # 这是所有的数据

        result = info_all[0]
        start_time = [i for i in (result[1][3], result[2][2]) if i]
        end_time = [i for i in (result[1][4], result[2][3]) if i]
        start_time = max(start_time) if start_time else None
        end_time = min(end_time) if end_time else None

        plantfrom = result[-1][-1]
        if len(info_all) > 2:
            if info_all[0][2][0] == info_all[1][2][0] and info_all[1][2][0] == info_all[2][2][0]:
                plantfrom = 'PC'
        prom_i = list(result[1])
        coupon_i = list(result[2])
        prom_i[-1] = plantfrom
        coupon_i[-1] = plantfrom
        return result[0], prom_i, coupon_i, start_time, end_time


    def get_future_all(self):
        future = [(self.get_min_price_future(self.plant_price), 'PC'), ]

        if self.vip_price: future.append((self.get_min_price_future(self.vip_price), 'PC'))
        if self.mobile_price: future.append((self.get_min_price_future(self.mobile_price), 'mobile'))
        if self.wechat_price: future.append((self.get_min_price_future(self.wechat_price), 'wechat'))
        if self.fan_price: future.append((self.get_min_price_future(self.fan_price), 'PC'))
        ed = None
        if self.pingou:
            ed = int((time() + int(self.pingou['lefttime'])) * 1000)
            pin_future = get_pin_future(self.info, ed)
            future.append((self.get_min_price_future(self.pingou['pin_price'], pin_future), 'mobile'))

        future = [i for i in future if i[0][0]]
        future.sort(key= lambda x: x[0][0])
        future = future[0] if future else None
        if not future: return None, None, None, None
        if ed:future[0][2] = future[0][2] if ed > future[0][2] else ed
        return future[0][0], future[0][1], future[0][2], future[1]









def compute(info_obj):
    info = json.dumps(info_obj, ensure_ascii=False)
    price = get_price(info)

    # 各种price
    platform_price = info_obj['info']['def']['platform_price']
    original_price = info_obj['info']['def']['original_price']
    vip_price = info_obj['info']['def']['vip_price']
    pingou_price = info_obj['info']['def']['pingou_price']
    mobile_price = info_obj['info']['def']['mobile_price']
    wechat_price = info_obj['info']['def']['wechat_price']

    prom_info = info_obj['prom_info']
    coupon = info_obj['coupon']

    # 进行运算
    result_info = price.get_now_all_info()  # 计算好的目前价格


    # 从类中拿数据
    prom_data = result_info[1]
    coupon_data = result_info[2]


    # 现在
    curr_price = result_info[0]
    curr_type = coupon_data[-1]
    curr_start_time = None
    curr_end_time = None

    # 最终
    finally_price = coupon_data[0]
    finally_start_time = result_info[3]
    finally_end_time = result_info[4]

    # 未来
    future_info = price.get_future_all()
    future_price = future_info[0]
    future_type = future_info[3]
    future_start_time = future_info[1]
    future_end_time = future_info[2]

    # 优惠信息
    prom_id = prom_data[1]
    prom_price = prom_data[0] if prom_id else None
    prom_prom_msg = prom_data[2]

    # 优惠券
    if isinstance(coupon_data[1], dict):
        coupon_price = coupon_data[0]
        coupon_key = coupon_data[1].get('coupon_Key', None)
        coupon_type = coupon_data[1].get('coupon_type', None)
        coupon_name = coupon_data[1].get('coupon_name', None)
        coupon_limit_type = coupon_data[1].get('coupon_limit_type', None)
        coupon_end_time = coupon_data[1].get('end_time', None)
        coupon_start_time = coupon_data[1].get('start_time', None)
        coupon_url = coupon_data[1].get('coupon_url', None)
        coupon_to_url = coupon_data[1].get('coupon_url', None)
        coupon_gt = coupon_data[1].get('gt', None)
        coupon_minus = coupon_data[1].get('minus', None)
        coupon_batch_id = coupon_data[1].get('coupon_batch_id', None)
        coupon_money_limit = coupon_data[1].get('coupon_money_limit', None)
        coupon_prom_type = coupon_data[1].get('coupon_prom_type', None)
        roleId = None
        if coupon_to_url:
            roleId = int(re.findall('roleId=(\d+)', coupon_to_url)[0]) if re.findall('roleId=(\d+)', coupon_to_url) else None
        coupon_role_id = roleId


    else:
        coupon_price, coupon_key, coupon_type, coupon_name, coupon_limit_type, coupon_end_time, coupon_start_time = None, None, None, None, None, None, None
        coupon_url, coupon_to_url, coupon_gt, coupon_minus, coupon_batch_id, coupon_role_id = None, None, None, None, None, None
        coupon_money_limit, coupon_prom_type = None, None

    result = {
        'platform_price': platform_price,
        'original_price': original_price,
        'vip_price': vip_price,
        'finally_price': finally_price,
        'finally_start_time': finally_start_time,
        'finally_end_time': finally_end_time,
        'curr_price': curr_price,
        'curr_type': curr_type,
        'curr_start_time': curr_start_time,
        'curr_end_time': curr_end_time,
        'future_price': future_price,
        'future_type': future_type,
        'future_start_time': future_start_time,
        'future_end_time': future_end_time,
        'pingou_price': pingou_price,
        'mobile_price': mobile_price,
        'wechat_price': wechat_price,
        'prom_info': prom_info,
        'prom_id': prom_id,
        'prom_price': prom_price,
        'prom_prom_msg': prom_prom_msg,
        'coupon': coupon,
        'coupon_price': coupon_price,
        'coupon_key': coupon_key,
        'coupon_type': coupon_type,
        'coupon_name': coupon_name,
        'coupon_limit_type': coupon_limit_type,
        'coupon_end_time': coupon_end_time,
        'coupon_start_time': coupon_start_time,
        'coupon_url': coupon_url,
        'coupon_to_url': coupon_to_url,
        'coupon_gt': coupon_gt,
        'coupon_minus': coupon_minus,
        'coupon_batch_id': coupon_batch_id,
        'coupon_role_id': coupon_role_id,
        'coupon_money_limit': coupon_money_limit,
        'coupon_prom_type': coupon_prom_type,
        'invalid_flag': True
    }
    if 'priceTip' in info_obj['info']['def']: info_obj['info']['priceTip'] = info_obj['info']['def'].pop('priceTip')
    info_obj.update(result)
    if float(info_obj['platform_price']) < 0:
        info_obj['invalid_flag'] = False
    return info_obj




if __name__ == '__main__':
    text = ' 每满999元，可减200元现金'
    print(manjian(text, 76990))


