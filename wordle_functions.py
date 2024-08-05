import random
import os
from colorama import Back, Style
import time


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def set_file_path(filename: str):
    # Path du dossier de travail
    directory = os.path.dirname(__file__)
    # contruction du chemin de fichier complet
    file_to_compute = os.path.join(directory, filename)
    return file_to_compute


def pick_word_from_list(word_list : list) -> list:

    rand = random.randint(0, len(word_list)-1)
    rand_word = word_list[rand].lower()
    
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
        print("Essai(s) restant(s) :", tries, '\n')
        answer = input("Votre proposition ? : ").lower()
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


        
def choose_theme() -> str:
    theme_file = ""
    print("1 - Animaux")
    print("2 - Corps humain")
    print("3 - Cuisine")
    print("4 - Geographie française")
    print("5 - Métiers")
    print("6 - Verbes français")
    print()
    while theme_file == "":
        answer_theme = input("votre choix ? : ")
        match answer_theme:
            case "1":
                theme_file = "dicos/animaux.txt"
            case "2":
                theme_file = "dicos/corps_humain.txt"
            case "3":
                theme_file = "dicos/cuisine.txt"
            case "4":
                theme_file = "dicos/geo_fr.txt"
            case "5":
                theme_file = "dicos/metiers.txt"
            case "6":
                theme_file = "dicos/verbes_fr.txt"
            case _:
                print("Choisissez un thème valide !")
                time.sleep(1)
    return theme_file


def choose_diffulty() -> int:
    difficulty = ""
    cls()
    print("Ok, choisissez le niveau difficulté : \n")
    print("1 - Facile      (mots de 1 à 5 lettres)")
    print("2 - Moyenne     (mots de 6 à 8 lettres)")
    print("3 - Difficile   (mots de 9 lettres et plus)\n")
    while difficulty == "":
        answer_dif = input("votre choix ? : ")
        match answer_dif:
            case "1":
                difficulty = 1
            case "2":
                difficulty = 2
            case "3":
                difficulty = 3
            case _:
                print("Votre choix n'est pas valide !")
                time.sleep(1)
    return difficulty


def generate_wordlist(theme, difficulty) -> list:
    abs_path_for_wordlist = set_file_path(theme)
    min = 0
    max = 0
    if difficulty == 1:
        min = 1
        max = 5
    elif difficulty == 2:
        min = 6
        max = 8
    else:
        min = 9
        max = 99

    with open(abs_path_for_wordlist, 'r') as f:
        content = f.read()
        full_list = content.split("\n")
    
    custom_list = [x for x in full_list if len(x) >= min and len(x) <= max]
    return custom_list


def start_wordle():
    cls()
    print("* * * * * * * * * * * * * *")
    print("        W O R D L E        ")
    print("* * * * * * * * * * * * * *\n")
    print("Bienvenue, avec quel thème voulez vous jouer ? :")
    theme_file = choose_theme()
    difficulty = choose_diffulty()
    customized_wordlist = generate_wordlist(theme_file, difficulty)
    word_to_find = pick_word_from_list(customized_wordlist)
    cls()
    play_wordle(7, word_to_find)
