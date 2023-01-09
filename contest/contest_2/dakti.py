for t in range(int(input())):
    words = input().split()
    n = len(words)
    d = {}
    for word in words:
        num = ""
        wo = ""
        for ch in word:
            if ch.isdigit():
                num += ch
            else:
                wo += ch
        d[int(num)] = wo

    for i in range(n):
        if i == n-1:
            print(d[i+1])
        else:
            print(d[i+1], end=" ")
