

class HashMap():

    def __init__(self, values):

        self.size = len(values)
        self.map = [None] * self.size
        self.values = values
        self.populate()

    def get_key_hash(self, key):
        return key % self.size

    def add(self, key, index):
        key_hash = self.get_key_hash(key)
        key_value = [key, index]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            self.map[key_hash].append(key_value)
            return True
    
    def populate(self):
        for i, e in enumerate(self.values):
            self.add(e, i)
        return True

    def get(self, key_hash, key):
        if self.map[key_hash] is not None:
            for e in self.map[key_hash]:
                if e[0] == key:
                    return e[1]
        return False

    
    def solution(self, target):
        for e,i  in enumerate(self.values):
            if target - i >= 0:
                key = self.get_key_hash(target - i)
                result = self.get(key, target - i)
                if result is not False:
                    print([e, result])


nums = [2, 7, 11, 15]
target = 9

classe = HashMap(nums)
classe.solution(target)
