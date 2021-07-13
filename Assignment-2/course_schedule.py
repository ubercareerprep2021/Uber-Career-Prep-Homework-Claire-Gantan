import unittest, queue
class graph_node:
    def __init__(self, data):
        self.data = data

class directed_graph:
    def __init__(self, adj_nodes):
        self.adj_nodes = adj_nodes
    def add_node(self, key):
        self.adj_nodes.append([graph_node(key),[]])
    def remove_node(self,key):
        nodes = [n[0].data for n in self.adj_nodes]
        if key in nodes:
            indx = nodes.index(key)
            for num in self.adj_nodes[indx][1]:
                self.remove_edge(key, num.data)
            self.adj_nodes.remove(self.adj_nodes[indx])

    def add_edge(self, one, two):
        nodes = [n[0].data for n in self.adj_nodes]
        if one in nodes and two in nodes:
            self.adj_nodes[nodes.index(one)][1].append(self.adj_nodes[nodes.index(two)][0])

    def remove_edge(self, one, two):
        nodes = [n[0].data for n in self.adj_nodes]
        if one in nodes and two in nodes:
            two_node = self.adj_nodes[nodes.index(two)][0]
            self.adj_nodes[nodes.index(one)][1].remove(two_node)

    def get_adj_nodes(self, key):
        nodes = [n[0].data for n in self.adj_nodes]
        if key in nodes:
            return [n.data for n in self.adj_nodes[nodes.index(key)][1]]

    def has_cycle(self):
        seen = []
        nodes = [n[0].data for n in self.adj_nodes]
        return self.has_cycle_helper(seen, nodes[0])

    def has_cycle_helper(self, seen, start):
        if start in seen:
            return True
        seen.append(start)
        possible = [self.has_cycle_helper(seen,i) for i in self.get_adj_nodes(start)]
        if len(possible) == 0 or True not in possible:
            return False
        return True

def course_schedule(num_courses, prereq):
    nodes = []
    graph = directed_graph([])
    for arr in prereq:
        if arr[0] not in nodes:
            graph.add_node(arr[0])
        if arr[1] not in nodes:
            graph.add_node(arr[1])
        graph.add_edge(arr[0], arr[1])
    if graph.has_cycle():
        return False
    return True


class UnitTests(unittest.TestCase):
    def test_has_cycle_false(self):
        one = directed_graph([])
        one.add_node(1)
        one.add_node(0)
        one.add_edge(0,1)
        self.assertEqual(one.get_adj_nodes(0),[1])
        self.assertEqual(one.get_adj_nodes(1),[])
        self.assertFalse(one.has_cycle())

    def test_has_cycle_true(self):
        one = directed_graph([])
        one.add_node(1)
        one.add_node(0)
        one.add_edge(0,1)
        one.add_edge(1,0)
        self.assertEqual(one.get_adj_nodes(0),[1])
        self.assertEqual(one.get_adj_nodes(1),[0])
        self.assertTrue(one.has_cycle())

    def test_course_schedule(self):
        self.assertTrue(course_schedule(2,[[1,0]]))
        self.assertFalse(course_schedule(2,[[1,0],[0,1]]))

if __name__ == '__main__':
    unittest.main()

#Timing: ex5: 23 min (with basic test cases)
