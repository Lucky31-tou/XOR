def len(var):
    ''' Renvoi la longueur d'une liste ou d'un string '''
    long = 0
    for elt in var:
        long += 1
    return long


def no_space(word:str):
    ''' Retire tous les espaces d'un string '''
    mot = ""
    for l in word: 
        if l != " ":
            mot += l
    return mot 

def copy(arr:list):
    ''' Renvoi une copie d'une liste '''
    arrR = []
    for elt in arr:
       append(arrR, elt)
    return arrR

def join(tab:list, sep=""):
    ''' Convertit une liste en string '''
    arr = ""
    for elt in tab:
        arr = arr + str(elt) + sep
    return arr

def reverse(element):
    ''' Inverse les caractères d'un string ou d'une liste '''
    ty = 0
    if type(element) == str:
        element = list(element)
        ty = 1
    for i in range(len(element)//2):
        element[i], element[-(i + 1)] = element[-(i + 1)], element[i]
    if ty == 1:
        element = join(element)
    return element


def binary(num:int):
    ''' Converti un nmobre décimal en nombre binaire '''
    # Si le nombre est 0
    if num == 0:
        return "0"
    
    test = num
    bin = ""
    while test > 0:
        # Mettre à jour le résultat binaire
        bin = str(test % 2) + bin
        test = test // 2

    return bin


def integer(bin:str):
    ''' Converti un chiffre binaire en entier naturel '''
    num_bin = []
    for c in reverse(bin): # Cette fonction lit les bits de doite à gauche
        num_bin += c
    
    num = 0
    for i in range(len(num_bin)):
        if num_bin[i] == "1":
            num += 2**i
    return num


def append(arr:list, elt):
    ''' Ajoute un élément à une liste '''
    arr += [0]
    arr[len(arr)-1] = elt
    return arr


def pop(arr: list, index=None):
    ''' Supprime un élément de la liste en place et le renvoie '''
    if index is None:
        index = len(arr) - 1
    elt = arr[index]

    # Supprimer l'élément directement dans la liste originale
    arr[index:index+1] = []  # équivalent à del arr[index] mais compatible avec ton style
    return elt


def pair(i:int):
    ''' Renvoi True si i est pair '''
    return i%2 == 0
    

class Pile:

    def __init__(self):
        self.pile = []

    def empty(self):
        ''' Renvoie True si la pile est vide '''
        return len(self.pile) == 0
    
    def stack(self, elt):
        ''' Ajoute un élément à la pile '''
        append(self.pile, elt)

    def unstack(self):
        ''' Supprime le dernier élément et le renvoi '''
        return pop(self.pile)
    
class File:

    def __init__(self):
        self.file = []

    def empty(self):
        ''' Renvoie True si la file est vide '''
        return len(self.file) == 0
    
    def add(self, elt):
        ''' Ajoute un élément à la file '''
        append(self.file, elt)

    def remove(self):
        ''' Supprime le premier élément et le renvoi '''
        return pop(self.file, 0)
    

