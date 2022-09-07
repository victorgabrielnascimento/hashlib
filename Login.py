import hashlib

class x1:

    def registro():
        xlogin = input("Digite seu usuário:")
        xsenha = input("Digite sua senha:")
        xhash = (xsenha).encode("utf8")
        xxhash = hashlib.md5(xhash).hexdigest()
        
        with open("db.txt", "a") as yanperone:
            yanperone.write(str(xlogin) + "," + (xxhash) + "\n")
    

    def login():
        zlogin = input("Digite seu usuário: ")
        
        with open("db.txt", "r") as yanperone:
            b1 = yanperone.read()    
            if zlogin in b1:
                zsenha = input("Digite sua senha: ") 
                xhash = (zsenha).encode("utf8")
                xxhash = hashlib.md5(xhash).hexdigest()

                if xxhash in b1:
                    print("Logado com sucesso!")
                else:
                    print("Senha incorreta, tente novamente!")
                    x1.login()
            else: 
                print("Usuário invalido, tente novamente!")
                x1.login() 

    def sair():
        print("Obrigado, até a próxima")
        exit

    def menuzinho():
        print("Olá! bem vindo")
        print("          Menu ")
        print("(I) Resgistrar-se")
        print("(II) Logar")
        print("(III) Sair")
        ação = input("Escolha uma opção acima:")
        if ação == "1":
            x1.registro()
        elif ação =="2":
            x1.login()
        elif ação == "3":
            x1.sair()

if __name__ == "__main__":
    x1.menuzinho()
