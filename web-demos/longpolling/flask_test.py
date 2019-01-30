from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.deug = True

VOTE_LIST = [
    {'name': '小明', 'count':3, 'id':1},
    {'name': '小红', 'count':5, 'id':2},
    {'name': '小花', 'count':6, 'id':3}
]

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_vote')
def get_vote():
    return jsonify(VOTE_LIST)

@app.route('/vote/')
def vote():
    nid = request.args.get('nid')
    for item in VOTE_LIST:
        if item['id'] == int(nid):
            item['count'] += 1
    return 'vote success'

if __name__ == '__main__':
    app.run(host='127.0.0.1')
