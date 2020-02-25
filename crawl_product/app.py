# coding=gbk
import pymysql
from flask import Flask, jsonify, request
import json
import requests
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
database = "daita"
db = pymysql.connect("localhost", "root", "123456", database, charset="utf8")



@app.route('/getMsg', methods=['POST', 'GET'])
def get_msg():
    res = request.data
    res = res.decode()
    res = json.loads(res)
    print(res)
    r1 = int(res['type1'])
    r2 = int(res['type2'])
    r3 = int(res['type3'])
    r4 = int(res['type4'])
    r_list = [r1, r2, r3, r4]
    cursor = db.cursor()
    print(":::::::",r1)
    cursor.execute("select name from typeList where type='type1' and type_id={}".format(r1))
    t1_name = cursor.fetchone()[0]
    cursor.execute("select name from typeList where type='type2' and type_id={}".format(r2))
    t2_name = cursor.fetchone()[0]
    cursor.execute('select name from typeList where type="type3" and type_id={}'.format(r3))
    t3_name = cursor.fetchone()[0]
    cursor.execute('select name from typeList where type="type4" and type_id={}'.format(r4))
    t4_name = cursor.fetchone()[0]
    name_list = [t1_name, t2_name, t3_name, t4_name]
    print(name_list)
    base_exe = "select name, url from api where"
    for i in range(len(r_list)):
        if r_list[i] != 0:
            base_exe += ' type{}="{}" and'.format(str(i+1), name_list[i])
    if base_exe != "select name, url from api where":
        base_exe = base_exe[:-3]
    else:
        base_exe = base_exe[:-5]
    print(base_exe)
    cursor.execute(base_exe)
    res = cursor.fetchall()
    name = []
    url = []
    for n, u in res:
        name.append(n)
        url.append(u)
    final = {
        'name': name,
        'url': url
    }
    print(final)
    return jsonify(final)



@app.route('/getMsg/two', methods=['POST', 'GET'])
def get_msg_two():
    res = request.data
    res = res.decode()
    res = json.loads(res)
    print(res['name'])
    cursor = db.cursor()
    cursor.execute("select type1, type2, type3, type4 from api where name={}".format(res))
    type_t = cursor.fetchall()
    type_l = {}
    for i in type_t:
        num = 1
        type_l.update({
            'type{}'.format(num): i
        })
        num += 1
    print(type_l)
    return jsonify({
        type_l
    })


@app.route("/jd")
def hello():
    return "Hello World!"


@app.route("/detail_nav")
def detail_nav():
    data = {"data":[]}


    data["data"] = [
        {"name": "京东基础信息接口", "to": "/detail?sort=京东&api=京东基础信息接口"},
        {"name": "京东基础价格接口", "to": "/detail?sort=京东&api=京东基础价格接口"},
        {"name": "京东优惠信息接口", "to": "/detail?sort=京东&api=京东优惠信息接口"},
        {"name": "京东预售信息接口", "to": "/detail?sort=京东&api=京东预售信息接口"},
        {"name": "京东商品好评率接口", "to": "/detail?sort=京东&api=京东商品好评率接口"},
    ]
    return jsonify(data)


