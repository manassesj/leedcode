class Node():
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.left_son = None
        self.right_son = None

class Tree():
    def __init__(self, values):
        self.raiz = None
        self.build_tree(values)
    
    def insert_node(self, value, index):

        current_node = self.raiz
        new_node = Node(value, index)
        while True:
            if value > current_node.value:
                if current_node.right_son == None:
                    current_node.right_son = new_node
                    break
                else:
                    current_node = current_node.right_son
            else:
                if current_node.left_son == None:
                    current_node.left_son = new_node
                    break
                else:
                    current_node = current_node.left_son

    def build_tree(self, values):
        n = len(values) // 2
        if self.raiz == None:
            self.raiz = Node(values[n], n)
        
        for i, j in enumerate(values):
            if i != n:
                self.insert_node( j, i)
    
    def solution(self, target):
        


Tree([2,7,11,15])