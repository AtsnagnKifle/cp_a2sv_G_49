for i in range(int(input())):
    n, cu = input().split()
    lig = input()
    n = int(n)
    ans = 0
    first_g = -1
    if cu == 'g':
        print(ans)
    else:
        stack = []
        for j in range(n):
            if lig[j] == cu:
                stack.append(j)
            elif lig[j] == 'g':
                if first_g == -1:
                    first_g = j
                while len(stack) > 0:
                    ans = max(ans, j-stack[-1])
                    stack.pop()
        while len(stack) > 0:
            ans = max(ans, n-stack[-1]+first_g)
            stack.pop()
        print(ans)
