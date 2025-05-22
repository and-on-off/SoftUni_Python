from math import floor

processors_needed = int(input())
employees = int(input())
working_days = int(input())

hours = employees * working_days * 8
processors_made = floor(hours / 3)
processors_diff = abs(processors_needed - processors_made)

if processors_made < processors_needed:
    processors_diff = processors_needed - processors_made
    print(f"Losses: -> {processors_diff * 110.1:.2f} BGN")
else:
    print(f"Profit: -> {processors_diff * 110.1:.2f} BGN")