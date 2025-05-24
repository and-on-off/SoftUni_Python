# Variant 1
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


# Variant 2 - works for the given problem
a = int(input())
b = int(input())

print(f"Before:")
print(f"a = {a}")
print(f"b = {b}")
print(f"After:")
print(f"a = {b}")
print(f"b = {a}")