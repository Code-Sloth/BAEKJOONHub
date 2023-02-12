n = int(input())

def hanoi(n,st,end,mid):
    if n == 1: 
        print(st,end)
        return
    hanoi(n-1,st,mid,end)
    print(st,end)
    hanoi(n-1,mid,end,st)

print(2**n-1)
hanoi(n,1,3,2)