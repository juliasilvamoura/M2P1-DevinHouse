from datetime import date
import uuid
# from veiculos import Veiculo
from classes import *
from exception import ErrorException

class HistoricoTransferencia:
    lista_vendas = []
    def historico(self, valor, cpf_comprador):
        self.id = uuid.uuid1().hex
        self.data = date.today().strftime("%d/%m/%y")
        self.valor = valor
        self.cpf_comprador = cpf_comprador
        self.veiculo = None
        print(self)
        
        
    # @classmethod
    def criarVeiculo(self, dataFabricacao, nome_modelo, placa, valor, cor ):
        self.veiculo = (Veiculo(dataFabricacao, nome_modelo, placa,valor,cor))
        # self.registar_venda()
        print("CRIOU VEICULO")
        
    # def registar_venda(self):
    #     lista = []
    #     self.__class__.lista_vendas.append(self)
    #     for x in self.__class__.lista_vendas:
    #         lista.append(vars(x))
    #         print(lista)
        

    # def modelar(self, lista_original):
    #     lista = []
    #     for x in lista_original:
    #         lista.append(vars(x))
    #     return lista

    # def listarHistorico(self):
    #     if self.__class__.lista_vendas != []:
    #         print("LISTA DE VENDAS")
    #         print(self.modelar(self.__class__.lista_vendas))
    #     else:
    #         raise ErrorException("ERRO! Não existem carros no sistema")



        