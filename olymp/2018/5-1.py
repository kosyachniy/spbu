n = int(input())
m = [list(map(int, input().split())) for i in range(n)]

q = lambda x, y: ((3, 2), (4, 1))[x>0][y>0] #(1 if y > 0 else 4) if x > 0 else (2 if y > 0 else 3)
print(q(*m[0]))