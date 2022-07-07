from abc import ABC, abstractmethod
# from exception import ErrorException
# from historicoTransferencias import HistoricoTransferencia
import uuid

from classes import *


class Veiculo:
    lista_veiculos = []
    def __init__(self, dataFabricacao, nome_modelo, placa, valor, cor) -> None:
        self.id = uuid.uuid1().hex
        self.chassi = uuid.uuid4().hex
        self.dataFabricacao = dataFabricacao
        self.nome_modelo = nome_modelo
        self.placa = placa
        self.valor = valor
        self.cpf_comprador = 0
        self.cor = cor
        self.__class__.lista_veiculos.append(self)
        
        
    def modelar(self, lista_original):
        lista = []
        for x in lista_original:
            lista.append(vars(x))
        return lista

    @abstractmethod
    def alterarCor(self,indice, nova_cor):
        pass

    @abstractmethod
    def alterarValor(self,indice, novo_valor):
        pass

    @abstractmethod
    def vender(self,indice,cpf_comprador):
        pass

    @abstractmethod
    def venderVeiculos(self):
        pass

    @abstractmethod
    def listarInformacoes(self):
        pass
    
    @abstractmethod
    def alterarInformacoes(self, info_alterar, novo_valor):
        pass
    
    
    def listar(self):
        if self.__class__.lista_veiculos != []:
            print("LISTA DE VEICULOS")
            print(self.modelar(self.__class__.lista_veiculos))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")


    def vendidos(self):
        vendidos = []
        print("VEICULOS VENDIDOS")
        vendidos = ([x for x in self.__class__.lista_veiculos if x.cpf_comprador != 0])
        if vendidos != []:
            print(self.modelar(vendidos))
        else:
            raise ErrorException("ERRO! Não existem carros vendidos")


    def disponiveis(self):
        disponiveis = []
        print("VEICULOS DISPONIVEIS")
        disponiveis =([x for x in self.__class__.lista_veiculos if x.cpf_comprador == 0])
        if disponiveis != []:
            print(self.modelar(disponiveis))
        else:
            raise ErrorException("ERRO! Não existem carros disponiveis")


    def vendidoMenorValor(self):
        lista_vendidos = []
        lista_vendidos = ([x for x in self.__class__.lista_veiculos if x.cpf_comprador != 0])
        if lista_vendidos != []:
            print("VEICULO VENDIDO COM MENOR VALOR")
            print(vars(min(lista_vendidos, key= lambda x: x.valor)))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")
    
   
    def vendidoMaiorValor(self):
        lista_vendidos = []
        lista_vendidos = ([x for x in self.__class__.lista_veiculos if x.cpf_comprador != 0])

        if lista_vendidos != []:
            print("VEICULO VENDIDO COM MAIOR VALOR")
            print(vars(max(lista_vendidos, key= lambda x: x.valor)))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")


    def realizarHistorico(self):
        HistoricoTransferencia.historico(self,self.valor, self.cpf_comprador)
        HistoricoTransferencia.criarVeiculo(self.dataFabricacao, self.nome_modelo, self.placa, self.valor, self.cor )
        print("DEU CERTO")
        # print(cpf_comprador)
    