class inserir():

    codigo = 0
    nome = ''
    categoria = 0
    preco = 0
    quant = 0

    def inserir_peca(self):

        self.codigo = int(input("Digite o código da peça:"))
        self.nome = input("Digite o nome da peça:")
        self.categoria = int(input("Digite a categoria:"))
        self.preco = float(input("Digite o preço da peça:"))
        self.quant = int(input("Digite o total de peça no estoque:"))

        return (self.codigo, self.nome, self.categoria, self.preco, self.quant)

    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(self.codigo, self.nome, self. categoria, self.preco, self.quant)
