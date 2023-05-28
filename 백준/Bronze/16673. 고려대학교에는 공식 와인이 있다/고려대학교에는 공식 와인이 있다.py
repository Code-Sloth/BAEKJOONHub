a,b,c = map(int, input().split())
answer = 0

for i in range(1, a + 1):    
    answer += b*i + c*(i**2)
    
print(answer)