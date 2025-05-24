number_one = int(input())
number_two = int(input())

print(f"Before:")
print(f"a = {number_one}")
print(f"b = {number_two}")

temp = number_one
number_one = number_two
number_two = temp

print(f"After:")
print(f"a = {number_one}")
print(f"b = {number_two}")
