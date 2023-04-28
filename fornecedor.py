import materiais

class fornecedor(materiais.materiais):
    def __init__(self, nome, valor):
        super().__init__(materiais.nome, materiais.preco, materiais.categoria)


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if nome == '':
            raise ValueError(' Nome Inválido ')
        self.__nome = nome.upper()


    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if valor == '':
            raise ValueError(' Valor Inválido ')
        self.__valor = valor.upper()
