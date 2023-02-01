import sys

n, m = map(int,input().split())
nums = sorted(list(map(int,input().split())), reverse = True)

m_n = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sol = nums[i] + nums[j] + nums[k]
            if sol <= m:
                if m_n < sol: m_n = sol
                break
print(m_n)