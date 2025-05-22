number = input()
prime_sum = 0
none_prime_sum = 0

while number != 'stop':

    number = int(number)

    if number < 0:
        print('Number is negative.')
        number = input()
        continue


    if number == 1:
        none_prime_sum += number

    elif number > 1:

        for i in range(2, number):
            if number % i == 0:
                none_prime_sum += number
                break

        else:
            prime_sum += number

    number = input()


print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {none_prime_sum}")