n_forces = int(input())

count = 0
x = 0
y = 0
z = 0

while count < n_forces:
    XYZ = input()
    XYZ = XYZ.split(" ")
    x += int(XYZ[0])
    y += int(XYZ[1])
    z += int(XYZ[2])
    count += 1

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
