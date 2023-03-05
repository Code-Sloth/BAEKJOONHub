b, c, d = map(int, input().split())

burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

result = 0
min_value = min(b, c, d)
for i in range(min_value) :
  result += (burger[i] + side[i] + drink[i]) * 0.9

result += sum(burger[min_value::])
result += sum(side[min_value::])
result += sum(drink[min_value::])

print(sum(burger) + sum(side) + sum(drink))
print(int(result))