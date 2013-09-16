#Masudur Rahman(mr3rw)
#CS3240 HW#3
#my_adts.py

__author__ = 'masudurrahman'

class Queue:
    'queue class for hw2 part 1'
    def __init__(self, *arg):
        if (arg is not None):
            Queue.myList = []
            for item in arg:
                Queue.myList.append(item)
        else :
            Queue.myList = []


    def add(self, item):
        Queue.myList.append(item)

    def remove(self):
        if (Queue.myList == []):
            return False
        if (Queue.myList is None):
            return False
        else:
            item = Queue.myList[0]
            del Queue.myList[0:1]
            return item

    def front(self):
        if (Queue.myList == []):
            return None
        if (Queue.myList is None):
            return None
        else:
            return Queue.myList[0]

    def __str__(self):
        return str(Queue.myList)

    def __len__(self):
        return len(Queue.myList)

    def __contains__(self, item):
        if(item in Queue.myList):
            return True
        else:
            return False

class Graph:
    'graph class for hw2 part 2'
    def __init__(self, *arg):
        if(arg is not None):
            Graph.myDict = dict()
            Graph.myDict.update(*arg)
        else:
            Graph.myDict = dict()

    def getadjlist(self, node):
        if (Graph.myDict.has_key(node)):
            return Graph.myDict[node]
        else:
            return None

    def isadjacent(self, node1, node2):
        if (Graph.myDict.has_key(node1)):
            if (node2 in Graph.myDict[node1]):
                return True
        else:
            return False

    def addNode(self, node):
        if(Graph.getadjlist(self, node) is None):
            Graph.myDict[node] = ""
            return True
        else:
            return False

    def link_nodes(self, node1, node2):
        if(node1 == node2):
            return False
        if(Graph.getadjlist(self, node1) is None):
            return False
        if(Graph.getadjlist(self, node2) is None):
            return False
        if(Graph.isadjacent(self, node1, node2)):
            return False
        else:
            Graph.myDict[node1].append(node2)
            Graph.myDict[node2].append(node1)
            return True

    def unlink_nodes(self, node1, node2):
        if(node1 == node2):
            return False
        if(Graph.getadjlist(self, node1) is None):
            return False
        if(Graph.getadjlist(self, node2) is None):
            return False
        if(not Graph.isadjacent(self, node1, node2)):
            return False
        else:
            Graph.myDict[node1].remove(node2)
            Graph.myDict[node2].remove(node1)
            return True

    def del_node(self, node):
        if(Graph.getadjlist(self, node) is None):
            return False
        else:
            for item in Graph.getadjlist(self, node):
                Graph.unlink_nodes(self, node, item)
            del Graph.myDict[node]
            return True

    def numnodes(self):
        return len(Graph.myDict.keys())

    def __str__(self):
        return list(Graph.myDict.items())

    def __iter__(self):
        return Graph.myDict.iterkeys()

    def __contains__(self, node):
        if (Graph.myDict.has_key(node)):
            return True
        else:
            return False

    def __len__(self):
        return len(Graph.myDict.keys())
