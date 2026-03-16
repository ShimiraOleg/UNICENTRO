class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def tipo_habilitacao(self):
        return "Habilitação necessária."

class Carro(Veiculo):
    def tipo_habilitacao(self):
        return "Categoria B — veículo de passeio."

class Moto(Veiculo):
    def tipo_habilitacao(self):
        return "Categoria A — motocicleta."

veiculos = [
    Carro("Toyota", "Corolla"),
    Moto("Honda", "CB 500"),
]
for v in veiculos:
    print(f"{v.marca} {v.modelo}: {v.tipo_habilitacao()}\n")