def converter_moeda(valor, taxa):
    return valor * taxa

print("Conversor de Moedas")
print("1 - Real para Dólar")
print("2 - Real para Euro")
print("3 - Dólar para Real")
print("4 - Euro para Real")

opcao = input("Escolha uma opção (1-4): ")
valor = float(input("Digite o valor a ser convertido: "))


TAXA_DOLAR = 5.71   
TAXA_EURO = 6.47     
TAXA_REAL_DOLAR = 5.71  
TAXA_REAL_EURO = 6.47  

if opcao == "1":
    convertido = converter_moeda(valor, TAXA_DOLAR)
    print(f"R$ {valor:.2f} equivalem a US$ {convertido:.2f}")
elif opcao == "2":
    convertido = converter_moeda(valor, TAXA_EURO)
    print(f"R$ {valor:.2f} equivalem a € {convertido:.2f}")
elif opcao == "3":
    convertido = converter_moeda(valor, TAXA_REAL_DOLAR)
    print(f"US$ {valor:.2f} equivalem a R$ {convertido:.2f}")
elif opcao == "4":
    convertido = converter_moeda(valor, TAXA_REAL_EURO)
    print(f"€ {valor:.2f} equivalem a R$ {convertido:.2f}")
else:
    print("Opção inválida.")
