import unittest
import os
import json
from todo import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.filename = "test_todos.json"
        # Ensure the file doesn't exist before each test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def tearDown(self):
        # Clean up the file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_add_and_list_todos(self):
        todo_list = TodoList(self.filename)
        self.assertEqual(todo_list.list_todos(), [])
        todo_list.add_todo("Test task 1")
        self.assertEqual(len(todo_list.list_todos()), 1)
        self.assertEqual(todo_list.list_todos()[0]['task'], "Test task 1")

    def test_save_and_load_from_file(self):
        todo_list = TodoList(self.filename)
        todo_list.add_todo("Test task 1")
        todo_list.add_todo("Test task 2")

        # Create a new instance to load from the file
        new_todo_list = TodoList(self.filename)
        self.assertEqual(len(new_todo_list.list_todos()), 2)
        self.assertEqual(new_todo_list.list_todos()[0]['task'], "Test task 1")

    def test_load_from_non_existent_file(self):
        todo_list = TodoList("non_existent_file.json")
        self.assertEqual(todo_list.list_todos(), [])

    def test_load_from_invalid_json_file(self):
        with open(self.filename, 'w') as f:
            f.write("invalid json")

        todo_list = TodoList(self.filename)
        self.assertEqual(todo_list.list_todos(), [])

    def test_auto_save_on_add(self):
        todo_list = TodoList(self.filename)
        todo_list.add_todo("Auto-save test")

        with open(self.filename, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['task'], "Auto-save test")

if __name__ == '__main__':
    unittest.main()
