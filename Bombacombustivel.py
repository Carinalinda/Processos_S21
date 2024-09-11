class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel): # _int_Ela configura os val's da bomba, preço por litro quantidade disponível.
        self.valor_litro = valor_litro
        self.quantidade_disponivel = quantidade_disponivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_disponivel:
            self.quantidade_disponivel -= litros_abastecidos
            return litros_abastecidos
        else:
            return "Quantidade insuficiente na bomba."

    def abastecer_por_litro(self, litros):
        if litros <= self.quantidade_disponivel:
            self.quantidade_disponivel -= litros
            return litros * self.valor_litro
        else:
            return "Quantidade insuficiente na bomba."

        print(bomba.quantidade_disponivel) #Aqui tava o comando get, tentei alterar.


# Subclasse BombaEtanol
class BombaEtanol(BombaCombustivel):
    pass  # Não precisa de alterações, apenas herda da classe base

# Subclasse BombaGasolina
class BombaGasolina(BombaCombustivel):
    def abastecer_gasolina_com_aditivo(self, litros):
        if litros <= self.quantidade_disponivel:
            # Aqui, o valor do aditivo é imaginado como 10% mais caro
            valor_aditivo = litros * self.valor_litro * 1.10
            self.quantidade_disponivel -= litros
            return valor_aditivo
        else:
            return "Quantidade insuficiente na bomba."