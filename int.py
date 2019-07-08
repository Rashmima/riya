g,d = map(int,input().split())
m = map(int,input().split())
li = list(m)
s = 0
for i in range(d):
  s += li[i]
print(s)
