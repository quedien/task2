import unittest

class TaskManager:
    def __init__(self):
        self.tasks = []

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            return True
        return False


class TestTaskManager(unittest.TestCase):

    def test_toggle_undone(self):
        tm = TaskManager()
        tm.tasks.append({"text": "Задача", "done": False})

        result = tm.toggle_task(0)

        self.assertTrue(result)
        self.assertEqual(tm.tasks[0]["done"], True)

    def test_toggle_done(self):
        tm = TaskManager()
        tm.tasks.append({"text": "Задача", "done": True})

        result = tm.toggle_task(0)

        self.assertTrue(result)
        self.assertEqual(tm.tasks[0]["done"], False)

    def test_toggle_invalid_index(self):
        tm = TaskManager()

        result = tm.toggle_task(5)

        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()