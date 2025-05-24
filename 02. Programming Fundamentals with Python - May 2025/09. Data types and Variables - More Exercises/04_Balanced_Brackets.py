lines = int(input())

opened_brackets = False
balanced = True

for line in range(lines):
    string = input()

    if string == "(":
        if opened_brackets:
            balanced = False
            break
        else:
            opened_brackets = True

    elif string == ")":
        if not opened_brackets:
            balanced = False
            break
        else:
            opened_brackets = False

print("BALANCED" if balanced else "UNBALANCED")