

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo um Objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Olá senhor {}, seu saldo é de R$:{}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, __valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return __valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} é maior que seu limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}





