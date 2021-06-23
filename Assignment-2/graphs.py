import unittest
class graph_node:
    def __init__(self, data):
        self.data = data

class graph_with_adjacency_list:
    def __init__(self, adj_nodes):
        self.adj_nodes = adj_nodes
    def add_node(self, key):
        self.adj_nodes.append([graph_node(key),[]])
    def remove_node(self,key):
        ##first draft: need to add changes for when there are edges to the node we are trying to remove
        # for n in self.adj_nodes:
        #     if n[0].data == key:
        #         self.adj_nodes.remove(n)

        ##second draft: before creating the remove_edge function
        # temp = None
        # for n in self.adj_nodes:
        #     if key in n[1]:
        #         self.adj_nodes[self.adj_nodes.index(n)][1].remove(key)
        #     if n[0].data == key:
        #         temp = n
        # if temp is not None:
        #     self.adj_nodes.remove(temp)

        ##third attempt below, using the remove_edge function
        nodes = [n[0].data for n in self.adj_nodes]
        if key in nodes:
            indx = nodes.index(key)
            for num in self.adj_nodes[indx][1]:
                self.remove_edge(key, num)
            self.adj_nodes.remove(self.adj_nodes[indx])

    def add_edge(self, one, two):
        nodes = [n[0].data for n in self.adj_nodes]
        if one in nodes and two in nodes:
            self.adj_nodes[nodes.index(one)][1].append(two)
            self.adj_nodes[nodes.index(two)][1].append(one)

    def remove_edge(self, one, two):
        nodes = [n[0].data for n in self.adj_nodes]
        if one in nodes and two in nodes:
            self.adj_nodes[nodes.index(one)][1].remove(two)
            self.adj_nodes[nodes.index(two)][1].remove(one)

    def get_adj_nodes(self, key):
        nodes = [n[0].data for n in self.adj_nodes]
        if key in nodes:
            return self.adj_nodes[nodes.index(key)][1]


class UnitTests(unittest.TestCase):
    def test_add_one_node(self):
        one = graph_with_adjacency_list([])
        one.add_node(4)
        self.assertEqual(one.adj_nodes[0][0].data, 4)

    def test_add_neg_nodes(self):
        three = graph_with_adjacency_list([])
        three.add_node(-1)
        three.add_node(2)
        three.add_node(-3)
        self.assertEqual(three.adj_nodes[0][0].data, -1)
        self.assertEqual(three.adj_nodes[1][0].data, 2)
        self.assertEqual(three.adj_nodes[2][0].data, -3)

    def test_remove_one_node(self):
        three = graph_with_adjacency_list([])
        three.add_node(-1)
        three.add_node(2)
        three.add_node(-3)
        self.assertEqual(three.adj_nodes[0][0].data, -1)
        self.assertEqual(three.adj_nodes[1][0].data, 2)
        self.assertEqual(three.adj_nodes[2][0].data, -3)
        three.remove_node(2)
        self.assertEqual(three.adj_nodes[0][0].data, -1)
        self.assertEqual(three.adj_nodes[1][0].data, -3)

    def test_remove_not_found(self):
        one = graph_with_adjacency_list([])
        one.add_node(4)
        self.assertEqual(one.adj_nodes[0][0].data, 4)
        one.remove_node(3)
        self.assertEqual(one.adj_nodes[0][0].data, 4)

    def test_add_one_edge(self):
        three = graph_with_adjacency_list([])
        three.add_node(-1)
        three.add_node(2)
        three.add_node(-3)
        self.assertEqual(three.adj_nodes[0][0].data, -1)
        self.assertEqual(three.adj_nodes[1][0].data, 2)
        self.assertEqual(three.adj_nodes[2][0].data, -3)
        three.add_edge(-1, -3)
        self.assertEqual(three.adj_nodes[0][1],[-3])
        self.assertEqual(three.adj_nodes[2][1],[-1])

    def test_add_edge_not_found(self):
        one = graph_with_adjacency_list([])
        one.add_node(4)
        self.assertEqual(one.adj_nodes[0][0].data, 4)
        one.add_edge(4,3)
        self.assertEqual(one.adj_nodes[0][1], [])

    def test_add_edge_remove_node(self):
        three = graph_with_adjacency_list([])
        three.add_node(-1)
        three.add_node(2)
        three.add_node(-3)
        self.assertEqual(three.adj_nodes[0][0].data, -1)
        self.assertEqual(three.adj_nodes[1][0].data, 2)
        self.assertEqual(three.adj_nodes[2][0].data, -3)
        three.add_edge(-1, -3)
        self.assertEqual(three.adj_nodes[0][1],[-3])
        self.assertEqual(three.adj_nodes[2][1],[-1])
        three.remove_node(2)
        three.remove_node(-1)
        self.assertEqual(three.adj_nodes[0][0].data, -3)
        self.assertEqual(three.adj_nodes[0][1],[])

    def test_remove_one_edge(self):
        three = graph_with_adjacency_list([])
        three.add_node(-1)
        three.add_node(2)
        three.add_node(-3)
        self.assertEqual(three.adj_nodes[0][0].data, -1)
        self.assertEqual(three.adj_nodes[1][0].data, 2)
        self.assertEqual(three.adj_nodes[2][0].data, -3)
        three.add_edge(-1, -3)
        three.add_edge(-1, 2)
        self.assertEqual(three.adj_nodes[0][1],[-3,2])
        self.assertEqual(three.adj_nodes[1][1],[-1])
        self.assertEqual(three.adj_nodes[2][1],[-1])
        three.remove_edge(-1, 2)
        self.assertEqual(three.adj_nodes[0][1],[-3])
        self.assertEqual(three.adj_nodes[1][1],[])
        self.assertEqual(three.adj_nodes[2][1],[-1])

    def test_get_adj_nodes(self):
        three = graph_with_adjacency_list([])
        three.add_node(-1)
        three.add_node(2)
        three.add_node(-3)
        self.assertEqual(three.adj_nodes[0][0].data, -1)
        self.assertEqual(three.adj_nodes[1][0].data, 2)
        self.assertEqual(three.adj_nodes[2][0].data, -3)
        three.add_edge(-1, -3)
        three.add_edge(-1, 2)
        self.assertEqual(three.get_adj_nodes(-1),[-3,2])
        self.assertEqual(three.get_adj_nodes(2),[-1])
        self.assertEqual(three.get_adj_nodes(-3),[-1])
        three.remove_edge(-1, 2)
        self.assertEqual(three.get_adj_nodes(-1),[-3])
        self.assertEqual(three.get_adj_nodes(2),[])
        self.assertEqual(three.get_adj_nodes(-3),[-1])

if __name__ == '__main__':
    unittest.main()

#TIMING:
#ex1: 57 min
#notes: do we assume nodes/data can be repeated???
