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
        {"name": "����������Ϣ�ӿ�", "to": "/detail?sort=����&api=����������Ϣ�ӿ�"},
        {"name": "���������۸�ӿ�", "to": "/detail?sort=����&api=���������۸�ӿ�"},
        {"name": "�����Ż���Ϣ�ӿ�", "to": "/detail?sort=����&api=�����Ż���Ϣ�ӿ�"},
        {"name": "����Ԥ����Ϣ�ӿ�", "to": "/detail?sort=����&api=����Ԥ����Ϣ�ӿ�"},
        {"name": "������Ʒ�����ʽӿ�", "to": "/detail?sort=����&api=������Ʒ�����ʽӿ�"},
    ]
    return jsonify(data)


@app.route("/detail_base")
def detail_baseInfo():
    base_info = {
        "pathBy": "����",
        "useful": "����������Ϣ�ӿ�",
        "apiType": "API",
        "version": "v1.0(0)",
        "creatTime": "2018-05-02",
        "updateTime": "2019-09-21",
        "hot": 999,
        "produce": "jd��Ʒ�Ļ�����Ϣ",
        "update": {
            "new": {
                "updateTime": "2019-12-01",
                "updateInfo": "������һЩ������֪������"
            },
            "history": [
                {
                    "updateTime": "2019-12-02",
                    "updateInfo": "������һЩ������֪������"
                },
                {
                    "updateTime": "2019-12-03",
                    "updateInfo": "������һЩ������֪������"
                },
                {
                    "updateTime": "2019-12-12",
                    "updateInfo": "������һЩ������֪������"
                },

            ]
        },
        "jsonExample": {
            "data": {"brand_name": "��Ϊ��HUAWEI��", "cat_name_1": "�ֻ�ͨѶ", "cat_name_2": "�ֻ�", "cat_name_3": "�ֻ�",
                     "img_urls": [
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t1/22718/1/12601/168068/5caedd41E05e879b0/865565d919219154.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t26566/130/1777317082/169052/23a35173/5bf4b276N43dbe017.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t30403/71/150100317/139642/b3ad6bcf/5bf4b277N9ede9770.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t27640/121/1971732627/42404/394bd8ca/5bf4b277N08512748.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t30694/48/450873641/53424/12095385/5bf4b277N574ab272.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t26935/339/2001258817/58623/1dfac72e/5bf4b278N9f230cd2.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t27568/122/2011591872/144168/7ba5e8de/5bf4b283N5bbda406.jpg",
                         "https://img14.360buyimg.com/n5/s54x54_jfs/t30340/132/460186811/89943/48de97cb/5bf4b283Nbb704105.jpg"],
                     "property_map": [{"skuId": 100001467225, "�汾": "ȫ��ͨ��4GB 64GB��", "��ɫ": "��ҹ��"},
                                      {"skuId": 100002071800, "�汾": "ȫ��ͨ��6GB 64GB��", "��ɫ": "��ҹ��"},
                                      {"skuId": 100002071796, "�汾": "ȫ��ͨ��6GB 128GB��", "��ɫ": "��ҹ��"},
                                      {"skuId": 100001550349, "�汾": "ȫ��ͨ��4GB 64GB��", "��ɫ": "������"},
                                      {"skuId": 100002071798, "�汾": "ȫ��ͨ��6GB 64GB��", "��ɫ": "������"},
                                      {"skuId": 100002071794, "�汾": "ȫ��ͨ��6GB 128GB��", "��ɫ": "������"},
                                      {"skuId": 100002071812, "�汾": "ȫ��ͨ��4GB 64GB��", "��ɫ": "�����"},
                                      {"skuId": 100001550347, "�汾": "ȫ��ͨ��6GB 64GB��", "��ɫ": "�����"},
                                      {"skuId": 100001550375, "�汾": "ȫ��ͨ��6GB 128GB��", "��ɫ": "�����"},
                                      {"skuId": 100002380994, "�汾": "ȫ��ͨ��4GB 64GB��", "��ɫ": "������"},
                                      {"skuId": 100002380984, "�汾": "ȫ��ͨ��6GB 64GB��", "��ɫ": "������"}],
                     "spec_param": ["��Ʒ���ƣ���Ϊ��ҫ10�ഺ��", "��Ʒ��ţ�100001550349", "��Ʒë�أ�162.00g", "��Ʒ���أ��й���½", "CPU�ͺţ�����",
                                    "�����ڴ棺4GB", "����洢��64GB", "�洢���������洢��", "����ͷ����������˫��", "�����������أ�1300������",
                                    "ǰ���������أ�2400������", "�����ص㣺����˫��", "����Ļ�ߴ磨Ӣ�磩��6.21Ӣ��", "�ֱ��ʣ�ȫ����FHD+", "��Ļ������������Ļ����",
                                    "��Ļǰ����ϣ�����", "���������mAh����3400mAh������ֵ��", "�������5V/2A", "������ɫ��������", "����ϵͳ��Android(��׿)",
                                    "��Ϸ���ܣ�����"], "thirdpart_flag": "��Ӫ",
                     "title": "��ҫ10�ഺ�� �òʽ��� 2400��AI���� ȫ��ͨ��4GB+64GB ������ �ƶ���ͨ����4Gȫ�����ֻ�"}, "msg": "ok", "status": 200},

        "requestInfo": {
            "uri": "�������ʼʹ�á���ť�ڹ���̨��ʹ��",
            "struct": "json",
            "method": "GET",
            "demo": "�������ʼʹ�á���ť�ڹ���̨��ʹ��",
            "data": [
                {"id": 1, "key": "product_id", "name": "��Ʒid", "type": "int", "comment": "��Ʒ�ھ���ƽ̨��Ψһ����"},
            ],
            "return": [
                {"id": 1, "key": "msg", "name": "��Ӧ��Ϣ", "type": "string", "comment": "ok����ɹ���������������д���"},
                {"id": 2, "key": "status", "name": "��Ӧ״̬", "type": "string", "comment": "200�����������أ�������������д���"},
                {"id": 2, "key": "data", "name": "��Ӧ����", "type": "object", "comment": '���ص����ݣ������ֶ������ֶ�˵����ǩ�鿴'},
            ],
        },
        "filedMean": [
            {"id": 1, "key": "brand_name", "name": "Ʒ������", "type": "string", "comment": "��Ʒ����Ʒ�Ƶ�����"},
            {"id": 2, "key": "cat_name_1", "name": "��һ�����", "type": "string", "comment": "��jdƽ̨�ϵĶ������"},
            {"id": 3, "key": "cat_name_2", "name": "�ڶ������", "type": "string", "comment": "jd��һ�������Ӽ�"},
            {"id": 4, "key": "cat_name_3", "name": "���������", "type": "string", "comment": "jd�������ĩ�����"},
            {"id": 5, "key": "img_urls", "name": "��Ʒͷͼ", "type": "list->string", "comment": "��Ʒͷͼ��С��"},
            {"id": 6, "key": "property_map", "name": "����sku", "type": "list->map",
             "comment": "ͬһspu�µ�sku����Ʒ��ͬ����map�µ��ֶβ�ͬ"},
            {"id": 7, "key": "spec_param", "name": "��Ʒ����", "type": "string", "comment": "��Ʒ�Ĳ���"},
            {"id": 8, "key": "thirdpart_flag", "name": "�Ƿ���Ӫ", "type": "string or null",
             "comment": "��Ӫ��Ʒ��ʾ����Ӫ��������null"},
            {"id": 9, "key": "title", "name": "��Ʒ����", "type": "string", "comment": "��Ʒ�ı���"},
        ],
    }


    base_info["pathBy"] = request.args.get("sort")
    base_info["useful"] = request.args.get("api")
    return jsonify(base_info)


