from tkinter import *
import os

# Bug à corriger
class MyApp:

    def __init__(self):
        
        self.color = '#64FFB1'  # Vert

        # Utile
        self.chiffre = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.lettre = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                       "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"
                       "u", "v", "w", "x", "y", "z")

        # Dictionnaire permettant de traduire
        self.atbash = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q",
                       "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g",
                       "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}

        self.caesar = {"a": "x", "b": "y", "c": "z", "d": "a", "e": "b", "f": "c", "g": "d", "h": "e", "i": "f",
                       "j": "g", "k": "h", "l": "i", "m": "j", "n": "k", "o": "l", "p": "m", "q": "n", "r": "o",
                       "s": "p", "t": "q", "u": "r", "v": "s", "w": "t", "x": "u", "y": "v", "z": "w"}

        self.a1z26 = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i",
                      "10": "j", "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", "16": "p", "17": "q", "18": "r",
                      "19": "s", "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", "25": "y", "26": "z"}
        
        # Configuration de la page
        self.window = Tk()
        
        self.window.title("Cryptogramme")
        self.window.geometry("825x150")
	if os.path.exists("img/language.ico"):
        	self.window.iconbitmap("img/language.ico")
        self.window.resizable(0, 0)
        self.window.config(background=self.color)
         
        # initialisation des composants
        self.frame = Frame(self.window, bg=self.color)
         
        # creation des composants
        self.create_widgets()
         
        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        """
        Cette procédure crée les widgets de la page.
        """
        self.create_menu()
        self.create_title()
        self.create_entry()
    
    def create_menu(self):
        """
        Cette procédure crée une barre de menu avec 2 lignes:
        - Traducteur : Atbash, Caesar, A1Z26
        - Option : Supprimer, Fermer
        """
        # Création de la barre de menu
        self.mainmenu = Menu(self.window)
        
        # Première ligne du menu : Traducteur
        self.first_menu = Menu(self.mainmenu, tearoff=0)
        self.first_menu.add_command(label="Atbash", command=lambda: self.button_activate(self.atbash))
        self.first_menu.add_command(label="Caesar", command=lambda: self.button_activate(self.caesar))
        self.first_menu.add_command(label="A1Z26", command=self.a1z26_activate)
        
        # Seconde ligne du menu : Options
        self.second_menu = Menu(self.mainmenu, tearoff=0)
        self.second_menu.add_command(label="Supprimer", command=self.delete)
        self.second_menu.add_command(label="Fermer", command=quit)
        
        self.mainmenu.add_cascade(label="Traducteur", menu=self.first_menu)
        self.mainmenu.add_cascade(label="Option", menu=self.second_menu)
    
    def create_title(self):
        """
        Cette procédure créant un label
        """
        self.titre = Label(self.frame, text="Message :", font=("Courrier", 35), bg=self.color, fg="white")
        self.titre.pack(side=LEFT)
        
    def create_entry(self):
        """
        Cette procédure créant une entry
        """
        self.entry = Entry(self.frame, font=("Helvica", 40), bg=self.color, fg="white")  # fg en blanc pour disserner
        self.entry.pack()
        
    def convert(self, phrase: list, translate: dict) -> str:
        """
        Cette fonction convertit les caractères

        param phrase: list phrase coupé mot par mot
        param translate: dict Utilisé pour traduire la liste
        return: str res
        """

        res = ""

        for mot in phrase:
            for lettre in mot:
                # Si lettre n'est pas dans translate
                try:
                    res += translate[lettre]
                except:
                    res += self.correct_error(lettre, translate)

            # On met un esapace pour séparer les mots
            res += " "
        
        return res.rstrip()

    def a1z26_convert(self, phrase): # Cette fonction doit être corriger

        res = ""

        for mot in phrase:

            mot = mot.split("-")

            for lettre in mot:
                try:
                    res += self.a1z26[lettre]
                except:
                    res += self.correct_error(lettre, self.a1z26)

            # On met un esapace pour séparer les mots
            res += " "

        return res.rstrip()

    def correct_error(self, lettre: str, translate: dict) -> str:
        """
        Cette fonction s'active si une erreur est faite.
        Pour éviter les msg d'erreur on utilise cette fonction.

        param lettre: le message a traduire
        param translate: dictionnaire permettant la traduction
        return: str res
        """
        res = ""

        for i in lettre:
            if i in self.lettre or i in self.chiffre:
                res += translate[i]
            else:
                res += i

        return res

    def delete(self, msg=""):
        """
        Cette procédure supprime le contenu de self.entry
        et peut également inserré un message à l'intérieur

        param msg: Rempli le self.entry
        """
        self.entry.delete(0, END)

        if not msg == "":
            self.entry.insert(0, msg)

    def button_activate(self, translate):
        """
        Cette procédure sert à traduire le param message grâce au param translate.
        C'est celle qui s'active quand on appuie sur un des boutons de la 1er ligne du menu. Elle utilise les
        autres fonctions et procédures se trouvant au dessus d'elle.
        Utilisé uniquement pour Caesar et Atbash

        param translate : dict contenant la traduction de chaque caractère en celui le correspondant
        """
        # Cette simple ligne est la traduction de toute la phrase
        message = self.convert(self.entry.get().lower().split(" "), translate)
        self.delete(message)

    def a1z26_activate(self):
        """
        Cette procédure sert à traduire les messages crypté en A1Z26.
        """
        message = self.a1z26_convert(self.entry.get().split(" "))
        self.delete(message)
