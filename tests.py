import unittest
from data_capture import DataCapture, BadFormat


class TestDataCapture(unittest.TestCase):
    data_capture = DataCapture()

    def test_add(self):
        self.assertEqual(self.data_capture.add(10), 10)
        with self.assertRaises(NotImplementedError):
            self.data_capture.greater(8)
        with self.assertRaises(NotImplementedError):
            self.data_capture.less(8)
        with self.assertRaises(NotImplementedError):
            self.data_capture.between(1,10)
        with self.assertRaises(ValueError):
            self.data_capture.add(1001)

    def test_build_stats(self):
        
        self.data_capture.add(10)
        self.data_capture.add(1)
        self.data_capture.add(2)
        self.data_capture.add(52)
        self.data_capture.add(9)
        self.data_capture.add(15)
        self.assertEqual(self.data_capture.build_stats(), [1,2,9,10,10,15,52]) # sorted list

    def test_greater(self):

        with self.assertRaises(BadFormat):
            self.data_capture.greater(99)
        with self.assertRaises(TypeError):
            self.data_capture.add(99)
        self.assertEqual(self.data_capture.greater(10), {15,52})

    def test_less(self):

        with self.assertRaises(BadFormat):
            self.data_capture.less(99)
        self.assertEqual(self.data_capture.less(10), {1,2,9})




if __name__ == '__main__':
    unittest.main()
