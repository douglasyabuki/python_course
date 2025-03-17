a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={name2} a={name1} a={name1} c={name3:.2f}'
formatted = string.format(
    name1=a, name2=b, name3=c
)

print(formatted)
