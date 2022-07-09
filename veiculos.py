from abc import ABC, abstractmethod
from exception import ErrorException
import uuid
from datetime import date
# biblioteca de formatação para imprimir
import pprint


#add a classe aqui por erro de import
class HistoricoTransferencia:
    lista_vendas = []
    def __init__(self):
        pass

    def historico(self, valor, cpf_comprador): 
        self.id =self.id = uuid.uuid4().hex
        self.data = date.today().strftime("%d/%m/%y")
        self.valor = valor
        self.cpf_comprador = cpf_comprador
        self.veiculo = None
        print(self)
        
    # CRIAR VEICULO USANDO COMPOSIÇÃO
    def criarVeiculo(self, dataFabricacao, nome_modelo, placa, valor, cor ):
        self.veiculo = vars(Veiculo(dataFabricacao, nome_modelo, placa,valor,cor))
        self.registar_venda()
        
    # ADD NA LISTA DE VENDAS
    def registar_venda(self):
        self.__class__.lista_vendas.append(self) 

    #IMPRIMIR
    def imprimir(self, lista_original):
        for x in lista_original:
            pprint.pprint(x)

    # MODELAR PARA IMPRIMIR BONITINHO
    def modelar(self, lista_original):
        lista = []
        for x in lista_original:
            lista.append(vars(x))
        return lista

    # LISTAR A LISTA DO HISTORICO DE VENDAS
    def listarHistorico(self):
        if self.__class__.lista_vendas != []:
            print("LISTA DE VENDAS".center(100,"-"))
            self.imprimir(self.modelar(self.__class__.lista_vendas))
            
        else:
            raise ErrorException("ERRO! Não existem veiculos no sistema")



class Veiculo:
    lista_veiculos = []
    def __init__(self, dataFabricacao, nome_modelo, placa, valor, cor) -> None:
        self.id = uuid.uuid4().hex
        self.chassi = uuid.uuid4().hex
        self.dataFabricacao = dataFabricacao
        self.nome_modelo = nome_modelo
        self.placa = placa
        self.valor = valor
        self.cpf_comprador = 0
        self.cor = cor
        self.tipo = "veiculo"
        self.__class__.lista_veiculos.append(self)

    #IMPRIMIR
    def imprimir(self, lista_original):
        for x in lista_original:
            pprint.pprint(x)
        
    # MODELAR E IMPRIMIR BONITINHO   
    def modelar(self, lista_original):
        lista = []
        for x in lista_original:
            lista.append(vars(x))
        return lista

    # TODAS AS CLASSES ABSTRATAS QUE SÓ SERVEM DE MODELO PARA SEREM CRIADAS PARA CLASSES FILHAS 

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
    
    # LISTA TODOS OS VEICULOS (MESMA FUNÇÃO PARA DEMAIS CLASSES)
    def listar(self):
        if self.__class__.lista_veiculos != []:
            print("LISTA DE VEICULOS".center(100,"-"))
            self.imprimir(self.modelar(self.__class__.lista_veiculos))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")

    # TODOS OS VEICULOS VENDIDOS (MESMA FUNÇÃO PARA DEMAIS CLASSES)
    def vendidos(self):
        vendidos = []
        print("VEICULOS VENDIDOS".center(100,"-"))
        vendidos = ([x for x in self.__class__.lista_veiculos if x.cpf_comprador != 0])
        if vendidos != []:
            self.imprimir(self.modelar(vendidos))
        else:
            raise ErrorException("ERRO! Não existem carros vendidos")

    # TODOS OS VEICULOS DISPONIVEIS (MESMA FUNÇÃO PARA DEMAIS CLASSES)
    def disponiveis(self):
        disponiveis = []
        print("VEICULOS DISPONIVEIS".center(100,"-"))
        disponiveis =([x for x in self.__class__.lista_veiculos if x.cpf_comprador == 0])
        if disponiveis != []:
            self.imprimir(self.modelar(disponiveis))
        else:
            raise ErrorException("ERRO! Não existem carros disponiveis")

    # TODOS OS VEICULOS VENDIDOS COM MENOR VALOR (MESMA FUNÇÃO PARA DEMAIS CLASSES)
    def vendidoMenorValor(self):
        lista_vendidos = []
        lista_vendidos = ([x for x in self.__class__.lista_veiculos if x.cpf_comprador != 0])
        if lista_vendidos != []:
            print("VEICULO VENDIDO COM MENOR VALOR".center(100,"-"))
            pprint.pprint(vars(min(lista_vendidos, key= lambda x: x.valor)))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")
    
    # TODOS OS VEICULOS VENDIDOS COM MAIOR VALOR (MESMA FUNÇÃO PARA DEMAIS CLASSES)
    def vendidoMaiorValor(self):
        lista_vendidos = []
        lista_vendidos = ([x for x in self.__class__.lista_veiculos if x.cpf_comprador != 0])

        if lista_vendidos != []:
            print("VEICULO VENDIDO COM MAIOR VALOR".center(100,"-"))
            pprint.pprint(vars(max(lista_vendidos, key= lambda x: x.valor)))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")

    # FUNÇÃO PARA CRIAR HISTORICO
    def realizarHistorico(self):
        # Unico jeito "Facil" que deu para instanciar a class historico e criar o historico
        h = HistoricoTransferencia()
        h.historico(self.valor, self.cpf_comprador)
        h.criarVeiculo(self.dataFabricacao, self.nome_modelo, self.placa, self.valor, self.cor )