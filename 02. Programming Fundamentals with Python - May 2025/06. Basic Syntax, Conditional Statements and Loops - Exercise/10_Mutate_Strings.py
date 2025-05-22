string1, string2 = input(), input()

for char in range(len(string1)):
    if string1[char] != string2[char]:
        string1 = string2[:char + 1] + string1[char + 1:]
        print(string1)




# string1 = input()
# string2 = input()
#
# for char in range(len(string1)):
#     if string1[char] != string2[char]:
#         string1 = string2[:char + 1] + string1[char + 1:]
#         print(string1)
