#Masudur Rahman(mr3rw)
#CS3240 HW#3
#test_graph.py

__author__ = 'masudurrahman'

import unittest
import my_adts

class TestGraphFunctions(unittest.TestCase):

    def setUp(self):
        a = ['Node2', 'Node3', 'Node4']
        b = ['Node1', 'Node4']
        c = ['Node1']
        d = ['Node1', 'Node2']
        example = {'Node1':list(a), 'Node2':list(b),'Node3':list(c), 'Node4':list(d)}
        self.myGraph = my_adts.Graph()
        self.myGraph.myDict.update(example)

    def test_init(self):
        a = ['Node2', 'Node3', 'Node4']
        b = ['Node1', 'Node4']
        c = ['Node1']
        d = ['Node1', 'Node2']
        example = {'Node1':list(a), 'Node2':list(b),'Node3':list(c), 'Node4':list(d)}
        self.myGraph = my_adts.Graph(example)
        self.assertEqual(self.myGraph.numnodes(), 4)

    def test_adjacent(self):
        self.assertTrue(self.myGraph.isadjacent('Node1', 'Node2'))
        self.assertFalse(self.myGraph.isadjacent('Node2', 'Node3'))

    def test_getlist(self):
        self.assertEqual(self.myGraph.getadjlist('Node3'), ['Node1'])
        self.assertEqual(self.myGraph.getadjlist('Node5'), None)

    def test_add(self):
        self.myGraph.addNode('Node5')
        self.assertEqual(self.myGraph.numnodes(), 5)
        self.assertFalse(self.myGraph.addNode('Node5'))

    def test_addEmpty(self):
        self.myGraph = my_adts.Graph()
        self.myGraph.addNode('Node1')
        self.assertEqual(self.myGraph.numnodes(), 1)

    def test_remove(self):
        self.myGraph.del_node('Node1')
        self.assertEqual(self.myGraph.numnodes(), 3)
        self.assertFalse(self.myGraph.del_node('Node1'))
        self.assertFalse(self.myGraph.__contains__('Node1'))
        self.assertEqual(self.myGraph.__len__(), 3)

    def test_removeEmpty(self):
        self.myGraph = my_adts.Graph()
        self.myGraph.del_node('Node1')
        self.assertEqual(self.myGraph.numnodes(), 0)

    def test_link(self):
        self.myGraph.link_nodes('Node2', 'Node3')
        self.assertEqual(len(self.myGraph.myDict['Node2']), 3)
        self.assertEqual(len(self.myGraph.myDict['Node3']), 2)
        self.assertFalse(self.myGraph.link_nodes('Node2', 'Node2'))
        self.assertFalse(self.myGraph.link_nodes('Node2', 'Node3'))
        self.assertFalse(self.myGraph.link_nodes('Node2', 'Node5'))
        self.assertFalse(self.myGraph.link_nodes('Node5', 'Node2'))

    def test_unlink(self):
        self.myGraph.unlink_nodes('Node1', 'Node2')
        self.assertEqual(len(self.myGraph.myDict['Node1']), 2)
        self.assertEqual(len(self.myGraph.myDict['Node2']), 1)
        self.assertFalse(self.myGraph.unlink_nodes('Node1', 'Node1'))
        self.assertFalse(self.myGraph.unlink_nodes('Node1', 'Node2'))
        self.assertFalse(self.myGraph.unlink_nodes('Node1', 'Node5'))
        self.assertFalse(self.myGraph.unlink_nodes('Node5', 'Node1'))

if __name__ == '__main__':
    unittest.main()