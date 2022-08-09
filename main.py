x=int(input("1"))
y=int(input("2"))
z=int(input("3"))
if x<y or x<z or x<y and x<z:
    print("x")
elif y<x or y<z or y<x and y<z:
    print("y")
elif z<x or z<y or z<x and z<y:
    print("z")
