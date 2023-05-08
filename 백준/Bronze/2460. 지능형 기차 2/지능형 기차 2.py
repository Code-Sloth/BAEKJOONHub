p = 0
max_p = 0

for _ in range(10):
    out_train, in_train  = map(int, input().split()) 
    p += in_train - out_train 
    max_p = max(p, max_p) 
    
print(max_p)