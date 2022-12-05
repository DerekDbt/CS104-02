names = []
max = 10
for i in range(0, max):
    name = [input("Enter A Name: ")]
    names.append(name)  
  
print(names)

for i in range(max):
    print (names.pop(0))

print(names)
