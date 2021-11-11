class Solution():

    def __init__(self):
        self.result = 0
        self.n = 4
    def func(self,current_number):
        if current_number == self.n:
            self.result += 1

        if current_number + 1 <= self.n:
            self.func(current_number + 1)
        if current_number + 2 <= self.n:
            self.func(current_number + 2)

c = Solution()
c.func(0)

print(c.result)