from Veiculo import Veiculo
from exception import ErrorException
from datetime import datetime, date
import uuid

class Caminhonete(Veiculo):
    lista_caminhonetes = []
    def __init__(self, dataFabricacao, nome_modelo, placa, valor, total_portas, capacidade_cacamba, tipo_combustivel, potencia, cor = "roxa"):
        super().__init__(dataFabricacao, nome_modelo, placa, valor, cor)
        self.total_portas = total_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.capacidade_cacamba = capacidade_cacamba
        

        if(dataFabricacao and nome_modelo and placa and valor and cor and total_portas and potencia and tipo_combustivel and capacidade_cacamba):
            if(tipo_combustivel.lower() == 'gasolina' or tipo_combustivel.lower() == 'diesel'):
                if(cor.lower() == "roxa"):
                    try:
                        self.dataFabricacao = datetime.strptime(dataFabricacao, '%d/%m/%Y').date() 
                        self.__class__.lista_caminhonetes.append(self)
                    except Exception as erro:
                        print(f"Erro! Data em formato errado | {erro}")
                else:
                    raise ErrorException("Caminhonetes DEVinCar são ROXAS")
            else:
                raise ErrorException("O Combustivel só pode ser GASOLINA ou DIESEL")
        else:
            raise ErrorException("Preencha todos os Campos corretamente")


   # modelo a lista para ele não imprimir em formato de código e sim como obj
    def modelar(self, lista_original):
        lista = []
        for x in lista_original:
            lista.append(vars(x))
        return lista

    #  LISTANDO INFORMAÇÕES DO CARRO
    # listo a informação de um veiculo especifico
    def listarInformacoes(self):
        print(vars(self))

    #  ALTERANDO INFORMAÇÕES 
    # altero a informação de um veiculo especifico
    def alterarInformacoes(self, info_alterar, novo_valor):
        if(info_alterar == 1):
            self.cor = novo_valor
            print("Alterado com sucesso")
        elif(info_alterar == 2):
            self.valor = novo_valor
            print("Alterado com sucesso")

    # VENDER CAMINHONETE
    # add o cpf no veiculo vendido e chamo a função realizar Histórico
    def venderVeiculos(self, cpf_comprador):
        self.cpf_comprador = cpf_comprador
        Veiculo.realizarHistorico(self, cpf_comprador)

    
     # RELATÓRIO CAMINHONETES
     # LISTAR CAMINHONETE
    def listar(self):
        if self.__class__.lista_caminhonetes!= []:
            print("LISTA DE CAMINHONETE")
            print(self.modelar(self.__class__.lista_caminhonetes))
        else:
            raise ErrorException("ERRO! Não existem caminhonetes no sistema")

    # RELATÓRIO CAMINHONETES VENDIDOS
    # compara qual tem cpf != 0 e retorna uma lista de objetos
    def vendidos(self):
        vendidos = []
        print("CAMINHONETE VENDIDOS")
        vendidos = ([x for x in self.__class__.lista_caminhonetes if x.cpf_comprador != 0])
        if vendidos != []:
            print(self.modelar(vendidos))
        else:
            raise ErrorException("ERRO! Não existem caminhonetes vendidos")

    # RELATÓRIO CAMINHONETES DISPONIVEIS
    # compara qual tem cpf = 0 e retorna uma lista de objetos
    def disponiveis(self):
        disponiveis = []
        print("CAMINHONETEs DISPONIVEIS")
        disponiveis =([x for x in self.__class__.lista_caminhonetes if x.cpf_comprador == 0])
        if disponiveis != []:
            print(self.modelar(disponiveis))
        else:
            raise ErrorException("ERRO! Não existem caminhonetes disponiveis")

    # RELATÓRIO CAMINHONETE MENOR VALOR DE VENDA
    # cria uma lista de veiculo vendido e depois usa a função min para comparar os valores e retornar o objeto de menor valor
    def vendidoMenorValor(self):
        lista_vendidos = []
        lista_vendidos = ([x for x in self.__class__.lista_caminhonetes if x.cpf_comprador != 0])
        if lista_vendidos != []:
            print("CAMINHONETE VENDIDO COM MENOR VALOR")
            print(vars(min(lista_vendidos, key= lambda x: x.valor)))
        else:
            raise ErrorException("ERRO! Não existem caminhonetes no sistema")
    
    # RELATÓRIO CAMINHONETE MAIOR VALOR DE VENDA
    # cria uma lista de veiculo vendido e depois usa a função max para comparar os valores e retornar o objeto de maior valor
    def vendidoMaiorValor(self):
        lista_vendidos = []
        lista_vendidos = ([x for x in self.__class__.lista_caminhonetes if x.cpf_comprador != 0])

        if lista_vendidos != []:
            print("CAMINHONETE VENDIDO COM MAIOR VALOR")
            print(vars(max(lista_vendidos, key= lambda x: x.valor)))
        else:
            raise ErrorException("ERRO! Não existem caminhonetes no sistema")