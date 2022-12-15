class Student:
    maximum_average=0
    def __init__(self,n,m1,m2,m3):
        self.name=n
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
        avg=(m1+m2+m3)/3
        if Student.maximum_average<avg:
            Student.maximum_average=avg
    def __del__(self):
        print("Destructor of ",self.name," is called ")

def main():
    s1=Student("SuperChild",82,70,11)
    s2=Student("BatMan",83,84,81)
    s3=Student("AntMan",43,24,28)

    print("Maximum Average of Students is : ",Student.maximum_average)


main()