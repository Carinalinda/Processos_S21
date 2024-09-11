from Bombacombustivel import BombaCombustivel

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
        