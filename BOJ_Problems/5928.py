from datetime import datetime
d, h, m = map(int, input().split())
gap = int((datetime(2011, 11, d, h, m) - datetime(2011, 11, 11, 11, 11)).total_seconds() // 60)
print(-1 if gap < 0 else gap)