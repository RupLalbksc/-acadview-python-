file1 = open("file.txt","w")
file1.write("this is file handling \n")
a = ["welcome \n","to the LPU \n","you r in LPU"]
file1.writelines(a)
file1.close()

file1 = open("file.txt","r+")
print(file1.read())
file1.close()

with open("file.txt") as f:
    with open("copy.txt","w") as f1:
        for line in f:
            f1.write(line)
        f1.write("\n copying")
f1.close()
f.close()

f1 = open("copy.txt","r")
print(f1.read())
f1.close()

with open("file.txt") as f:
    with open("copy.txt") as f1:
        with open("added.txt","w") as f2:
            x = f.readlines()
            y = f1.readlines()
            for line1, line2 in zip(y, x):
                f2.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))
f2.close()
f2 = open("added.txt","r")
print(f2.read())




