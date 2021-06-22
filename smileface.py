# using print to draw a face hoping it was smiling

# can we have placeholder in placeholder
quote = "hello"
print("{0:2.2}\n".format(quote))

x = 2
y = 2
a = [1, 2, 3]
b = [1, 2, 3]

print("x is y: {}.".format(x is y))

# ^ means format print to the middle '<' left and '>' right
print("a is b: {:^10.3f}.".format(a is b))
print("float format print: {:.3f}".format(3.14159))


# format print for smiling face
p1 = True
p2 = True
spaceCnt = 9
spaces = ''
for i in range(spaceCnt):
    spaces += ' '
print(spaces + '.')
print("{0:>9}{1}".format('', p1 is p2) ,end = ' ')

str1 = "beautiful"
str2 = "beautiful"
print("{0:>8}{1}".format('', str1 is str2))
