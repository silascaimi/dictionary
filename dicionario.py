class Dic:
    def __init__(self):
       self.regs = []
       self.keys = []

    def Member(self, k):
        for i in range(len(self.keys)):
            if self.keys[i]==k :
                return True
        return False

    def Search(self, k):
        first = 0
        last = len(self.keys)-1

        while first <= last :
            mid = int((first + last)/2)
            if self.keys[mid] == k:
                return mid
            else:
                if k < self.keys[mid]:
                    last = mid-1
                else:
                    first = mid+1
        return -1

    def Insert(self, r, k):
        self.regs.append(r)
        self.keys.append(k)

    def Delete(self, k):
        x = self.Search(k)
        result = self.regs[x]
        while x < len(self.keys):
            self.regs[x-1] = self.regs[x]
            self.keys[x-1] = self.keys[x]
            x+=x
        return result

    def bubbleSort(self):
        for i in range(len(self.keys)-1,0,-1):
            for j in range(i):
                if self.keys[j] > self.keys[j + 1]:
                    swap = self.keys[j]
                    self.keys[j] = self.keys[j+1]
                    self.keys[j+1] = swap
                    reg = self.regs[j]
                    self.regs[j] = self.regs[j+1]
                    self.regs[j+1] = reg

    # Funcao separar pega o ultimo elemento e coloca 
    # na posicao correta do vetor ordenado
    def separar(self, inicio, fim):
        i = inicio - 1         # indice do menor elemento
        pivot = self.keys[fim]
 
        for j in range(inicio , fim):
 
            # Se o elemento atual é menor ou igual ao pivot
            if   self.keys[j] <= pivot:
         
                # incrementa o indice do menor elemento
                i = i + 1
                self.keys[i],self.keys[j] = self.keys[j],self.keys[i] # troca a chave
                self.regs[i],self.regs[j] = self.regs[j],self.regs[i] # troca o registro

        self.keys[i+1],self.keys[fim] = self.keys[fim],self.keys[i+1] # troca a chave
        self.regs[i+1],self.regs[fim] = self.regs[fim],self.regs[i+1] # troca o registro

        return i + 1

    def quickSort(self, inicio = None, fim = None):
        
        if inicio == None:
            inicio = 0

        if fim == None:
            fim = len(dic.keys)-1

        if inicio < fim:
 
            posPivo = self.separar(inicio, fim)
 
            # Ordena os elementos antes e depois da particao
            self.quickSort(inicio, posPivo-1)
            self.quickSort(posPivo+1, fim)


    def heapify(self, n, i): 
        max = i
        e = 2 * i + 1     # filho esquerdo
        d = 2 * i + 2     # filho direito
  
        # Verifica se o filho esquerdo existe e é maior que a raiz
        if e < n and self.keys[i] < self.keys[e]: 
            max = e 
  
        # Verifica se o filho direito existe e é maior que a raiz
        if d < n and self.keys[max] < self.keys[d]: 
            max = d 
  
        # Troca a raiz se necessario
        if max != i: 
            self.keys[i],self.keys[max] = self.keys[max],self.keys[i] # troca a chave
            self.regs[i],self.regs[max] = self.regs[max],self.regs[i] # troca o registro
  
            # Heapify 
            self.heapify(n, max) 
  
    # A funcao principal ordena o vetor
    def heapSort(self): 
        n = len(self.keys) 
  
        # Constroe um maxheap 
        for i in range(n, -1, -1): 
            self.heapify(n, i) 
  
        # Extrai os elementos um por um 
        for i in range(n-1, 0, -1): 
            self.keys[i], self.keys[0] = self.keys[0], self.keys[i] # troca a chave 
            self.regs[i], self.regs[0] = self.regs[0], self.regs[i] # troca o registro
            self.heapify(i, 0)

    # Funcao que faz o insertion sort 
    def insertionSort(self): 
  
        for i in range(1, len(self.keys)): 
  
            key = self.keys[i] # armazena a chave
            reg = self.regs[i] # armazena o registro
  
            # Move os elementos de self.keys[0..i-1], que são 
            # maiores que key, para uma posicao a frente
            # de sua posicao atual 
            j = i-1
            while j >= 0 and key < self.keys[j] : 
                    self.keys[j+1] = self.keys[j] 
                    self.regs[j+1] = self.regs[j] 
                    j -= 1
            self.keys[j+1] = key
            self.regs[j+1] = reg

    # Funcao que faz o mergeSort
    def mergeSort(self, arrayKeys = None, arrayRegs = None): 

        if arrayKeys == None:
            arrayKeys = self.keys

        if arrayRegs == None:
            arrayRegs =  self.regs

        if len(arrayKeys) > 1: 
            mid = len(arrayKeys)//2 # Encontra o meio do vetor
            eKeys = arrayKeys[:mid] # divide os elementos chaves 
            dKeys = arrayKeys[mid:] # do vetor em metade

            eRegs = arrayRegs[:mid] # divide os elementos registros
            dRegs = arrayRegs[mid:] # do vetor em metade
  
            self.mergeSort(eKeys, eRegs) # Ordena a primeira metade desse conjunto de chaves e registros
            self.mergeSort(dKeys, dRegs) # Ordena a segunda metade desse conjuto de chaves e registros
  
            i = j = k = 0
          
            # Copia os dados dos vetores temporarios
            while i < len(eKeys) and j < len(dKeys): 
                if eKeys[i] < dKeys[j]: 
                    arrayKeys[k] = eKeys[i]
                    arrayRegs[k] = eRegs[i]

                    i += 1
                else: 
                    arrayKeys[k] = dKeys[j]
                    arrayRegs[k] = dRegs[j]
                    j += 1
                k += 1
          
            # Verifica se algum elemento foi deixado
            while i < len(eKeys): 
                arrayKeys[k] = eKeys[i] 
                arrayRegs[k] = eRegs[i]
                i += 1
                k += 1
          
            while j < len(dKeys): 
                arrayKeys[k] = dKeys[j] 
                arrayRegs[k] = dRegs[j]
                j += 1
                k += 1


dic = Dic()
dic.Insert("Joao",4)
dic.Insert("Maria",3)
dic.Insert("Jose",7)
dic.Insert("Marina",1)
dic.Insert("Luana",5)
#dic.bubbleSort()
#print(dic.Member(5))
#print(dic.Member(7))
#print(dic.Search(3))
#print(dic.Search(4))
#dic.Delete(5)
#print(dic.Member(5))

print(dic.keys)
print(dic.regs)

#dic.quickSort()
#dic.heapSort()
#dic.insertionSort()
dic.mergeSort()

print(dic.keys)
print(dic.regs)


