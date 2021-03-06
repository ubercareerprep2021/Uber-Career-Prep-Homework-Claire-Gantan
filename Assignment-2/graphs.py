import unittest, queue
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
                self.remove_edge(key, num.data)
            self.adj_nodes.remove(self.adj_nodes[indx])

    def add_edge(self, one, two):
        nodes = [n[0].data for n in self.adj_nodes]
        if one in nodes and two in nodes:
            self.adj_nodes[nodes.index(one)][1].append(self.adj_nodes[nodes.index(two)][0])
            self.adj_nodes[nodes.index(two)][1].append(self.adj_nodes[nodes.index(one)][0])

    def remove_edge(self, one, two):
        nodes = [n[0].data for n in self.adj_nodes]
        if one in nodes and two in nodes:
            one_node = self.adj_nodes[nodes.index(one)][0]
            two_node = self.adj_nodes[nodes.index(two)][0]
            self.adj_nodes[nodes.index(one)][1].remove(two_node)
            self.adj_nodes[nodes.index(two)][1].remove(one_node)

    def get_adj_nodes(self, key):
        nodes = [n[0].data for n in self.adj_nodes]
        if key in nodes:
            return [n.data for n in self.adj_nodes[nodes.index(key)][1]]

    # def dfs_helper(self, start_node):
    #     res = ""
    #     if start_node is not None:
    #         for n in start_node[1]:
    #             res = res +" "+ str(n.data)
    #             if self.get_adj_nodes(n.data) is not None:
    #                 for i in self.get_adj_nodes(n.data):
    #                     if str(i) not in res and i != start_node[0].data:
    #                         res = res +" "+ str(i)
        # return res

    def dfs(self, start_key):
        #originally used a recursive solution (part of it is above), but moved to an iterative one
        # nodes = [n[0].data for n in self.adj_nodes]
        # if start_key in nodes:
        #     start_node = self.adj_nodes[nodes.index(start_key)]
        #     res = str(start_node[0].data)
        #     for n in start_node[1]:
        #         if str(n.data)+" " not in res:
        #             res = res +" "+ str(n.data)
        #         if self.get_adj_nodes(n.data) is not None:
        #             for i in self.get_adj_nodes(n.data):
        #                 if str(i)+" " not in res:
        #                     res = res +" "+ str(i)
        #     return res
        # return ""
        #
        #FINAL solution: using a stack
        stack = []
        seen = []
        nodes = [n[0].data for n in self.adj_nodes]
        if start_key in nodes:
            res = ""
            start_node = self.adj_nodes[nodes.index(start_key)]
            stack.append(start_node[0].data)
            while len(stack) != 0:
                n = stack.pop()
                if n not in seen:
                    res = res + " " +str(n)
                    seen.append(n)
                for i in self.get_adj_nodes(n):
                    if i not in seen:
                        stack.append(i)
            return res[1:]
        return ""


    def bfs(self, start_key):
        q = queue.Queue()
        seen = []
        nodes = [n[0].data for n in self.adj_nodes]
        if start_key in nodes:
            res = ""
            start_node = self.adj_nodes[nodes.index(start_key)]
            q.put(start_node[0].data)
            while not q.empty():
                n = q.get()
                res = res + " " +str(n)
                seen.append(n)
                if self.get_adj_nodes(n) is not None:
                    for i in self.get_adj_nodes(n):
                        if i not in seen:
                            q.put(i)
                            seen.append(i)
            return res[1:]
        return ""

    def min_number_of_edges(self, one, two):
        seen = []
        return self.min_number_of_edges_helper(one, two, seen)

    def min_number_of_edges_helper(self, one, two, seen):
        nodes = [n[0].data for n in self.adj_nodes]
        if one not in nodes or two not in nodes:
            return -1 #assumed return -1 if no way to get from node1 to node2
        if one == two:
            return 0
        elif two in self.get_adj_nodes(one):
            return 1
        else:
            seen.append(one)
            possible = [self.min_number_of_edges_helper(n, two, seen) for n in self.get_adj_nodes(one) if n not in seen]
            if len(possible) == 0 or max(possible) == -1:
                return -1
            return 1 + min([i for i in possible if i > -1])



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
        self.assertEqual(three.get_adj_nodes(-1),[-3])
        self.assertEqual(three.get_adj_nodes(-3),[-1])

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
        self.assertEqual(three.get_adj_nodes(-1),[-3])
        self.assertEqual(three.get_adj_nodes(-3),[-1])
        three.remove_node(2)
        three.remove_node(-1)
        self.assertEqual(three.adj_nodes[0][0].data, -3)
        self.assertEqual(three.get_adj_nodes(-3),[])

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
        self.assertEqual(three.get_adj_nodes(-1),[-3,2])
        self.assertEqual(three.get_adj_nodes(2),[-1])
        self.assertEqual(three.get_adj_nodes(-3),[-1])
        three.remove_edge(-1, 2)
        self.assertEqual(three.get_adj_nodes(-1),[-3])
        self.assertEqual(three.get_adj_nodes(2),[])
        self.assertEqual(three.get_adj_nodes(-3),[-1])

    def test_get_adj_nodes(self):
        three = graph_with_adjacency_list([])
        three.add_node(-1)
        three.add_node(2)
        three.add_node(-3)
        self.assertEqual(three.adj_nodes[0][0].data, -1)
        self.assertEqual(three.adj_nodes[1][0].data, 2)
        self.assertEqual(three.adj_nodes[2][0].data, -3)
        self.assertEqual(three.get_adj_nodes(-1),[])
        self.assertEqual(three.get_adj_nodes(2),[])
        self.assertEqual(three.get_adj_nodes(-3),[])
        self.assertEqual(three.get_adj_nodes(4),None)
        three.add_edge(-1, -3)
        three.add_edge(-1, 2)
        self.assertEqual(three.get_adj_nodes(-1),[-3,2])
        self.assertEqual(three.get_adj_nodes(2),[-1])
        self.assertEqual(three.get_adj_nodes(-3),[-1])

    def test_empty_dfs_print(self):
        empty = graph_with_adjacency_list([])
        self.assertEqual(empty.dfs(1), "")

    def test_dfs_print(self):
        four = graph_with_adjacency_list([])
        four.add_node(1)
        four.add_node(-2)
        four.add_node(-300)
        four.add_node(4)
        self.assertEqual(four.get_adj_nodes(-300),[])
        four.add_edge(4,-300)
        four.add_edge(-300,1)
        four.add_edge(-300,-2)
        four.add_edge(-2, 4)
        four.remove_edge(-300,-2)
        self.assertEqual(four.get_adj_nodes(-300),[4,1])
        self.assertEqual(four.get_adj_nodes(1),[-300])
        self.assertEqual(four.get_adj_nodes(4),[-300,-2])
        self.assertEqual(four.get_adj_nodes(-2),[4])
        self.assertEqual(four.dfs(-300),"-300 1 4 -2")
        self.assertEqual(four.dfs(4),"4 -2 -300 1")

    def test_dfs_print_similar_nums(self):
        three = graph_with_adjacency_list([])
        three.add_node(-3)
        three.add_node(-30)
        three.add_node(-300)
        three.add_node(-3000)
        three.add_edge(-3, -30)
        three.add_edge(-30, -300)
        three.add_edge(-3, -3000)
        self.assertEqual(three.get_adj_nodes(-30),[-3, -300])
        self.assertEqual(three.dfs(-3),"-3 -3000 -30 -300")
        self.assertEqual(three.dfs(-30),"-30 -300 -3 -3000")
        self.assertEqual(three.dfs(-300),"-300 -30 -3 -3000")
        self.assertEqual(three.dfs(-3000),"-3000 -3 -30 -300")

    def test_bfs_print(self):
        four = graph_with_adjacency_list([])
        four.add_node(1)
        four.add_node(-2)
        four.add_node(-300)
        four.add_node(4)
        self.assertEqual(four.get_adj_nodes(-300),[])
        four.add_edge(4,-300)
        four.add_edge(-300,1)
        four.add_edge(-2, 4)
        self.assertEqual(four.get_adj_nodes(-300),[4,1])
        self.assertEqual(four.get_adj_nodes(1),[-300])
        self.assertEqual(four.get_adj_nodes(4),[-300,-2])
        self.assertEqual(four.get_adj_nodes(-2),[4])
        self.assertEqual(four.bfs(-300),"-300 4 1 -2")

    def test_min_edges(self):
        graph = graph_with_adjacency_list([])
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_node(6)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(0, 4)
        graph.add_edge(1,2)
        graph.add_edge(3, 4)
        graph.add_edge(4,5)
        graph.add_edge(4,6)
        graph.add_edge(2,5)
        self.assertEqual(graph.get_adj_nodes(0),[1,2,4])
        self.assertEqual(graph.get_adj_nodes(1),[0,2])
        self.assertEqual(graph.get_adj_nodes(2),[0,1,5])
        self.assertEqual(graph.get_adj_nodes(3),[4])
        self.assertEqual(graph.get_adj_nodes(4),[0,3,5,6])
        self.assertEqual(graph.get_adj_nodes(5),[4,2])
        self.assertEqual(graph.get_adj_nodes(6),[4])
        self.assertEqual(graph.min_number_of_edges(1,5), 2)
        self.assertEqual(graph.min_number_of_edges(6,1), 3)

    def test_min_edges_no_edges(self):
        graph = graph_with_adjacency_list([])
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        self.assertEqual(graph.min_number_of_edges(0,2), -1)

    def test_min_edges_line(self):
        graph = graph_with_adjacency_list([])
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(0,1)
        graph.add_edge(1,2)
        self.assertEqual(graph.min_number_of_edges(0,2), 2)

    def test_min_edges_cycle(self):
        graph = graph_with_adjacency_list([])
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(0,1)
        graph.add_edge(1,2)
        graph.add_edge(0,2)
        graph.add_edge(2,3)
        self.assertEqual(graph.min_number_of_edges(0,3), 2)

if __name__ == '__main__':
    unittest.main()

#TIMING:
#ex1: 57 min
#notes: do we assume nodes/data cannot be repeated???, at first I incorrecly assumed the list of adjacent nodes were just the keys instead of the actual nodes themselves
#ex4: 37 min (with basic test case)
