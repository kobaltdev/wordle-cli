import random
import os
from colorama import Fore, Back, Style
import time


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


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
        rand_word = wlist[rand].lower()
    
    return rand_word


def compare_words(word1: str, word2: str) -> bool:
    # convert words to lists
    w1 = [x for x in word1]
    w2 = [x for x in word2]

    for i in range(len(w1)):
        if w2[i] == w1[i]:
            print(Back.GREEN + w2[i].upper(), end='')
            print(Style.RESET_ALL + ' ', end='')
        else:
            if w2[i] in word1:
                print(Back.YELLOW + w2[i].upper(), end='')
                print(Style.RESET_ALL + ' ', end='')
            else:
                print(Style.RESET_ALL + w2[i].upper(), end='')
                print(Style.RESET_ALL + ' ', end='')
    print(Style.RESET_ALL)
    time.sleep(0.2)

    if w2 == w1:
        return True
    return False


def check_if_answer_length_is_ok(word_to_find: str, answer: str) -> bool:
    if len(answer) ==  len(word_to_find):
        return True
    if len(answer) < len(word_to_find):
        print(f"Le mot saisi est trop court ! (rappel : le mot à trouver fait {len(word_to_find)} caractères)\n")
        return False
    if len(answer) > len(word_to_find):
        print(f"Le mot saisi est trop long ! (rappel : le mot à trouver fait {len(word_to_find)} caractères)\n")
        return False
    

def play_wordle(tries: int, word_to_find: str):
    win = False
    print(f"C'est parti, le mot à trouver fait {len(word_to_find)} caractères !\n")

    while tries > 0:
        print()
        print("Essai(s) restant(s) :", tries, '\n')
        answer = input("Votre proposition ? : ")
        print()
        print("Analyse ...\n")
        time.sleep(1)
        if check_if_answer_length_is_ok(word_to_find, answer):
            if compare_words(word_to_find, answer):
                print()
                print("Bravo, vous avez trouvé le mot !")
                win = True
                break
            else:
                tries -= 1
    if win == False:
        print()
        print("Perdu !\n")
        print("Le mot à trouver était :", word_to_find)

        





