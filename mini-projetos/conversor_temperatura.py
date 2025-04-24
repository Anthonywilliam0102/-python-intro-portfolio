def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Conversor de Temperatura")
escolha = input("Digite 'C' para converter para Celsius ou 'F' para converter para Fahrenheit: ").upper()

if escolha == "C":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"Temperatura em Celsius: {fahrenheit_para_celsius(f):.2f}°C")
elif escolha == "F":
    c = float(input("Digite a temperatura em Celsius: "))
    print(f"Temperatura em Fahrenheit: {celsius_para_fahrenheit(c):.2f}°F")
else:
    print("Opção inválida.")