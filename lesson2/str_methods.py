fruit = "Apple and Banana"
print(fruit.lower())
print(fruit.upper())
print(fruit.capitalize())
print(fruit.title())
print(fruit.endswith("a"))
print(fruit.startswith("A"))

word = '        Hello World       ' 
print(word)
print(word.strip())

fruits = "banan apple cherry pineapple"
print(fruits.split())

print('-' * 50)
file_name = "numeric.py"
base_name = file_name.split('.')[0]
extension = file_name.split('.')[1]
print(f"{file_name}")
print(f"{base_name}")
print(f"{extension}")