@app.route("/detail_base")
def detail_baseInfo():
    base_info = {
        "pathBy": "京东",
        "useful": "京东基础信息接口",
        "apiType": "API",
        "version": "v1.0(0)",
        "creatTime": "2018-05-02",
        "updateTime": "2019-09-21",
        "hot": 999,
        "produce": "jd单品的基本信息",
        "update": {
            "new": {
                "updateTime": "2019-12-01",
                "updateInfo": "更新了一些众所周知的问题"
            },
            "history": [
                {
                    "updateTime": "2019-12-02",
                    "updateInfo": "更新了一些众所周知的问题"
                },
                {
                    "updateTime": "2019-12-03",
                    "updateInfo": "更新了一些众所周知的问题"
                },
                {
                    "updateTime": "2019-12-12",
                    "updateInfo": "更新了一些众所周知的问题"
                },

            ]
        },
        "jsonExample": {
            "data": {"brand_name": "华为（HUAWEI）", "cat_name_1": "手机通讯", "cat_name_2": "手机", "cat_name_3": "手机",
                     "img_urls": [
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t1/22718/1/12601/168068/5caedd41E05e879b0/865565d919219154.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t26566/130/1777317082/169052/23a35173/5bf4b276N43dbe017.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t30403/71/150100317/139642/b3ad6bcf/5bf4b277N9ede9770.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t27640/121/1971732627/42404/394bd8ca/5bf4b277N08512748.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t30694/48/450873641/53424/12095385/5bf4b277N574ab272.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t26935/339/2001258817/58623/1dfac72e/5bf4b278N9f230cd2.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t27568/122/2011591872/144168/7ba5e8de/5bf4b283N5bbda406.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t30340/132/460186811/89943/48de97cb/5bf4b283Nbb704105.jpg"],
                     "property_map": [{"skuId": 100001467225, "版本": "全网通（4GB 64GB）", "颜色": "幻夜黑"},
                                      {"skuId": 100002071800, "版本": "全网通（6GB 64GB）", "颜色": "幻夜黑"},
                                      {"skuId": 100002071796, "版本": "全网通（6GB 128GB）", "颜色": "幻夜黑"},
                                      {"skuId": 100001550349, "版本": "全网通（4GB 64GB）", "颜色": "渐变蓝"},
                                      {"skuId": 100002071798, "版本": "全网通（6GB 64GB）", "颜色": "渐变蓝"},
                                      {"skuId": 100002071794, "版本": "全网通（6GB 128GB）", "颜色": "渐变蓝"},
                                      {"skuId": 100002071812, "版本": "全网通（4GB 64GB）", "颜色": "渐变红"},
                                      {"skuId": 100001550347, "版本": "全网通（6GB 64GB）", "颜色": "渐变红"},
                                      {"skuId": 100001550375, "版本": "全网通（6GB 128GB）", "颜色": "渐变红"},
                                      {"skuId": 100002380994, "版本": "全网通（4GB 64GB）", "颜色": "铃兰白"},
                                      {"skuId": 100002380984, "版本": "全网通（6GB 64GB）", "颜色": "铃兰白"}],
                     "spec_param": ["商品名称：华为荣耀10青春版", "商品编号：100001550349", "商品毛重：162.00g", "商品产地：中国大陆", "CPU型号：其他",
                                    "运行内存：4GB", "机身存储：64GB", "存储卡：其它存储卡", "摄像头数量：后置双摄", "后摄主摄像素：1300万像素",
                                    "前摄主摄像素：2400万像素", "拍照特点：后置双摄", "主屏幕尺寸（英寸）：6.21英寸", "分辨率：全高清FHD+", "屏幕比例：其它屏幕比例",
                                    "屏幕前摄组合：其他", "电池容量（mAh）：3400mAh（典型值）", "充电器：5V/2A", "机身颜色：渐变蓝", "操作系统：Android(安卓)",
                                    "游戏性能：其他"], "thirdpart_flag": "自营",
                     "title": "荣耀10青春版 幻彩渐变 2400万AI自拍 全网通版4GB+64GB 渐变蓝 移动联通电信4G全面屏手机"}, "msg": "ok", "status": 200},

        "requestInfo": {
            "uri": "点击“开始使用”按钮在工作台中使用",
            "struct": "json",
            "method": "GET",
            "demo": "点击“开始使用”按钮在工作台中使用",
            "data": [
                {"id": 1, "key": "product_id", "name": "商品id", "type": "int", "comment": "商品在京东平台的唯一编码"},
            ],
            "return": [
                {"id": 1, "key": "msg", "name": "响应信息", "type": "string", "comment": "ok代表成功，其余情况代表有错误"},
                {"id": 2, "key": "status", "name": "响应状态", "type": "string", "comment": "200代表正常返回，其余情况代表有错误"},
                {"id": 2, "key": "data", "name": "响应数据", "type": "object", "comment": '返回的数据，具体字段请点击字段说明标签查看'},
            ],
        },
        "filedMean": [
            {"id": 1, "key": "brand_name", "name": "品牌名称", "type": "string", "comment": "商品所属品牌的名称"},
            {"id": 2, "key": "cat_name_1", "name": "第一层分类", "type": "string", "comment": "在jd平台上的顶层分类"},
            {"id": 3, "key": "cat_name_2", "name": "第二层分类", "type": "string", "comment": "jd第一层分类的子集"},
            {"id": 4, "key": "cat_name_3", "name": "第三层分类", "type": "string", "comment": "jd分类的最末层分类"},
            {"id": 5, "key": "img_urls", "name": "商品头图", "type": "list->string", "comment": "商品头图（小）"},
            {"id": 6, "key": "property_map", "name": "其他sku", "type": "list->map",
             "comment": "同一spu下的sku，商品不同，，map下的字段不同"},
            {"id": 7, "key": "spec_param", "name": "商品参数", "type": "string", "comment": "商品的参数"},
            {"id": 8, "key": "thirdpart_flag", "name": "是否自营", "type": "string or null",
             "comment": "自营商品显示“自营”，否则null"},
            {"id": 9, "key": "title", "name": "商品标题", "type": "string", "comment": "商品的标题"},
        ],
    }


    base_info["pathBy"] = request.args.get("sort")
    base_info["useful"] = request.args.get("api")
    return jsonify(base_info)


@app.route("/table_api")
def get_table_apis():
    sort = request.args.get("sort")
    api = request.args.get("api")

    apis = {'京东基础信息接口': 'jingdong/base', '京东基础价格接口': 'jingdong/price', '京东优惠信息接口': 'jingdong/prom', '京东预售信息接口': 'jingdong/yushou', '京东商品好评率接口': 'jingdong/comment',}


    result = []
    if api in apis: result.append({"label": api, "value": apis.pop(api)})
    for k, v in apis.items():result.append({"label": k, "value": v})
    return jsonify(result)


@app.route("/api_params")
def get_api_param():
    sort = request.args.get("sort")
    api = request.args.get("api")
    return jsonify({'product_id' : {"name": "商品id", "value":""},})


@app.route("/api_data", methods=["GET", "POST"])
def get_api_data():
    data = json.loads(request.data)

    api_name = data.get("API")
    param = data.get("data")
    param["id"] = param.pop("product_id")

    result = json.loads(requests.get("http://127.0.0.1:8888/"+ api_name, params=param).text)

    filedMean = [
            {"id": 1, "key": "brand_name", "name": "品牌名称", "type": "string", "comment": "商品所属品牌的名称"},
            {"id": 2, "key": "cat_name_1", "name": "第一层分类", "type": "string", "comment": "在jd平台上的顶层分类"},
            {"id": 3, "key": "cat_name_2", "name": "第二层分类", "type": "string", "comment": "jd第一层分类的子集"},
            {"id": 4, "key": "cat_name_3", "name": "第三层分类", "type": "string", "comment": "jd分类的最末层分类"},
            {"id": 5, "key": "img_urls", "name": "商品头图", "type": "list->string", "comment": "商品头图（小）"},
            {"id": 6, "key": "property_map", "name": "其他sku", "type": "list->map",
             "comment": "同一spu下的sku，商品不同，，map下的字段不同"},
            {"id": 7, "key": "spec_param", "name": "商品参数", "type": "string", "comment": "商品的参数"},
            {"id": 8, "key": "thirdpart_flag", "name": "是否自营", "type": "string or null",
             "comment": "自营商品显示“自营”，否则null"},
            {"id": 9, "key": "title", "name": "商品标题", "type": "string", "comment": "商品的标题"},
        ]

    result_info = {
        "jsonExample": result,
        "filedMean": filedMean,
    }

    return jsonify(result_info)





if __name__ == '__main__':
    app.run()


# value: 'jingdong/base',
# label: '京东基础信息接口'；
# value: 'jingdong/price',
# label: '京东基础价格接口'；
# value: 'jingdong/prom',
# label: '京东优惠信息接口'；
#  value: 'jingdong/pingou',
# label: '京东拼购信息接口'；
#  value: 'jingdong/good',
#  label: '京东商品好评率接口'；


