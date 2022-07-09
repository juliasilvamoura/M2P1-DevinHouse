from carros import Carro
from motos import Moto
from caminhonetes import Caminhonete
from veiculos import Veiculo, HistoricoTransferencia
from exception import ErrorException
import time

car1 = Carro("05/07/2022","corsa","fzu1520",50000,"amarelo",4,"gasolina", 350)
car2 = Carro("05/07/2022","corsa","fzu1521",50000,"amarelo",4,"gasolina", 350)
moto1 = Moto("05/07/2022","corsa","fzu1500",5000,"amarelo",2,150)
moto2 = Moto("05/07/2022","corsa","fzu1501",5000,"amarelo",2,150)
caminhonete1 = Caminhonete("05/07/2022","corsa","fzu2000",50000,4, 150,"gasolina", 350)
caminhonete2 = Caminhonete("05/07/2022","corsa","fzu2001",50000,4, 150,"gasolina", 350)

# Foi criado para ele imprimir todos da classe veiculos, se passar a instancia carro, moto ou caminhonete ele 
# não imprime todos os veiculos, só os da classe da instancia passada já que tem o mesmo nome as funções na classe 
# pais e na classe filha
vei = Veiculo(None,None,None,None,None)
# Para a função imprimir o Histórico de vendas
ht = HistoricoTransferencia()

lista =[]
# Para imprimir melhor
for obj in Veiculo.lista_veiculos:
    if obj.placa != None:
        lista.append({"tipo": obj.tipo,"modelo": obj.nome_modelo, "placa": obj.placa, "valor": obj.valor,"cor": obj.cor})

# para pegar o objeto veiculo que quer
lista1 = [car1,car2,moto1,moto2,caminhonete1,caminhonete2]



def listarVeiculos():
    print("VEICULOS".center(50, "-"))
    veiculo = None
    for x in lista:
        print(x)
    placa = input("Qual a placa do veiculo? ")
    for x in lista1:
        if x.placa == placa:
            veiculo = x
            return True, veiculo
    print("Placa errada")
    time.sleep(10)
    return False, veiculo       

while True:

    test = False
    while not test:
        test, veiculo = listarVeiculos()

    print("Venda".center(40,"-"))
    print("1. Vender Veículos".ljust(40))
    print("Listar Informações".center(40,"-"))
    print("2. Listar Informações do Veículo".ljust(40))
    print("Alterar Informações".center(40,"-"))
    print("3. Alterar informações".ljust(40))
    print("Relatórios".center(40,"-"))
    print("4. Relatórios".ljust(40))
    print("Histórico Vendas".center(40,"-"))
    print("5. Histórico Vendas".ljust(40))
    print("Sair".center(40,"-"))
    print("0. Sair".ljust(40))

    op = input("O que deseja realizar: ")

    if op.isnumeric():
        match op:
            case "1":
                cpf = input("Digite o CPF do comprador: ")
                veiculo.venderVeiculos(cpf)
            case "2":
                veiculo.listarInformacoes()
            case "3":
                print("""
                Alterar:
                1 - Cor
                2 - Valor
                """)
                info_alterar = input("Opção que deseja alterar: ")
                
                if info_alterar == "1":
                    novo_valor = input("Qual a nova cor: ")
                    veiculo.alterarInformacoes(int(info_alterar),novo_valor)
                elif info_alterar == "2":
                    novo_valor = input("Qual o novo valor: ")
                    veiculo.alterarInformacoes(int(info_alterar),int(novo_valor))
            case "4":
                print("""
                Para qual tipo de veiculo deseja gerar relatório:
                1 - Moto/Triciclo
                2 - Carro
                3 - Caminhonete
                4 - Todos
                """)
                op_veiculo = input("Qual a opção de veiculo: ")
                print("""
                Qual relatório deseja gerar:
                1 - Listar
                2 - Disponiveis
                3 - Vendidos
                4 - Vendidos maior Valor
                5 - Vendidos menor Valor
                """)
                op_relatorio = input("Escolha a opcâo: ")

                if op_relatorio == "1":
                    if op_veiculo.isnumeric():
                        match op_veiculo:
                            case "1":
                                Moto.lista_motos[0].listar()
                            case "2":
                                Carro.lista_carros[0].listar()
                            case "3":
                                Caminhonete.lista_caminhonetes[0].listar()
                            case "4":
                                vei.listar()
                elif op_relatorio == "2":
                    if op_veiculo.isnumeric():
                        match op_veiculo:
                            case "1":
                                Moto.lista_motos[0].disponiveis()
                            case "2":
                                Carro.lista_carros[0].disponiveis()
                            case "3":
                                Caminhonete.lista_caminhonetes[0].disponiveis()
                            case "4":
                                vei.disponiveis()
                elif op_relatorio == "3":
                    if op_veiculo.isnumeric():
                        match op_veiculo:
                            case "1":
                                Moto.lista_motos[0].vendidos()
                            case "2":
                                Carro.lista_carros[0].vendidos()
                            case "3":
                                Caminhonete.lista_caminhonetes[0].vendidos()
                            case "4":
                                vei.vendidos()
                elif op_relatorio == "4":
                    if op_veiculo.isnumeric():
                        match op_veiculo:
                            case "1":
                                Moto.lista_motos[0].vendidoMaiorValor()
                            case "2":
                                Carro.lista_carros[0].vendidoMaiorValor()
                            case "3":
                                Caminhonete.lista_caminhonetes[0].vendidoMaiorValor()
                            case "4":
                                vei.vendidoMaiorValor()
                elif op_relatorio == "5":
                    if op_veiculo.isnumeric():
                        match op_veiculo:
                            case "1":
                                Moto.lista_motos[0].vendidoMenorValor()
                            case "2":
                                Carro.lista_carros[0].vendidoMenorValor()
                            case "3":
                                Caminhonete.lista_caminhonetes[0].vendidoMenorValor()
                            case "4":
                                vei.vendidoMenorValor() 
                                
            case "5":
                ht.listarHistorico()             
                

            case "0":
                break        