from model import db, Todo

def get_todo_by_id(id):
    todo = Todo.query.get(id)  # ID bata Todo fetch garne
    if todo:
        return {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'done': todo.done
        }
    return None

def create_todo(title, description,done):
    new_todo = Todo(title=title, description=description,done=done)  # Naya Todo create garne
    db.session.add(new_todo)
    db.session.commit()
    return new_todo

def get_all_todos():
    return Todo.query.all()  # Sabai Todo list garne

def update_todo(id, title, description, done):
    todo = Todo.query.get(id)
    if todo:
        todo.title = title
        todo.description = description
        todo.done = done
        db.session.commit()
        return todo
    return None

def delete_todo(id):
    todo = Todo.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return True
    return False
