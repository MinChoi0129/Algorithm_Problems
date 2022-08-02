Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())

# 한 직선위에 있다 -> 3C2 cases의 기울기가 같다. -> 나눗셈 없애도록 ab=cd
# 기울기 발산 고려.