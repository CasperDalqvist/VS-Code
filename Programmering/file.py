mil1 = int(input("Mäterställning idag? "))
mil2 = int(input("Mätarstlnning för ett år sen? "))
mil3 = int(mil1 - mil2)
print("Antal körda mil ", mil3)
liter = int(input("Hur många liter? "))
print(f"Liter per mil: {(liter/mil3):.4f}")