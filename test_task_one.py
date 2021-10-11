import task_one, unittest


class Test_task_one(unittest.TestCase):

    def test_type(self):
        self.assertEqual(type(task_one.count_letters('Hello')), dict)
        
    def test_result(self):
        self.assertEqual(task_one.count_letters("Hello"), {"H": 1, "e": 1, "l": 2, "o": 1})


if __name__ == "__main__":
    unittest.main()