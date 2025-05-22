goal = 10000
step_counter = 0
step_diff = 0

while step_counter < goal:
    steps = input()

    if steps == "Going home":
        going_home = input()
        step_counter += int(going_home)
        break

    step_counter += int(steps)

step_diff = abs(goal - step_counter)

if step_counter >= goal:
    print(f"Goal reached! Good job!")
    print(f"{int(step_diff)} steps over the goal!")
else:
    print(f"{int(step_diff)} more steps to reach goal.")
