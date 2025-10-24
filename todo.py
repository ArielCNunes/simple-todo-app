import json

"""Simple TODO list application."""

class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.load_from_file()
    
    def add_todo(self, task):
        """Add a new todo item."""
        self.todos.append({'task': task, 'completed': False})
        self.save_to_file()
    
    def list_todos(self):
        """List all todos."""
        return self.todos

    def save_to_file(self):
        """Save todos to the file."""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=4)

    def load_from_file(self):
        """Load todos from the file."""
        try:
            with open(self.filename, 'r') as f:
                self.todos = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.todos = []

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_todo("Learn about Jules")
    print(todo_list.list_todos())
