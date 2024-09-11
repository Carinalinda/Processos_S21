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
            return "-1."

    def abastecer_por_litro(self, litros):
        if litros <= self.quantidade_disponivel:
            self.quantidade_disponivel -= litros
            return litros * self.valor_litro
        else:
            return "-1"
        