"""
Ternary operation (single-line conditional)
<value> if <condition> else <other value>
"""
# condition = 10 == 11
# variable = 'Value' if condition else 'Other value'
# print(variable)

# digit = 9  # If > 9, set to 0
# new_digit = digit if digit <= 9 else 0
# new_digit = 0 if digit > 9 else digit
# print(new_digit)

print('Value' if False else 'Other value' if False else 'End')
