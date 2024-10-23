notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

mediafinal = (notaA + notaB) /2

if mediafinal >= 7.0:
    print("A média é %.1f - Aprovado"% mediafinal)
else:
    print("A média é %.1f - Reprovado"% mediafinal)