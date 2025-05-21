deposit = float(input())
months = int(input())
glp = float(input())/100

result = deposit + months * ((deposit * glp) / 12)

print(result)
