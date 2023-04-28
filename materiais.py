class materiais:

    def __init__(self, nome, preco, categoria):
        self.__nome = nome
        self.__preco = preco
        self.__categoria = categoria


        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, nome):
            if nome == '':
                raise ValueError('Nome Inválido')
            self.__nome = nome.upper()


        @property
        def preco(self):
            return self.__preco

        @preco.setter
        def preco(self, preco):
            if preco == '':
                raise ValueError('Valor Inválido')
            self.__preco = preco.upper()

        @property
        def categoria(self):
            return self.__categoria

        @categoria.setter
        def categoria(self, categoria):
            if categoria == '':
                raise ValueError('Valor Inválido')
            self.__categoria = categoria.upper()
