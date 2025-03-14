"""
Flag - Marking a location
None = No value
is and is not = is or is not (type, value, identity)
id = Identity
"""
condition = False
passed_if = None

if condition:
    passed_if = True
    print('Do something')
else:
    print('Do not do something')


if passed_if is None:
    print('Did not pass the if condition')
else:
    print('Passed the if condition')
