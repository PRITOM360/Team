n = int(input())
total = 0
for i in range(n):
    x = input()
    if x.count("1") >= 2:
        total += 1
    else:
        pass
print(total)

