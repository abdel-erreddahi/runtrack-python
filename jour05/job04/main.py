def tapis(n: int) -> None:
    cloture = "+" + "-" * n + "+"
    print(f"{cloture}")
    for k in range(n):
        interieur = "#" * (n-k-1) + " " + "#" * k
        print(f"|{interieur}|")
    print(f"{cloture}")

tapis(10)