from native_py import*
# Chiffrement XOR
def add_bin(bin1, bin2):
    ''' Applique le XOR entre deux chaines binaires '''
    # Aligne les longueurs des binaires avec deszéros devant
    diff = len(bin1) - len(bin2)
    if diff > 0:
        bin2 = "0" * diff + bin2
    else:
        bin1 = "0" * (-diff) + bin1

    # XOR bit à bit
    result = ""
    for i in range(len(bin1)):
        if bin1[i] == bin2[i]:
            result += "0"
        else:
            result += "1"

    return result


def encryption(mess, key):
    ''' Chiffre un message '''
    code = ""
    i = 0 # Index de la clé
    for l in mess:
        if i == len(key):
            i = 0 # Recommence si on arrive à la fin de la clé
        add = add_bin(binary(ord(l)), binary(ord(key[i])))
        code += str(integer(add)) + " " # Ajout d'un entier suivi d'un espace
        i += 1
    return code


def decoding(code, key):
    ''' Décode un messsage '''
    mess = ""
    num = ""
    i = 0 # Index de la clé
    for n in code:
        if n == " ":
            if i == len(key):
                i = 0
            # Applique le XOR pour retrouver le caractère
            add = add_bin(binary(int(num)), binary(ord(key[i])))
            mess += str(chr(integer(add)))
            i += 1
            num = "" # Réinitialise le nombre
        else: 
            num += n
    return mess



if __name__=="__main__":
    # Initialisation de la clé par l'utilisateur
    mess = input("Votre message : ")
    while no_space(mess) == "":
        mess = input("Votre message est trop court : ")

    # Initialisation de la clé par l'utilisateur
    key = input("Votre clé : ")
    while no_space(key) == "" or len(key) > 8:
        if no_space(key) == "":
            key = input("Votre clé doit être une combinaison de caractères : ")
        else:
            key = input("Votre clé ne doit pas avoir plus de 8 caractères : ")

    # Chiffrement du message
    code = encryption(mess, key)
    print(code)

    # Déchiffrement du message
    print(decoding(code, key))