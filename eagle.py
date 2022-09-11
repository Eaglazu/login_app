#!/usr/bin/python3

from tkinter import *
import os 

#############fenetre###############


#fenetre
root = Tk()
root.geometry("800x600")
root.title("Eagle's")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)

#logo fenetre
root.config(background="#291666")

logo=Canvas(root,width=800,height=600,bg="#291666")
logo.place(x=0,y=0)

#################interface conexion#####################

identifiant=Label(logo,text="pseudo",bg="#291666",font=('arial',15,'bold'),fg="#fff")
identifiant.place(x=365,y=100)

mdp=Label(logo,text="Mot de passe",bg="#291666",font=('arial',15))
mdp.place(x=338,y=215)

identifiantEntry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
identifiantEntry.place(x=175,y=150)

mdpEntry=Entry(logo,width=50,show='*',relief=FLAT,font=('arial',12))
mdpEntry.place(x=175,y=250)
###################fin de l'interface##################
##################"CONNEXION"#######################
def new_code():
    nom_new = identifiantEntry.get()
    pass_new = mdpEntry.get()
    File_new_name = os.listdir()
    if str(nom_new) + ".txt" in File_new_name : 
        print("le nom est déja pris")
    else:
        File = open(str(nom_new)+".txt","w")
        File.write(str(nom_new)+":"+str(pass_new))
        File.close
        
def login_code():
    nom_login = identifiantEntry.get()
    pass_login = mdpEntry.get()
    File_login_name = os.listdir()
    if str(nom_login) + ".txt" in File_login_name :
        File1 = open(str(nom_login)+ ".txt","r")
        liste_info_login = File1.read().split(":")
        File1.close
        if pass_login == liste_info_login[1] :
            print("bienvenue")
            page2=Canvas(logo,width=800,height=600,bg="#291666")
            page2.place(x=0,y=0)
            bvn =Label(page2,text="Bienvenue",bg="#291666",font=('arial',15,'bold'),fg="white")
            bvn.place(x=220, y=400)
        else:
            print("incorect")
            errorlog=Label(logo,text="identifiant ou mot de passe incorrect",bg="#291666",font=('arial',15,'bold'),fg="red")
            errorlog.place(x=220,y=275)
    else:
        print("erreur identifiant inconnue")
        errorlog=Label(logo,text="identifiant ou mot de passe incorrect",bg="#291666",font=('arial',15,'bold'),fg="red")
        errorlog.place(x=220,y=275)

connexion=Button(logo,text="Se connecter",bg="green",fg="white",relief=FLAT,font=('arial',12),width=20,command=login_code)
connexion.place(x=295,y=345)
new=Button(logo,text="inscription",bg="green",fg="white",relief=FLAT,font=('arial',12),width=20,command=new_code)
new.place(x=295,y=400)
####################fin de connexion###############
root.mainloop()
