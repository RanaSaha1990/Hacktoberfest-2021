import time
def middle_white(n):
    ar = []
    for i in range(1, n + 1):
        ar.append(i)
    # print(ar)
    ar.reverse()
    # print(ar)
    for i in ar:
        for j in range(1, i + 1):
            print("\t", end=" ")

        for k in range(1, n - (i - 2)):
            if k == 1:
                print("*\t\t", end=" ")
            elif k == n - (i - 1):
                print("*\t\t", end=" ")
            else:
                print(" \t\t", end=" ")
        print("\n")
    br = []
    for i in range(1, n):
        br.append(i)
    # print(br)
    for i in br:
        for j in range(1, i + 1):
            print("\t", end=" ")
            # print("*")

        for k in range(1, n - (i - 1)):
            if k == 1:
                print("\t *\t ", end=" ")
            elif k == n - i:
                print("\t *\t ", end=" ")
            else:
                print("\t  \t ", end=" ")
        print("\n")


print(time.asctime(time.localtime()))
a = int(input("Enter the number of rows: "))
middle_white(a)
