from collections import Counter, defaultdict
import random
from typing import List

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


def containsDuplicate( nums: List[int]) -> bool:
        for x in nums:
            if nums.count(x) >1:
                print(nums.count(x))
                return True
        return False
        
testList = [1,2,2,3,3,3]
print(containsDuplicate(testList))

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            sortedWord = "".join(sorted(word))
            result[sortedWord].append(word)

        return list(result.values())

# neetcode Find the most frequent elements in a list
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}
    for x in nums:
        counter[x] = 1 + counter.get(x,0)
        
    temp = []
    for key, value in counter.items():
        temp.append([value,key])
    temp.sort()
        
    result = []
    for i in range(k):
        result.append(temp.pop()[1])

    return result


testList = [1,2,2,3,3,3]
result = topKFrequent(testList,2)
print(result)

def encode(self, strs: List[str]) -> str:
    codedWord = ""
    for word in strs:
        codedWord = codedWord.join
    return codedWord


        
            

def decode(self, s: str) -> List[str]:

    return result


def productExceptSelf( nums: List[int]) -> List[int]:
        output = []
        for x in range(len(nums)):
            product = 1
            for y in range(len(nums)):
                if x != y:
                    product *= nums[y] 
            output.append(product)
        return output    

testList = [1,2,4,6]

print(productExceptSelf(testList))


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    
    counter = 0
    store = set(nums)
    for num in nums: 
        streak, number = 0 , num
        while number in store:
            streak += 1
            number += 1
        counter =  max(counter,streak)
    return counter

print(longestConsecutive([2,20,4,10,3,4,5]))

alphabet = ['q', 'm', 'a', 'z', 'b', 'x', 'c', 'v', 'w', 'k', 'y', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'n', 'o', 'p', 'r', 's', 't', 'u']


def sortAlphabet(alphabet : List[str]) -> List[str]:
    output = sorted(alphabet)
    return output

sortedAlphabet = sortAlphabet(alphabet)
for x in sortedAlphabet:
    print(x)


def countLetters(words : List[str]) -> List[int]:
    output = []

    for word in words:
        output.append(len(word))
    return output

words = ["apple", "banana", "cherry", "date", "elderberry"]

print(countLetters(words))

def threeSum(nums: List[int]) ->  List[List[int]]:
        output=[]
        seen = set()
        for x in range(len(nums)):
            for y in range(len(nums)):
                if y != x:
                    for z in range(len(nums)):
                        if z != y and z != x:
                            product = nums[x] + nums[y] + nums[z]
                            #print(f"Adding index {x} from nums which is {nums[x]},index {y} from nums which is {nums[y]},index {z} from nums which is {nums[z]}")
                            if product == 0:
                                triplet = tuple(sorted([nums[x], nums[y], nums[z]]))
                                if triplet not in seen:
                                    seen.add(triplet)
                                    output.append(list(triplet))
                                

        return output

listNums = [-1,0,1,2,-1,-4]
print(threeSum(listNums))

def maxArea (heights: List[int]) -> int:
    maxWater = 0
    left = 0
    right = len(heights) -1

    while(left<right):
        product = min(heights[left] , heights[right]) * (right -1 )
        maxWater = max(maxWater, product)
        if left < right:
            left +=1
        else:
            right -= 1
    return maxWater

def maxProfit(prices: List[int]) -> int:
    maxProfit = 0
    minNumIndex = prices.index(min(prices))
    for num in range(minNumIndex,len(prices)):
        product = prices[num] -prices[minNumIndex] 
        maxProfit = max(maxProfit, product)
    return maxProfit


prices = [10,1,5,6,7,1]
print(maxProfit(prices))


def binarySearch(nums: List[x], target:int):
    low = 0
    high = len(list) - 1
    
    while high > low:
        med = (list[high] - list[low]) - 1

        if nums[med] == target:
            return med
        if nums[med] > target:
            high = med - 1
        else:
            low = med + 1

    return -1

    
print(listNums)
listNums.reverse()
print(listNums)


#self & skills

#Tell me about a time you were asked to give contructive feedback to a coworker


tempString = "I am going to create this string to test" \
"out how the Counter collection works!"

c = Counter(tempString)
#print(c)
print("Most common outputs this: " ,c.most_common(2))

def searchInsert(nums: List[int], target: int) -> int:
        nums.append(target)
        nums = sorted(nums)
        print("SOrted LIst " , nums)

        for x in range(len(nums)):
            print("x is: " ,x)
            if nums[x] == target:
                return x
        

nums = [-1,0,2,4,6,8] 
target = 10
print(f"Index of {target} would be at: " ,searchInsert(nums,target))