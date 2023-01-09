# 6 3
# 1 3 5 2 5 4
# 1 1 0 1 0 0


# wrong answer
n, k = [int(i) for i in input().split()]
te = [int(i) for i in input().split()]
we = [int(i) for i in input().split()]
r_st = 0
r_en = k-1
max_te = 0
ans = 0
for i in range(k):
    if not we[i]:
        max_te += te[i]
for i in range(k, n, 1):
    if we[i] == 0:
        if te[r_st] < te[i]:
            max_te = max_te - te[r_st] + te[i]
            r_st = i - k + 1
            r_en = i
for i in range(n):
    if i >= r_st and i <= r_en:
        ans += te[i]
    elif we[i]:
        ans += te[i]
print(ans)
