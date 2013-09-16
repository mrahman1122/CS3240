#Masudur Rahman(mr3rw)
#CS3240 HW#3
#test_queue.py

__author__ = 'masudurrahman'

import unittest
import my_adts

class TestQueueFunctions(unittest.TestCase):

    def setUp(self):
        self.myQueue = my_adts.Queue('c', 'b', 'a')

    def test_add(self):
        #Q2
        self.myQueue = my_adts.Queue('b', 'a')
        self.myQueue.add('d')
        self.assertEqual(self.myQueue.front(), 'b')

    def test_addEmpty(self):
        #Q6
        self.myQueue = my_adts.Queue()
        self.assertEqual(self.myQueue.front(), None)
        self.myQueue.add('a')
        current = ['a']
        self.assertEqual(len(self.myQueue), len(list(current)))

    def test_remove(self):
        #Q1
        self.assertEqual(self.myQueue.remove(), 'c')

    def test_removeEmpty(self):
        #Q5
        self.myQueue = my_adts.Queue()
        self.myQueue.remove()
        self.assertEqual(len(self.myQueue), 0)

    def test_init(self):
        #Q3
        self.myQueue = my_adts.Queue('c', 'b', 'a')
        self.assertEqual(self.myQueue.front(), 'c')

    def test_str(self):
        #Q4
        self.assertEqual(self.myQueue.__str__(), "['c', 'b', 'a']")

    def test_len(self):
        #Q7
        self.assertEqual(self.myQueue.__len__(), 3)

if __name__ == '__main__':
    unittest.main()