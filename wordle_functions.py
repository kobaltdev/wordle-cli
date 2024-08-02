import random
import os


def set_file_path(filename: str):
    # Path du dossier de travail
    directory = os.path.dirname(__file__)
    # contruction du chemin de fichier complet
    file_to_compute = os.path.join(directory, filename)
    return file_to_compute


def pick_word_from_list(word_list_txt_file: str) -> list:
    
    with open(word_list_txt_file, 'r') as wordlist_txt:
        content = wordlist_txt.read()
        wlist = content.split("\n")

        rand = random.randint(0, len(wlist)-1)
        randomWord = wlist[rand].lower()
        print("mot choisi : ", randomWord)
        
        


