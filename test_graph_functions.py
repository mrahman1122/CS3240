#Masudur Rahman(mr3rw)
#CS3240 HW#3
#test_graph_functions.py

__author__ = 'masudurrahman'

import unittest
import my_adts
import graph_functions

class TestGraphFunctions(unittest.TestCase):

    def setUp(self):
        a = ['Node2', 'Node3', 'Node4']
        b = ['Node1', 'Node4']
        c = ['Node1']
        d = ['Node1', 'Node2']
        example = {'Node1':list(a), 'Node2':list(b),'Node3':list(c), 'Node4':list(d)}
        self.myGraph = my_adts.Graph(example)

    def test_iscomplete1(self):
        self.assertFalse(graph_functions.is_complete(self.myGraph))
        self.myGraph.link_nodes('Node3', 'Node2')
        self.myGraph.link_nodes('Node3', 'Node4')
        self.assertTrue(graph_functions.is_complete(self.myGraph))

    def test_iscomplete2(self):
        self.myGraph = my_adts.Graph()
        self.assertTrue(graph_functions.is_complete(self.myGraph))
        self.myGraph.addNode('Node1')
        self.assertTrue(graph_functions.is_complete(self.myGraph))

    def test_iscomplete3(self):
        with self.assertRaises(TypeError):
            self.myGraph = my_adts.Queue()
            graph_functions.is_complete(self.myGraph)

    def test_bfs1(self):
        print (graph_functions.bfs_search(self.myGraph, 'Node4', 'Node1')).__str__()
        print (graph_functions.bfs_search(self.myGraph, 'Node4', 'Node4')).__str__()
        print (graph_functions.bfs_search(self.myGraph, 'Node4', 'Node2')).__str__()

if __name__ == '__main__':
    unittest.main()