#Masudur Rahman(mr3rw)
#CS3240 HW#3
#graph_functions.py

__author__ = 'masudurrahman'

import my_adts

#graph functions

def is_complete(grph):
    if(not isinstance(grph, my_adts.Graph)):
        raise TypeError('This is not a graph type. Please enter a graph object instead.')
    else:
        if((grph.numnodes() == 1) or (grph.numnodes() == 0)):
            return True
        for item in grph.myDict.keys():
            if(not (len(grph.myDict[item]) == grph.numnodes()-1)):
                return False
        return True


def bfs_search(grph, start, target):
    if(not isinstance(grph, my_adts.Graph)):
        raise TypeError('This is not a graph type. Please enter a graph object instead.')
    else:
        path = my_adts.Queue()
        path.add(start)
        visit = my_adts.Queue()
        visit.add(start)

        if((grph.numnodes() == 1) or (grph.numnodes() == 0)):
            return False
        if(start == target):
            return path

        while(path.__len__() < grph.numnodes()):
            currentNode = visit.remove()
            for node in grph.getadjlist(currentNode):
                if (path.__contains__(node)):
                    continue
                else:
                    path.add(node)
                    if (node == target):
                        return path

                    for item in grph.getadjlist(node):
                        if(not(visit.__contains__(item))):
                            visit.add(item)
