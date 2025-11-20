import array
tester = array.array('i', [1,2,3,4,5])

#Find length of array
print("Length of arrya is ",len(tester))

#Accessing elements
print("Finding element at index 3: ", tester[3])

#Looping through array
print("Iterating/Looping through array")
for x in tester:
    print(x)

#Appending elements
tester.append(17)
print("Array after appending 17: ", tester)
print(tester)

#Inserting elements
tester.insert(2,25) 
print("Array after inserting 25 at index 2: ", tester)

#Removing elements
tester.remove(tester[1])
print("Array after removing index 1: ", tester)

#Popping elements
tester.pop(3)
print("Array after popping index 3: ", tester)

#Finding index of an element
index_of_4 = tester.index(3)
print("Index of element 3 is: ", index_of_4)

stringArray = array.array("u", ['a','b','c'])

stringArray.append('d')
print("Appending d: ", stringArray)

#tuple is made with parenthesis () immutable
#list is made with square brackets [] mutable
tuple =("apple",3,"cherry")
list = ["apple",3,"cherry"]
print(tuple)
print(list)

#This thorws an error because tuples are immutable

#tuple.append("banana")

list.append("banana")
print(list)

#Put 2 lists together
list2 = [7,8,9]
combined = list + list2
print("Combined lists: ", combined)

#Check for common items in lists
listA = [1,8,3,4,5]
listB = [4,5,6,7,8]
common = []

for item in listA:
    if item in listB:
        common.append(item)
print("Common items in listA and listB: ", common)

print(common)


#Lets do dictionsaries  
# Immutable key:value pairs
# Keys are immutable however, you can still update a value and add new key:value pairs using .update()

persons = {"name" : "John",
 "age" : 36, "country" : "Norway"}

print(persons)

#
#persons.clear()
#print("After clearing: ", persons)

temp = persons.get("country")
print(temp)

#finds all the keys in the dictionary
bool = persons.keys()
print(bool)

items = persons.items()
print(items)

#adding a new key:value pair 
persons.update({"email":"John01@yahoo.com"})
#updating an existing key:value pair
persons.update({"age": 37})
print("After adding email & updating age: ", persons)

#Another way to update age
persons["age"] = 38

#If the Key doesn't exsist to update, it will create a new ket:value pair
persons["phone"] = "555-1234"
print("After adding phone: ", persons)

print("The removed item is: ", persons.pop("country"))
print("After popping country: ", persons)

# del deletes the entire dictionary
#del persons

print("There are ",len(persons)," items in the dictionary")

for key in persons:
    print(key, ":", persons[key])

names = ["John", "Jane", "Doe"]

for x in names:
    print(x[len(x)-1])  # Prints last character of each name


    





