a = "2 3"
b = a.split()
print(b[0])
print(b[1])
result = int(b[0]) + int(b[1])
print(result)

a = "2x3"
b = a.split('x')
print(b[0])
print(b[1])
result = int(b[0]) * int(b[1])
print(result)