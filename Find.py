##############################################################################################
#                                                                                            #
#                                  - Python --- Laura R3dB  -                                #
#                                         V.3.10                                             #
##############################################################################################

##########   Import    ############
import hashlib

mp_dico={}
mp_brut=[]

with open("./mpp.txt", encoding="utf-8") as txt:
    for ligne in txt :
        a=ligne
        a=a[:-1] # because '\n'
        mp_brut= mp_brut + [a] 
       
def fct_mp_dico(mp_brut,mp_dico):
    for i in range(0,len(mp_brut)):
        MD5 = hashlib.md5()
        MD5.update(bytes(mp_brut[i], encoding = "utf-8"))
        mp_dico[MD5.hexdigest()]= (mp_brut[i])       
        SHA1 = hashlib.sha1()
        mp_dico[hashlib.sha1(bytes(mp_brut[i], encoding = "utf-8")).hexdigest()]=(mp_brut[i])
        SHA256 = hashlib.sha256()
        SHA256.update(bytes(mp_brut[i], encoding = "utf-8"))
        mp_dico[SHA256.hexdigest()]=mp_brut[i]
        SHA512 = hashlib.sha512()
        SHA512.update(bytes(mp_brut[i], encoding = "utf-8"))
        mp_dico[SHA512.hexdigest()]=mp_brut[i]
    return mp_dico

def fct_mpbrut(mp_dico):
    if mp_dico.get(H)== None:
        return print("Sorrry Bro ! I don't have it !")
    else :
        return print("The PassWord is : " + mp_dico.get(H))
        
def fct_type_de_H(mp_dico):
    if len(H)>=64:
        if len(H)==64:
            return print("Is: SHA256 , len is 64")
        elif len(H)==128:
            return print("Is : SHA512 , len is 128")
        else :
            return print("I don't know which one it's.")
    else :
        if  len(H)==40:
            return print("Is : SHA1 ,len is 40")
        elif len(H)==32:
            return print("Is : MD5, len is 32")
        else :
            return print("I don't know which one it's.")

############# Mes Apels ##############
fct_mp_dico(mp_brut,mp_dico)
H = input("put your crypt here.... " )
fct_mpbrut(mp_dico)
fct_type_de_H(mp_dico)

