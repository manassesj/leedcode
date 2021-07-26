
class Node():
    def __init__(self, value):
        self.value = value
        self.prev = None

class Pile():
    
    def __init__(self):
        self.last = None

    def solution(self, input):
        i = 0

        while i < len(input):
            node = Node(input[i])
            if self.last is None:
                self.last = node
            else:
                self.helper(input[i], node)
            
            i += 1
        
        if self.last is None:
            return True
        else:
            return False
    def helper(self, value, node):
        if value == ")" and self.last.value == "(":
            self.set_last()     
        elif value == "]" and self.last.value == "[":
            self.set_last()
        elif value == "}" and self.last.value == "{":
            self.set_last()
        else:
            node.prev = self.last
            self.last = node

    def set_last(self):
            if self.last.prev is None:
                self.last = None
            else:
                self.last = self.last.prev

            
                
i = "()[]{}"

model  = Pile()
print(model.solution(i))