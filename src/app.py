from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [{"label": "My first task", "done": False},
         {"label": "My second task", "done": False}]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return  jsonify(todos), 201

@app.route('/todos<int:position>', methods=['DELETE'])
def delete_todos(position):
    todos.pop(position)
    print('this is the position delete:',position)
    return  jsonify(todos), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)