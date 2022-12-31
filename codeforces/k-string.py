k = int(input())
s = input()
s = sorted(s)
n = len(s)
s1 = ""
flag = True

if n%k:
    print(-1)
else:
    for i in range(0,n,k):
        # print("".join(s[i:i+k]))
        # print(s[i]*k)
        if "".join(s[i:i+k]) == s[i]*k:
            s1+=s[i]
        else:
            flag = False
            print(-1)
            break
    if flag:
        print(s1*k)
