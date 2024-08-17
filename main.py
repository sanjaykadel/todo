from flask import jsonify, request
from model import app
from views import get_todo_by_id, create_todo, get_all_todos, update_todo, delete_todo

@app.route('/todos', methods=['GET'])  # Sabai Todo list garne route
def get_todos():
    todos = get_all_todos()
    return jsonify([{
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'done': todo.done
    } for todo in todos])

@app.route('/todos/<int:id>', methods=['GET'])  # Get by ID ko route
def get_todo(id):
    todo = get_todo_by_id(id)
    if todo:
        return jsonify(todo)
    return jsonify({'message': 'Todo not found'}), 404

@app.route('/todos', methods=['POST'])  # Naya Todo create garne route
def add_todo():
    data = request.get_json()
    new_todo = create_todo(data['title'], data.get('description'), data.get('done'))
    return jsonify({
        'id': new_todo.id,
        'title': new_todo.title,
        'description': new_todo.description,
        'done': new_todo.done
    }), 201

@app.route('/todos/<int:id>', methods=['PUT'])  # Todo update garne route
def edit_todo(id):
    data = request.get_json()
    todo = update_todo(id, data['title'], data.get('description'), data['done'])
    if todo:
        return jsonify({
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'done': todo.done
        })
    return jsonify({'message': 'Todo not found'}), 404

@app.route('/todos/<int:id>', methods=['DELETE'])  # Todo delete garne route
def remove_todo(id):
    if delete_todo(id):
        return jsonify({'message': 'Todo deleted successfully'})
    return jsonify({'message': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)  # Flask app run garne
