num1 = int(input())
num2 = int(input())

for number in range(num1, num2 + 1):

    odd_sum = 0
    even_sum = 0
    number = str(number)

    for i in range(len(number)):
        num = int(number[i])

        if i % 2 == 0:
            even_sum += num

        else:
            odd_sum += num

    if odd_sum == even_sum:
        print(number, end=' ')