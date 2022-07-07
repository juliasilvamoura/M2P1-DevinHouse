from datetime import date
# from Veiculo import Veiculo
from exception import ErrorException

class HistoricoTransferencia:
    lista_vendas = []
    def chegar(self, veiculo):
        print(veiculo)
        # self.veiculo = (Veiculo(veiculo))
        # print(self.veiculo)

    def venda(self, veiculo, cpf_comprador):
        self.veiculo = veiculo
        self.cpf_comprador = cpf_comprador
        # self.valor= dadosvenda.valor
        self.data = date.today().strftime("%d/%m/%y")
        self.__class__.lista_vendas.append(self)

    def modelar(self, lista_original):
        lista = []
        for x in lista_original:
            lista.append(vars(x))
        return lista

    def listarHistorico(self):
        if self.__class__.lista_vendas != []:
            print("LISTA DE CARROS")
            print(self.modelar(self.__class__.lista_vendas ))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")



        