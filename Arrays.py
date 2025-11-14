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


#Lets do dictionsaries now immutable key:value pairs

persons = {"name" : "John",
 "age" : 36, "country" : "Norway"}

print(persons)

#
#persons.clear()
#print("After clearing: ", persons)

copyPersons = persons.fromkeys("name", "44")
print("Copy of persons: ", copyPersons)