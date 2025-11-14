import random

name = "Jonathan"
age = 23

introduction =f"My name is {name} and I am {age}"
print(introduction)

def addSum(x,y):
    return x+y


numbers= [4,8,67,45,66,80,2,7,48,58,28,23]
def findMin(num):
    return min(num)

print("Minimum number: " ,findMin(numbers))

def findMax(num):
    return max(num)

print("Maximum number: ",findMax(numbers))

def findEvenOrOdd(num):
    if num == 0:
        print("The numer 0 is neither even or odd")
    if num % 2 == 0:
        print("This is a Even number",num)
    if num%2 ==1:
        print("This is a odd number",num)

findEvenOrOdd(-5)

def canAfford(balance,cost):
    if cost > balance:
        print("You can not afford this")
    else:
        print("You can afford it")

canAfford(1000,100)

def collect_apples(turns,steve_apples,tommy_apples):
    while turns != 0:
        steve_apples = steve_apples + random.randint(1,10)
        tommy_apples = tommy_apples + random.randint(1,10)
        turns -= 1
    print(f"Steve has {steve_apples} apples")
    print(f"Tommy has {tommy_apples} apples")

collect_apples(1,0,0)

def fibonacciSequence(count):
    a, b = 0,1
    sequence = []
    for _ in range(count):
        sequence.append(a)
        a,b = b,a+b
    return sequence

print(fibonacciSequence(10))
total = sum(fibonacciSequence(10))
print("The sum of the fibonacci sequence is" , total)

def stringPalidromeCheck(string):
    if string == string[::-1]:
        return True
    else:
        return False

testWord = "rabbit"
print(f"{testWord} is a palidrome =",stringPalidromeCheck(testWord))

def listPalidromeCheck(list):
    for word in list:
        if word == word[::-1]:
            print(word," is a palidrome")
        else:
            print(word," is not a palidrome")

testList = ["rabbit","tacocat","racecar","animal"]

listPalidromeCheck(testList)

original = 1, 2, 3, 4, 5
copy = tuple(original)
print(original)
print(copy)
