import task_three, unittest


class Test_task_three(unittest.TestCase):

    def setUp(self):
        self.SEA = task_three.SimpleEncryptionAlgorithm("Hello~~~, my Amigo! It's a simple test for my algorithm")

    def test_type(self):
        self.assertEqual(type(self.SEA.generate_key()), str)
        
    
if __name__ == "__main__":
    unittest.main()