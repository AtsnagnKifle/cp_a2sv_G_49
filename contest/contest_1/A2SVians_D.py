from collections import defaultdict
n = int(input())
mems = input().split()
bad = input().split()
ans = 0


def check(name):
    d = defaultdict(int)
    for ch in name:
        d[ch] += 1

    co = d[name[0]]
    for key in d:
        if d[key] != co:
            return False
    return True


for mem in mems:
    if check(mem):
        # if not mem in bad:
        #     ans += 1
        flag = True
        for badm in bad:
            if mem == badm:
                flag = False
                break
        if flag:
            ans += 1
print(ans)
