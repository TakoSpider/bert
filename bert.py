from flask import Flask, Response, request, jsonify
from flask.json import load
import requests
import json
from urllib import parse
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def bert(path):
    query = parse.parse_qs(parse.urlsplit(request.full_path).query)
    title = query["title"]
    url = "http://47.100.51.234:7009/encode"
    payload = "{\"id\": 1,\"texts\": [\"%s\"], \"is_tokenized\": false}" % title
    headers = {
        'content-type': 'application/json'
    }
    table = {
        'news_entertainment': '娱乐', 'news_sports': '体育', 'news_finance': '财经', 'news_house': '房产',
        'news_car': '汽车', 'news_edu': '教育', 'news_tech': '科技', 'news_military': '军事', 'news_game': '游戏', 'news_other': '其他'
    }
    response = requests.request(
        "POST", url, headers=headers, data=payload.encode('utf-8'))
    obj = json.loads(response.text)
    print(obj)
    label = obj["result"][0]["pred_label"][0]
    obj["result"][0]["pred_label"][0] = table[label]
    ret = json.dumps(obj, ensure_ascii=False)
    return Response(ret, mimetype='application/json')
    # return 'Hello, World!'

