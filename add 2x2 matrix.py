import sys
def main():
    a11= float(input("a11: "))
    a12 = float(input("a12: "))
    a21 = float(input("a21: "))
    a22 = float(input("a22: "))

    b11 = float(input(("b11: ")))
    b12 = float(input(("b12: ")))
    b21 = float(input(("b21: ")))
    b22 = float(input(("b22: ")))

    A1=[
        [a11,a12],
        [a21,a22],
    ]
    A2=[
        [b11,b12],
        [b21,b22],
    ]
    Asum=[
        [a11+b11,a12+b12],
        [a21+b21,a22+b22],
    ]
    print(f"A={Asum}")
    print(f"a11={Asum[0][0]}")
    print(f"a12={Asum[0][1]}")
    print(f"a21={Asum[1][0]}")
    print(f"a22={Asum[1][1]}")
    return 0
if __name__=="__main__":
    sys.exit(main())
