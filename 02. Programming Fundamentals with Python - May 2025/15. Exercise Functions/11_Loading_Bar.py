def loading_bar(percent: int) -> str:
    if percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    percent_loaded = percent // 10
    return f"{percent}% [{'%' * percent_loaded}{'.' * (10 - percent_loaded)}]\nStill loading..."

number = int(input())

print(loading_bar(number))