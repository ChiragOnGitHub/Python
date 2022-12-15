file1=input("Enter the path of File 1")
file2=input("Enter the path of File 2")

try:
    f1=open(file1,"r")
    f2=open(file2,"w")
except:
    print("Error in opening file !!")
else:
    l=f1.readlines()
    for i in range (0,len(l),2):
        f2.write(l[i])
    print("Alternative lines are transferred successfully!!")