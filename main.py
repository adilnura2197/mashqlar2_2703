#1
add = lambda a, b: a + b
print("1. Yig‘indi:", add(5, 3))

#2
square = lambda x: x * x
print("2. Kvadrat:", square(4))

#3
even_odd = lambda x: "Juft" if x % 2 == 0 else "Toq"
print("3. Natija:", even_odd(7))

#4
numbers = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x**2, numbers))
print("4. Kvadratlar:", squared_list)

#5
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("5. Juft sonlar:", even_numbers)
