import unittest

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, text):
        if text.strip():
            self.tasks.append({"text": text.strip(), "done": False})
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def get_count(self):
        return len(self.tasks)

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            return True
        return False

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()

    def test_add_task(self):
        result = self.tm.add_task("Купить молоко")
        self.assertTrue(result)
        self.assertEqual(self.tm.get_count(), 1)

    def test_add_empty_task(self):
        result = self.tm.add_task("")
        self.assertFalse(result)
        self.assertEqual(self.tm.get_count(), 0)

    def test_delete_task(self):
        self.tm.add_task("Задача")
        result = self.tm.delete_task(0)
        self.assertTrue(result)
        self.assertEqual(self.tm.get_count(), 0)

    def test_toggle_undone_task(self):
        self.tm.add_task("Задача")
        result = self.tm.toggle_task(0)
        self.assertTrue(result)
        self.assertTrue(self.tm.tasks[0]["done"])

    def test_toggle_done_task(self):
        self.tm.add_task("Задача")
        self.tm.toggle_task(0)
        result = self.tm.toggle_task(0)
        self.assertTrue(result)
        self.assertFalse(self.tm.tasks[0]["done"])

    def test_toggle_invalid_index(self):
        result = self.tm.toggle_task(0)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()