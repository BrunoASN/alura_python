class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self): #metodo não publico
        valor_diponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_diponivel_a_sacar

    def saca(self, valor):
        if (self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite.".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__saldo

    def get_limite(self):
        return self.__saldo

    def set_limite(self, limite):
        self.__limite = limite
