n = int(input())

arr = list(map(int, input().split()))
arr.sort()

res = 0
for i in range(len(arr)):
    res += sum(arr[:i+1])

print(res)