def hist(l):
    import matplotlib.pyplot as plt
    plt.hist(l)
    plt.title("Histogram")
    plt.show()

def main():
    l=[]
    n=int(input("Enter number of Values you want to enter : "))
    print("Please Enter Numbers : ")
    for i in range (n):
        a=int(input())
        l.append(a)
    hist(l)

main()
