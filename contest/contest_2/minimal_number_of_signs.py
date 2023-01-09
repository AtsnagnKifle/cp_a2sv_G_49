patt = []
for t in range(int(input())):
    patt.append(input())
n = len(patt[0])
ans = ""
for i in range(n):
    ch = patt[0][i]
    flag = True
    for pa in patt:
        if ch == "?" and pa[i] != "?":
            ch = pa[i]
        if ch != pa[i] and pa[i] != "?":
            ans += "?"
            flag = False
            break
    if flag:
        if ch == "?":
            ans += "a"
        else:
            ans += ch
print(ans)