@app.route("/table_api")
def get_table_apis():
    sort = request.args.get("sort")
    api = request.args.get("api")

    apis = {'����������Ϣ�ӿ�': 'jingdong/base', '���������۸�ӿ�': 'jingdong/price', '�����Ż���Ϣ�ӿ�': 'jingdong/prom', '����Ԥ����Ϣ�ӿ�': 'jingdong/yushou', '������Ʒ�����ʽӿ�': 'jingdong/comment',}


    result = []
    if api in apis: result.append({"label": api, "value": apis.pop(api)})
    for k, v in apis.items():result.append({"label": k, "value": v})
    return jsonify(result)


@app.route("/api_params")
def get_api_param():
    sort = request.args.get("sort")
    api = request.args.get("api")
    return jsonify({'product_id' : {"name": "��Ʒid", "value":""},})


@app.route("/api_data", methods=["GET", "POST"])
def get_api_data():
    data = json.loads(request.data)

    api_name = data.get("API")
    param = data.get("data")
    param["id"] = param.pop("product_id")

    result = json.loads(requests.get("http://127.0.0.1:8888/"+ api_name, params=param).text)

    filedMean = [
            {"id": 1, "key": "brand_name", "name": "Ʒ������", "type": "string", "comment": "��Ʒ����Ʒ�Ƶ�����"},
            {"id": 2, "key": "cat_name_1", "name": "��һ�����", "type": "string", "comment": "��jdƽ̨�ϵĶ������"},
            {"id": 3, "key": "cat_name_2", "name": "�ڶ������", "type": "string", "comment": "jd��һ�������Ӽ�"},
            {"id": 4, "key": "cat_name_3", "name": "���������", "type": "string", "comment": "jd�������ĩ�����"},
            {"id": 5, "key": "img_urls", "name": "��Ʒͷͼ", "type": "list->string", "comment": "��Ʒͷͼ��С��"},
            {"id": 6, "key": "property_map", "name": "����sku", "type": "list->map",
             "comment": "ͬһspu�µ�sku����Ʒ��ͬ����map�µ��ֶβ�ͬ"},
            {"id": 7, "key": "spec_param", "name": "��Ʒ����", "type": "string", "comment": "��Ʒ�Ĳ���"},
            {"id": 8, "key": "thirdpart_flag", "name": "�Ƿ���Ӫ", "type": "string or null",
             "comment": "��Ӫ��Ʒ��ʾ����Ӫ��������null"},
            {"id": 9, "key": "title", "name": "��Ʒ����", "type": "string", "comment": "��Ʒ�ı���"},
        ]

    result_info = {
        "jsonExample": result,
        "filedMean": filedMean,
    }

    return jsonify(result_info)





if __name__ == '__main__':
    app.run()


# value: 'jingdong/base',
# label: '����������Ϣ�ӿ�'��
# value: 'jingdong/price',
# label: '���������۸�ӿ�'��
# value: 'jingdong/prom',
# label: '�����Ż���Ϣ�ӿ�'��
#  value: 'jingdong/pingou',
# label: '����ƴ����Ϣ�ӿ�'��
#  value: 'jingdong/good',
#  label: '������Ʒ�����ʽӿ�'��


