# IMPORTS
import wordle_functions


# MAIN

dico = "dicos/metiers.txt"

dict_to_work_with = wordle_functions.set_file_path(dico)
word_from_list = wordle_functions.pick_word_from_list(dict_to_work_with)


wordle_functions.play_wordle(tries=7, word_to_find=word_from_list)


