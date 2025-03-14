name = 'Name Lastname'
height = 1.80
weight = 95
bmi = weight / height ** 2  # BMI (Body Mass Index)

"f-strings"
line_1 = f'{name} is {height:.2f} meters tall,'
line_2 = f'weighs {weight} kilograms, and his BMI is'
line_3 = f'{bmi:.2f}'

print(line_1)
print(line_2)
print(line_3)

# Name Lastname is 1.80 meters tall,
# weighs 95 kilograms, and his BMI is
# 29.32
