message = "Hello World\n"
print(message)

print("Numbers For Loop:\n")
for i in range(10):
    print(i)

print("\nList For Loop")
names = ["Ryan", "Michael","Laura","Megan"]
for name in names:
    print (name)

for index,name in enumerate(names):
    print(index,name)

person = "Alexander"
for letter in person:
    print(letter)

for i in range(20):
    if i%2 == 0:
        print (i)

for i in range(3):
    for x in range(2):
        print(i,x)

i = 10
while i > -1:
    print("Countdown: ", i)
    if i ==0:
        print("Boom!")
    i -= 1