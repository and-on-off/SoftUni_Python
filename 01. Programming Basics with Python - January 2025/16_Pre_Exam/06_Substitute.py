k = int(input())
l = int(input())
m = int(input())
n = int(input())

substitutions = 0

for num_1_1 in range(k, 9):
    if num_1_1 % 2 == 0:
        for num_1_2 in range(9, l - 1, -1):
            if num_1_2 % 2 != 0:
                for num_2_1 in range(m, 9):
                    if num_2_1 % 2 == 0:
                        for num_2_2 in range(9, n - 1, -1):
                            if num_2_2 % 2 != 0:
                                combo1 = f"{num_1_1}{num_1_2}"
                                combo2 = f"{num_2_1}{num_2_2}"
                                if combo1 == combo2:
                                    print("Cannot change the same player.")
                                else:
                                    print(f"{combo1} - {combo2}")
                                    substitutions += 1
                                if substitutions == 6:
                                    break
                        if substitutions == 6:
                            break
                if substitutions == 6:
                    break
        if substitutions == 6:
            break
