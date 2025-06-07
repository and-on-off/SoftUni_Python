numbers = input().split()
string = list(input())
index_sum = []
message = []

for index in numbers:
    index_summed = 0
    for num in str(index):
        index_summed += int(num)
    index_sum.append(index_summed)

for index in index_sum:
    if index > len(string) -1:
        index = index % (len(string) -1) -1
    message.append(string.pop(index))

print("".join(message))