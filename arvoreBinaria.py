class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)
    
    def _inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.esquerda)            
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.direita)  

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def mostrar_in_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_in_ordem_recursivo(self.raiz)

    def mostrar_in_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_in_ordem_recursivo(no.esquerda)
        print(no.valor, end=' ')
        if no.direita is not None:
            self.mostrar_in_ordem_recursivo(no.direita)
    
    def mostrar_raiz(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            print('Raiz:', self.raiz.valor, end=' ')   

    def altura(self):
        if self.raiz is None:
            return 0
        else:
            return self._altura(self.raiz) 
    
    def _altura(self, no):
        if no is None:
            return 0
        altura_e = 0
        altura_d = 0

        if no.esquerda is not None:
            altura_e = 1 + self._altura(no.esquerda)
        if no.direita is not None:
            altura_d = 1 + self._altura(no.direita)
        if altura_e > altura_d:
            return altura_e
        else:
            return altura_d

    def mostrar_nos_internos(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_nos_internos_recursivo(self.raiz)

    def mostrar_nos_internos_recursivo(self, no):
        if no is not None:
            if no.esquerda is not None or no.direita is not None:
                print(no.valor, end=' ')
            self.mostrar_nos_internos_recursivo(no.esquerda)
            self.mostrar_nos_internos_recursivo(no.direita)

    def mostrar_as_folhas(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_as_folhas_recursivo(self.raiz)

    def mostrar_as_folhas_recursivo(self, no):
        if no is not None:
            if no.esquerda is None and no.direita is None:
                print(no.valor, end=' ')
            self.mostrar_as_folhas_recursivo(no.esquerda)
            self.mostrar_as_folhas_recursivo(no.direita)
            
    def procurar(self, v):
        if self.raiz is None:
            return False
        else:
            return self._procurar(self.raiz, v)
    
    def _procurar(self, no, v):
        if no is None:
            return False
        if no.valor == v:
            return True
        if self._procurar(no.esquerda, v):
            return True
        if self._procurar(no.direita, v):
            return True


def menu():
    arvore = ArvoreBinaria()

    while True:
        print('------------------------------------------------')
        print("""
            MENU
            1 - INSERIR NÓ NA ÁRVORE
            2 - EXIBIR A ALTURA DA ÁRVORE
            3 - EXIBIR OS NÓS INTERNOS
            4 - EXIBIR OS NÓS FILHOS 
            5 - EXIBIR O NÓ RAIZ
            6 - PROCURAR VALOR NA ÁRVORE
            7 - ENCERRAR
        """)
        print('------------------------------------------------')

        op = int(input('Digite a opção que você deseja realizar: '))

        if op == 1:
            num = int(input('Digite quantos nós a ser inserido na arvore: '))
         
            for _ in range(num):
                valor = int(input('Digite o valor do nó a ser inserido: '))
                arvore.inserir_em_nivel(valor)
            print('\n')
            print('Os nós foram inseridos na árvore.')
            print('\n')
            
            
        elif op == 2:
            print('Altura: ', arvore.altura())
            print('\n')
            
        elif op == 3:
            print('Nós internos da árvore:')
            arvore.mostrar_nos_internos()
            print('\n')
        elif op == 4:
            print('\n')
            print('Nós folha da árvore:')
            arvore.mostrar_as_folhas()
            print('\n')
        elif op == 5:
            print('Nó raiz:')
            arvore.mostrar_raiz()
            print('\n')
        elif op == 6:
            valor = int(input('Digite o valor a ser procurado na arvore: '))
            if arvore.procurar(valor):
                print('\n')
                print(f'O valor {valor} está na árvore.')
            else:
                print(f'O valor {valor} não está na árvore.')
                print('\n')
        elif op == 7:
            break
        else:
            print('Opção inválida. Tente novamente.')
            
menu()
