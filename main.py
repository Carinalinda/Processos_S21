from Bomba_etanol import BombaEtanol
from Bomba_gasolina import BombaGasolina

def main():
    # Criando as instâncias das bombas
    bomba_etanol = BombaEtanol(3.59, 1000)  # R$ 3,59 por litro e 1000 litros disponíveis
    bomba_gasolina = BombaGasolina(4.79, 1500)  # R$ 4,79 por litro e 1500 litros disponíveis

    # Pergunta ao cliente qual tipo de combustível deseja
    tipo_combustivel = input("Qual combustível você deseja? (etanol/gasolina/aditivada): ").lower()

    # Pergunta se deseja abastecer por valor ou por litro
    modo_abastecimento = input("Deseja abastecer por valor ou por litro? (valor/litro): ").lower()

    # Escolhe a bomba correta com base no tipo de combustível
    
    if tipo_combustivel == "etanol":
        bomba = bomba_etanol
    elif tipo_combustivel == "gasolina":
        bomba = bomba_gasolina
    elif tipo_combustivel == "aditivada":
        bomba = bomba_gasolina
    else:
        print("Opção de combustível inválida!")
        return

    # Processa o abastecimento com base no modo escolhido (valor ou litro)
    if modo_abastecimento == "valor":
        valor = float(input("Digite o valor que deseja abastecer: R$ "))
        if tipo_combustivel == "aditivada":
            print(f"Você abasteceu {bomba.abastecer_gasolina_com_aditivo(valor / bomba.valor_litro):.2f} litros de gasolina aditivada.")
        else:
            print(f"Você abasteceu {bomba.abastecer_por_valor(valor):.2f} litros.")
    elif modo_abastecimento == "litro":
        litros = float(input("Digite a quantidade de litros que deseja abastecer: "))
        if tipo_combustivel == "aditivada":
            print(f"Valor total com aditivo: R$ {bomba.abastecer_gasolina_com_aditivo(litros):.2f}.")
        else:
            print(f"Valor total: R$ {bomba.abastecer_por_litro(litros):.2f}.")
    else:
        print("Opção de abastecimento inválida!")

# Executa o main
if __name__ == "__main__":
    main()