n = 2

class teste():
    
    def __init__(self):
        self.ord = 0

    def solution(self,n, current_n):
        if current_n == n:
            self.ord += 1
        
        if current_n + 1 <= n:
            self.solution(n, current_n + 1)
            
        if current_n + 2 <= n:
            self.solution(n, current_n + 2)



t = teste()

if n < 2:
    t.solution(n, 1)
else:
    t.solution(n, 1)
    t.solution(n, 2)
print(t.ord)