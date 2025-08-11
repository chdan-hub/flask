from flask import Flask, jsonify, request

app = Flask(__name__)


# GET
# 전체 게시물을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def get_all_feeds():
    data = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}
    return data

# 특정 게시물을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id) 
    return jsonify({'result':'success', 'data': {"feed1":"data"}})

# POST
# 게시물을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return jsonify({'result':'success'})