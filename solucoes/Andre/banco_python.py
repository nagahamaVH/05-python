class Cliente:
    def __init__(self, nome):
        self.nome = nome

class ClienteFisico(Cliente):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf

class ClienteJuridico(Cliente):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj

class Conta():
    def __init__(self, saldo, cliente):
        self.saldo = saldo
        self.cliente = cliente
    
    def saque(qtd):
        saldo -= qtd
        return qtd

    def deposito(qtd):
        saldo += qtd

class ContaCorrente(Conta):
    def __init__(self, saldo, cliente):
        super().__init__(saldo, cliente)

class ContaPoupanca(Conta):
    def __init__(self, saldo, cliente):
        super().__init__(saldo, cliente)

print("### Teste de cliente ###")
c = Cliente("André")
print(c.nome)
print("### Teste de cliente físico ###")
cf = ClienteFisico("João", 12345)
print(cf.nome, cf.cpf)
print("### Teste de cliente jurídico ###")
cj = ClienteJuridico("Josefina Ltda", 321654)
print(cj.nome, cj.cnpj)