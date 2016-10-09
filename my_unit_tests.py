import unittest
from mpiaa.funcs import algorithm

class my_unit_tests(unittest.TestCase):


    def test_many(self):
        self.assertEqual(algorithm("../record_gen/records_1e3.txt"), [46,  '12'])

    def test_one(self):
        self.assertEqual(algorithm("../record_gen/records_1e1.txt"), [1, '15'])

    def test_empty(self):
        self.assertEqual(algorithm("../record_gen/records_1e0.txt"), "Exception: file empty")

if __name__ == "__main__":
    unittest.main()
