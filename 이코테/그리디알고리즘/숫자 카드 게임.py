n, m = map(int, input().split())
result = 0

for i in range(n):
     data = list(map(int, input().split()))
     minData = min(data)
     
     result = max(result, minData)

print(result)