Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())

if (Xa*Yb + Xb*Yc +Xc*Ya - Xb*Ya - Xc*Yb - Xa*Yc) == 0:
    print(-1)
else:
    l1 = 2 * ((( (Xc-Xa) ** 2 + (Yc-Ya) ** 2 ) ** 0.5) + (( (Xb-Xa) ** 2 + (Yb-Ya) ** 2 ) ** 0.5))
    l2 = 2 * ((( (Xc-Xb) ** 2 + (Yc-Yb) ** 2 ) ** 0.5) + (( (Xb-Xa) ** 2 + (Yb-Ya) ** 2 ) ** 0.5))
    l3 = 2 * ((( (Xc-Xa) ** 2 + (Yc-Ya) ** 2 ) ** 0.5) + (( (Xc-Xb) ** 2 + (Yc-Yb) ** 2 ) ** 0.5))
    print(max(l1, l2, l3) - min(l1, l2, l3))