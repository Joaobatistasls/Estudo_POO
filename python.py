# Criando uma classe
class Pessoa:
    # Criando a função contruto, parâmetros e os atributos
    def __init__(self, nome, sobrenome, idade, telefone, saldo):
        # Criando as caracterica do objeto com os atributos e deixando os atributos privados
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__telefone = telefone
        self.__saldo = saldo
        self.__codigo_banco = "001"

    # Criando um método para exibir o nome da pessoa
    def __informa_pessoa(self):
        print(f"o nome do titular é {self.__nome} {self.__sobrenome} e tem {self.__saldo} na conta.")

    # Criando um método para amostra o extrato
    def extrato(self):
        print(f"o titular {self.__nome} {self.__sobrenome} tem o saldo de {self.__saldo} na conta.")
    
    # Criando um método para deposita, adicionando um parâmetro no método.
    def deposita(self, valor):
        self.__saldo += valor

    # Criando um método para sacar, subtraindo o valor através de um parâmetro
    def saca(self, valor):
        self.__saldo -= valor

    # Criando um método para tranferir, usando 
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # Criando método para saber o banco
    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

# Criando as referências
pessoa = Pessoa("João", "Batista", 19, 93335750, 100.0)

# Imprimindo o método #staticmethod
print(pessoa.codigo_banco())




"""
pessoa2 = Pessoa("Steve", "Hanakagi", 18, 93685296, 40.0)

# Transfereindo 20.0 reaos da pessoa 1 para pessoa 2 através do método
pessoa.transfere(20.0, pessoa2)

# Imprimindo o extrato da pessoa 2 após a transferência
print(pessoa2.extrato())
"""

"""
# Criando a referência com as informações da pessoa
pessoa = Pessoa("João", "Batista", 19, 93335750, 100.0)

# Usando o método informa pessoa através da referência
print(pessoa.informa_pessoa())

# Depositando dinheiro na conta através da referência
pessoa.deposita(100.0)

# Imprimindo saldo da conta através da referência
print(pessoa.extrato())
"""

'''
# Criando outra referêcia pessoa
outraReferencia = pessoa

# Diferênciando uma referência
outraReferencia = None

# Criando as carcteristicas de pessoa 
pessoa = Pessoa("João", "Batista", 19, 93335750)
# Criando as carcteristicas de pessoa 2
pessoa2 = Pessoa("Steve", "Hanagaki", 19, 93285695)

#Exibindo mensagem 
print("o nome da pessoa é {} {}, tem {} anos e seu telefone é {}".format(pessoa.nome, pessoa.sobrenome, pessoa.idade, pessoa.telefone))
print("o nome da pessoa é {} {}, tem {} anos e seu telefone é {}".format(pessoa2.nome, pessoa2.sobrenome, pessoa2.idade, pessoa2.telefone))
'''