def feets_steps (steps) :
    steps_in_feet = 2.5
    steps_counted = steps / steps_in_feet
    return int(steps_counted)
feets_travelled = float(input("Please enter the distance travelled in feet: "))
walked_steps = feets_steps(feets_travelled)
print(f'Steps walked {walked_steps}')