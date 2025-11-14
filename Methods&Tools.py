# ".strip" gets rid of empty space at the end of beginning 
string = "     Lets learn Python    "
print(string.strip())

# .upper()  .lower() either change all letters to upper or lower case
string = "PYTHON is fun"
print(string.upper())
print(string.lower())

# .split() is used to split up a string where it finds the "separator" and returns a list of string
# If you don't provide a separator it will split any white space(spaces)
string = "There should be three brown because I say brown three times brown"
words = string.split()
print(words)
checked = []

print("This is testing the Python .count method ", string.count("three"))

for word in words:
    if word.lower() not in checked:
        count = 0
        for target in words:
            if word.lower() == target.lower():
                count += 1
        print(word , " appeared ", count , " times")
        checked.append(word.lower())

# Learning Lists

numbers = [22,24,44,7,00,67,11]
print(numbers)

x = 2
print("Add",x)
numbers.append(x)
print(numbers)

print("Sort list")
numbers.sort()
print(numbers)

print("Reverse the List")
numbers.reverse()
print(numbers)

print("Remove even numbers")
# The [:] is a copy of numbers, so instead of iterating through the OG numbers list 
# that can cause problem since you are modifying it actively in the loop
for x in numbers[:]:
    if x % 2 == 0:
        numbers.remove(x)
print(numbers)




