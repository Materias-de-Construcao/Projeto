import pyodbc as bd
import os
import getpass as gp
def conectantar ():
    global conectando
    os.system('cls')
    while True:
        uID =input("Digite o seu login:  ")
        senha =gp.getpass("Digite a senha do seu banco de dados:  ")
        dataBase =input("Digite o banco de dados que quer acessar:  ")
        try:
            conectando = bd.connect (driver="{SQL Server}",
                                server="regulus.cotuca.unicamp.br",
                                uid =f"{uID}", # Login para acessar o banco de dados. Para os que usam isso
                                database=f"{dataBase}", #Banco de dados que tem o nome. Para caso use um servidor próprio 
                                pwd=f"{senha}") #Senha do banco de dados 
            print (F"Conseguimos conectar no seu banco de dados \n esse é o menu:")
            break
        
        except:
            print (F"Algo deu errado  !!!")
    menu()        

def menu ():
    os.system('cls')
    print (10 * "=-", "MENU", 10 * "=-")
    print (F"0: Sair")
    print (f"1: Listar ")
    print (F"2: Deletar do Banco")
    print (F"3: Alterar")
    print (F"4: Inserir no Banco")
    opcao = input(F"Digite sua opção: ")

    selecionar(opcao)

def selecionar (opcao):
    match opcao:
        case '4':
            Insert()
        case '2':
            print ('del')
            Delete ()
        case '3':
            print (f"Alter")
            #Alter()
        case '1':
            List()
        case '0':
            print (F"Saindo")
            quit()
        case _:
            print (F"Opção não existente")
            input(F"[ENTER] para voltar ao menu: ")
            menu()

def Insert ():
    cursorBD = conectando.cursor()
    nomeProduto = '1'
    while nomeProduto != '0':
        print (10 * "=-", "Cadastro de produto ", 10 * "=-")
        nomeProduto = input(f"Digite o nome do produto que queira cadastrar [caso queira encerrar digite 0]: ")
        if nomeProduto != '0':
            descricao = input(f"Digite a descrição de {nomeProduto}: ")
            preco = float(input(f"Digite o valor de {nomeProduto}:  "))
            qntEstoque = int(input(F"Digite a quantidade em estoque:  "))
            cursorBD.execute("insert into Mat.Produto " +\
                  "       (NomeProd, Descrição, Preço, QntEstoque)"+\
                  " VALUES "+\
               f"('{nomeProduto}', '{descricao}', '{preco}', {qntEstoque})")
        else:
            print (F"Saindo")
    menu()
    cursorBD.commit()
 

def Delete():
    cursorBD = conectando.cursor()
    idProduto = 1
    while idProduto != 0:
        idProduto = int(input(F"Digite o ID do produto que deseja excluir [0 para encerrar]: "))
        if idProduto == 0:
            break
        else:
            resultado = cursorBD.execute("SELECT *FROM Mat.Produto where codProduto = ?", idProduto)
# def Alter():

def List():
    dataframe = 0
    cursorBD = conectando.cursor()
    try:
        resultado = cursorBD.execute(
            'SELECT * FROM Mat.Produto')
        itens = resultado.fetchall()
    except:
        print (f"Erro na busca dos dados.")
    print(10*'=-', "Tabela de Produtos",10*'-=')
    print(F"|ID|\t\t|Nome|\t\t|Descrição|\t\t|Preço|\t\t|Em Estoque|")
    for i in itens:
        print(f"{i[0]}\t|{i[1]}\t|{i[2]}\t|{i[3]}\t{i[4]}")
    input(F"[ENTER] para voltar ao menu ")
    menu()
conectantar()
