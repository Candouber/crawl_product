import json, requests
from application import db
from .module import Api, Typelist
from . import index
from flask import render_template, request, flash, jsonify, current_app
from ... import csrf
from flask_wtf.csrf import generate_csrf
from application import mgo
from .utils import INIT_MGO_DB
# @index.before_request
# def validate_requests():
#     print(generate_csrf())




@csrf.exempt
@index.route('/getMsg', methods=['POST', 'GET'])
def get_list_msg():
    if request.method == "GET": return generate_csrf()
    res = request.data
    res = res.decode()
    res = json.loads(res)
    print(res)
    r1 = int(res['type1'])
    r2 = int(res['type2'])
    r3 = int(res['type3'])
    r4 = int(res['type4'])


    type_filters = [
        db.and_(Typelist.get_attr("type") == "type1", Typelist.type_id == r1),
        db.and_(Typelist.get_attr("type") == "type2", Typelist.type_id == r2),
        db.and_(Typelist.get_attr("type") == "type3", Typelist.type_id == r3),
        db.and_(Typelist.get_attr("type") == "type4", Typelist.type_id == r4)
    ]

    type_list = {i.type:i.name for i in Typelist.query.filter(db.or_(*type_filters)) if i.name != "全部"}

    api_list = Api.query.filter_by(**type_list).all()

    final = {'name': [], 'url': []}
    for api in api_list: final['name'].append(api.name); final['url'].append(api.url)

    return jsonify(final)


@index.route("/detail_nav")
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


@index.route("/detail_base")
def detail_baseInfo():
    base_info = mgo[INIT_MGO_DB]["api"].find_one({"useful" : "京东基础信息接口"})
    if isinstance(base_info, dict) and '_id' in base_info: base_info.pop('_id')
    base_info["pathBy"] = request.args.get("sort")
    base_info["useful"] = request.args.get("api")
    return jsonify(base_info)


@index.route("/table_api")
def get_table_apis():
    sort = request.args.get("sort")
    api = request.args.get("api")

    apis = {i.name:i.com for i in Api.query.filter_by(sort=sort).all()}

    result = []
    if api in apis: result.append({"label": api, "value": json.dumps({"name":api, "val": apis.pop(api)})})
    for k, v in apis.items():result.append({"label": k, "value": json.dumps({"name":k, "val": v})})
    return jsonify(result)


@index.route("/api_params")
def get_api_param():
    sort = request.args.get("sort")
    api = request.args.get("api")

    infos = mgo[INIT_MGO_DB]["api"].find_one({"useful": api})
    if not infos: return jsonify({})
    filelds = infos.get("requestInfo", {}).get("data", [])

    return jsonify({i["key"]: {"name": i["name"], "value": ""} for i in filelds})


@index.route("/api_data", methods=["GET", "POST"])
def get_api_data():
    data = json.loads(request.data)
    print(data)
    api_name = data.get("API")
    param = data.get("data")
    param["id"] = param.pop("product_id")



    result = json.loads(requests.get("http://127.0.0.1:8888/" + api_name, params=param).text)

    sort = data["sort"]
    api = data["name"]

    infos = mgo[INIT_MGO_DB]["api"].find_one({"useful": api})
    filedMean = infos.get("filedMean", [])


    result_info = {
        "jsonExample": result,
        "filedMean": filedMean,
    }

    return jsonify(result_info)









