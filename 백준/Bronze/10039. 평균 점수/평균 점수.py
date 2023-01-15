t=0
for _ in range(5):
    s = int(input())
    if s < 40:
        s = 40
    t += s
print(t//5)