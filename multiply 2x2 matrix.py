import sys
def main():
    a11=int(input("a11= "))
    a12=int(input("a12= "))
    a21=int(input("a21= "))
    a22=int(input("a22= "))

    b11=int(input("b11= "))
    b12=int(input("b12= "))
    b21=int(input("b21= "))
    b22=int(input("b22= "))

    A1=[
        [a11,a12],
        [a21,a22],
    ]
    A2=[
        [b11,b12],
        [b21,b22],
    ]
    Amult=[
        [a11*b11,a12*b12],
        [a21*b21,a22*b22],
    ]
    print(Amult)
    return 0
if __name__=="__main__":
    sys.exit(main())