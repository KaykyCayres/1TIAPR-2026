vog = ["a", "e", "i", "o", "u"]
letra = input("Digite uma letra: ")
if letra.lower() in vog:
    print(f"A letra {letra} é vogal")
else:
    print(f"A letra {letra} é consoante")