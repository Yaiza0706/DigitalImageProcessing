import time
import numpy as np
from tkinter import *  # pour sauvegarder l'image
from turtle import *   # pour sauvegarder l'image
import turtle as t
import random
from PIL import Image
t.speed('fastest')
global taille# taille means size in french
taille=3    #taille est la taille d'un "pixel" du qr code
"1 signifie noir (rempli) 0 signifie blanc, vide"
t.bye()#à enlever si on veut faire tourner trace()
def generate_empty():# on fait un qr code 21*21 avec des cibles de taille 7 le reste vide
    M=[[1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1],[1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],[1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1],[1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1],[1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1],[1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    return(np.array(M))


def sym_horizontal(M):
    N=[]
    for i in range(len(M)):
        N.append(M[len(M)-(i+1)])
    return(N)

def liste_bin_to_dec_number(L):
    n = len(L)
    result = 0
    for i in range(n):
        result += L[i]*(2**(n-(i+1)))
    return(result)

def get_and_verif_Id(M):
    bin_ide1 = []
    bin_ide2 = []
    bin_ide3 = []
    bin_ide4 = []
    clef = []
    for j in range(7):
        bin_ide1.append(M[8][j])
        bin_ide2.append(M[9][j])
        bin_ide3.append(M[10][j])
        bin_ide4.append(M[11][j])
    for j in range(7):
        print(M,"e")
        clef.append(M[12][j])
    bin_ide = bin_ide1+bin_ide2+bin_ide3+bin_ide4
    dec_ide = liste_bin_to_dec_number(bin_ide)
    clef_base_10 = liste_bin_to_dec_number(clef)
    liste_decimale_ide = decList(dec_ide)
    clef_potentielle = sum(liste_decimale_ide)
    if clef_potentielle == clef_base_10:
        print("Clef valide")
        return(clef_base_10)
    else:
        print("Erreur, mauvaise clef")
        return(-1)


def save_as_png(canvas,fileName):
    canvas.postscript(file = fileName + '.eps')
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.png' , 'png')




def trace(M,taille):
    M=sym_horizontal(M)
    t.up()
    t.speed('fastest')
    t.down()
    t.bgcolor('grey')
    for i in range(len(M)):
        #print(i,1)
        for j in range(len(M[0])):
            t.goto(j*taille,i*taille)
            #print(i,j)
            if M[i][j]==1:
                t.color("black")
            else:
                t.color("white")
            t.down()
            t.begin_fill()
            for k in range(4):
                t.forward(taille)
                t.right(90)
            t.end_fill()
            t.up()
    t.ht()
    ts = t.getscreen()
    canvas = ts.getcanvas()
    canvas.postscript(file="QR_Code_2.eps")
    save_as_png(canvas,'QR_Code_2')
    input("Press Enter to close")#   il suffit de faire entré dans la console quand on veut fermer la fenêtre turtle
    t.bye()
#print(a)


def binListe(a):
    "8 donne: [1,0,0,0]"
    L=[]
    while a:
        r = a%2
        a = a//2
        L.append(r)
    L.reverse()
    return(L)

def decList(a):
    L=[]
    while a:
        r = a%10
        a = a//10
        L.append(r)
    L.reverse()
    return(L)


def zero_au_début(L,n):
    #ajoute des zeros au début d'une liste pour qu'elle soit de taille n
    if len(L)>n:
        return(L)
    else:
        M=[]
        for i in range(n-len(L)):
            M.append(0)
        for j in range(len(L)):
            M.append(L[j])
    return(M)

def generate_Id_Clef():
    #val_cle_base_10 est la valeure de la somme des chiffres de l'id
    #clef est la valeure de val_cle_base_10 codée en binaire
    ide = random.randint(0,2**28-1)
    bin_ide = binListe(ide)
    
    digits = decList(ide)
    val_cle_base_10 = sum(digits)
    clef = binListe(val_cle_base_10)
    return(ide,bin_ide,clef,val_cle_base_10)

def generate_qr_avec_id_et_clef():
    ide,bin_ide,clef,clef_base_10 = generate_Id_Clef()
    bin_ide = zero_au_début(bin_ide,28)#on fait en sorte que l'ide (sans la clef) soit codé sur bits
    clef = zero_au_début(clef,7)#on fait en sorte que la clef soit codé sur bits
    qr_code = generate_empty()
    #Assigner ici la clef
    for j in range(7):
        qr_code[12][j]=clef[j]
    # Ci dessous les différentes lignes composant bin_ide
    bin_ide1 = bin_ide[0:7]
    bin_ide2 = bin_ide[7:14]
    bin_ide3 = bin_ide[14:21]
    bin_ide4 = bin_ide[21:28]
    #print(bin_ide1,bin_ide2,bin_ide3,bin_ide3)
    for j in range(7):
        qr_code[8][j]=bin_ide1[j]
        qr_code[9][j]=bin_ide2[j]
        qr_code[10][j]=bin_ide3[j]
        qr_code[11][j]=bin_ide4[j]
    return(np.array(qr_code),clef,ide)
    
    return ide,bin_ide,clef,clef_base_10

def rempli(QR_code,data):#QR_code est le QR code avec Id et clef, data est une liste de longueur 169
    lignes = []#va recueillir data séparé en lignes de longeur 13
    for i in range(13):
        lignes.append(data[13*i:13*(i+1)])
        print(len(lignes))
    for j in range(13):
        ligne = lignes[j]
        for k in range(len(ligne)):
            QR_code[8+j][8+k] = ligne[k]
    return(QR_code)

def read(M):# Prend un qr_code en liste et retourne deta et ide voir quel ordre.
    data =[]
    ide = []
    return(data,ide)



a,clef,ide=generate_qr_avec_id_et_clef()
print(a,ide)
data=[random.randint(0,1) for i in range(169)]
QR_code = rempli(a,data)
print(QR_code)
print(" ")
print(data)
trace(QR_code,10)


