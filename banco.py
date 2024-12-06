class ContaBancaria:
    titular = ""
    saldo = 0,00
    credit = 0,00
    
    def __init__(self, titular, saldo, credit):
        self.titular = titular
        self.saldo = saldo
        self.credit = credit

    def depositar(self, to_deposit):     
        if(to_deposit < 0):
            print("0")
        else:
            self.saldo += to_deposit
            print("1")
        
    def levantar(self, to_extract):
        if(self.saldo + self.credit >= to_extract):
            self.saldo += -to_extract
            print("1")
        else:
            print("0")
    
    def exibir_saldo(self):
        print("{:.2f}".format(self.saldo))
    
    def exibir_info(self):
        print(f"{self.titular} {self.saldo:.2f} {self.credit:.2f}")

conta = ContaBancaria("João", 1000.00, 500.00)
conta.depositar(-500.00)
conta.depositar(500.00)
conta.levantar(1200.00)
conta.levantar(1200.00)
conta.exibir_info()