"""
Repetitions
while (while loop)
Executes an action while a condition is true
Infinite loop -> When a code has no end
"""
counter = 0

while counter <= 100:
    counter += 1

    if counter == 6:
        print('I will not show 6.')
        continue

    if 10 <= counter <= 27:
        print('I will not show', counter)
        continue

    print(counter)

    if counter == 40:
        break

print('Finished')
