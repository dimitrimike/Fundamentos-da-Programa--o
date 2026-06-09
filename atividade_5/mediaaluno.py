def calcular_media (nota1: float, nota2: float, nota3: float) -> float:
    print("== Bem vindo ao Sistema do Colégio Byte! ==")
    for nota in [nota1, nota2, nota3]:
        if nota < 0 or nota > 10:
            return -1.0
    return round((nota1 * 2 + nota2 * 3 + nota3 * 5) / 10, 1)

media = calcular_media(7, 8, 9)
print(f"Média: {media}")

media2 = calcular_media(5, 6, 4)
print(f"Média: {media2}")

media3 = calcular_media(5, 11, 8)
print(f"Média: {media3}")


