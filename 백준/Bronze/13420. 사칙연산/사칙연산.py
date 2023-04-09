T = int(input())
for _ in range(T):
    prob, answer = map(str, input().split('='))
    
    if eval(prob) == int(answer):
        print("correct")
    else:
        print("wrong answer")