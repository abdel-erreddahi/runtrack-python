def triangle(n: int) -> None:
    for k in range(n - 1):
        space = "/" + "  " * k + "\\"
        print(f"{space: ^{n*2}}")
    space = "_" * (n-1) * 2
    print(f"/{space}\\")

n = int(input("Entrer un entier strictement positif: "))
triangle(n)