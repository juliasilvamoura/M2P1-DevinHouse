from datetime import datetime, date
from Veiculo import Veiculo
from exception import ErrorException
import uuid


class Carro(Veiculo):
    lista_carros = []
    def __init__(self, dataFabricacao, nome_modelo, placa, valor, cor, total_portas, tipo_combustivel, potencia):
        super().__init__(dataFabricacao, nome_modelo, placa, valor, cor)
        self.total_portas = total_portas
        self.tipo_combustivel = tipo_combustivel.lower()
        self.potencia = potencia
            
        if(dataFabricacao and nome_modelo and placa and valor and cor and total_portas and potencia and tipo_combustivel):
            if(tipo_combustivel.lower() == 'gasolina' or tipo_combustivel.lower() == 'flex'):
                try:
                    self.dataFabricacao = datetime.strptime(dataFabricacao, '%d/%m/%Y').date() 
                    self.__class__.lista_carros.append(self)
                except Exception as erro:
                    print(f"Erro! Data em formato errado | {erro}")
            else:
                raise ErrorException("O Combustivel só pode ser GASOLINA ou FLEX")
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

    # VENDER CARRO
    # add o cpf no veiculo vendido e chamo a função realizar Histórico
    def venderVeiculos(self, cpf_comprador):
        self.cpf_comprador = cpf_comprador
        Veiculo.realizarHistorico(self, cpf_comprador)

    
     # RELATÓRIO CARROS
    def listar(self):
        if self.__class__.lista_carros!= []:
            print("LISTA DE CARROS")
            print(self.modelar(self.__class__.lista_carros))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")

    # RELATÓRIO CARROS VENDIDOS
    # compara qual tem cpf != 0 e retorna uma lista de objetos
    def vendidos(self):
        vendidos = []
        print("CARROS VENDIDOS")
        vendidos = ([x for x in self.__class__.lista_carros if x.cpf_comprador != 0])
        if vendidos != []:
            print(self.modelar(vendidos))
        else:
            raise ErrorException("ERRO! Não existem carros vendidos")

    # RELATÓRIO CARROS DISPONIVEIS
    # compara qual tem cpf = 0 e retorna uma lista de objetos
    def disponiveis(self):
        disponiveis = []
        print("CARROS DISPONIVEIS")
        disponiveis =([x for x in self.__class__.lista_carros if x.cpf_comprador == 0])
        if disponiveis != []:
            print(self.modelar(disponiveis))
        else:
            raise ErrorException("ERRO! Não existem carros disponiveis")

    # RELATÓRIO CARRO MENOR VALOR DE VENDA
    # cria uma lista de veiculo vendido e depois usa a função min para comparar os valores e retornar o objeto de menor valor
    def vendidoMenorValor(self):
        lista_vendidos = []
        lista_vendidos = ([x for x in self.__class__.lista_carros if x.cpf_comprador != 0])
        if lista_vendidos != []:
            print("CARRO VENDIDO COM MENOR VALOR")
            print(vars(min(lista_vendidos, key= lambda x: x.valor)))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")
    
    # RELATÓRIO CARRO MAIOR VALOR DE VENDA
    # cria uma lista de veiculo vendido e depois usa a função max para comparar os valores e retornar o objeto de maior valor
    def vendidoMaiorValor(self):
        lista_vendidos = []
        lista_vendidos = ([x for x in self.__class__.lista_carros if x.cpf_comprador != 0])

        if lista_vendidos != []:
            print("CARRO VENDIDO COM MAIOR VALOR")
            print(vars(max(lista_vendidos, key= lambda x: x.valor)))
        else:
            raise ErrorException("ERRO! Não existem carros no sistema")

    

# car1 = Carro("05/07/2022","corsa","Fzu1520",50000,"amarelo",4,"Gasolina", 350)
# car2 = Carro("05/07/2022","corsa","fzu1520",70000,"amarelo",4,"gasolina", 350)
# vei = Veiculo(None,None,None,None,None)
# # car2.alterarInformacoes(1,"Rosa")
# vei.listar()
# car2.venderVeiculos("457.180.448.21")
# car1.venderVeiculos("457.180.448.21")
# car1.listar()
# print("listar:")
# car1.listarInformacoes()
# print("VEICULOS")
# Carro.lista_carros[0].disponiveis()
# Veiculo.lista_veiculos[2].listar()
# car1.venderVeiculos("457.180.448.21")
# car1.vendidoMenorValor()
# print(car1.carros)
