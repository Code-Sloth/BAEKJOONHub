channel = int(input())
n = int(input())
broken = []

if n: broken = list(input().split())

# 상하 버튼으로만 이동 경우
sol = abs(100 - channel)

# 0 -> 500,000 / 1,000,000 -> 500,000 두 경우 생각
for nums in range(1000001):
    # nums의 숫자 하나하나를 꺼내서
    for i in str(nums):
        # 고장난 버튼이 하나라도 있으면 번호를 눌러 만들 수 없으니 멈춤
        if i in broken: break
    # 번호를 눌러 만들 수 있으면
    else:
        # 상하 버튼 이동 경우와 번호 + 상하 버튼 이동 횟수의 최솟값 저장
        sol = min(sol, len(str(nums)) + abs(nums - channel))

print(sol)