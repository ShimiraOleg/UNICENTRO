class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade > self.estoque:
            print(f"Estoque insuficiente! Disponível: {self.estoque}\n")
        else:
            self.estoque -= quantidade
            print(f"{quantidade} unidade(s) de '{self.nome}' vendida(s)\n")

    def repor_estoque(self, quantidade):
        self.estoque += quantidade
        print(f"Estoque de '{self.nome}' reposto. Novo estoque: {self.estoque}\n")

    def exibir_informacoes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque}\n")

p = Produto("Teclado", 199.90, 10)
p.exibir_informacoes()
p.vender(3)
p.vender(20)
p.repor_estoque(5)
p.exibir_informacoes()