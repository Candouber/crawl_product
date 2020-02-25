import json

import requests

import pymongo
# payloadData = {
# 'type1': 100,
# 'type2': "0",
# 'type3': "0",
# 'type4': "0",
# "csrf-token": "IjAzNmQ1MDZkMWQ5MWIyMTgwZTA5NGRjNDEwZTEyZDE5NDEwMjRjN2Qi.EOSG6w.dHU_HjaXVQNocw6-iZobYPeQ71I"
# }
#
#
# payloadHeader = {
#     'Content-Type': 'application/json',
# "X-CSRFToken":"IjJiNTNhM2VjYmI4YTc1OTljNDM3ZDJlOWI0ZTU3NWE1YTM2MWYzZTci.EOSZwg.yg3Q1kLPyFfv9p4kfHo50qgP3pA",
# "Cookie":"session=9b52f70d-0819-44cc-9142-098e081cc900.Sgzil0LP9ykYoL4YtKFdbEaeSlw",
# }
#
# postUrl = "http://localhost:8080/api/getMsg"
# # while 1:
# r = requests.post(postUrl, data=json.dumps(payloadData), headers=payloadHeader)
#
# print(r.headers)


# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class A(db.Model):
#     aaa = "aaa"


# print(A.aaa)
# print(A["aaa"])

#####################################
# mongodb
mgo = pymongo.MongoClient()

db = mgo["daita"]


coll = db["api"]



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




coll.update_one({"useful": base_info.pop("useful")}, {"$set": base_info}, upsert=True)



































