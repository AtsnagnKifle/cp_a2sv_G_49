n = input()
li = [int(i) for i in input().split()]
mi = li[0]
ma = li[0]
co = 0
for num in li:
    if num < mi:
        co += 1
        mi = num
    elif num > ma:
        co += 1
        ma = num
print(co)
