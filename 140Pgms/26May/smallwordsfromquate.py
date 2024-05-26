quaote = "Give man a program, frustrate him for a day , teach man to program , frustrate him for life"
small = []
for i in quaote.split():
    if len(i)<3:
        small.append(i)

print(small)
