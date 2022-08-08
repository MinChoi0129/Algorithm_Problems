from collections import deque;s,n,k=100000,*map(int,input().split());Q,d=deque([n]),[0]*(s+1)
while Q:
  x=Q.popleft()
  if x==k:print(d[x]);break
  for y in [x-1,x+1,2*x]:
    if 0<=y<=s and d[y]==0:d[y]=d[x]+1;Q.append(y)