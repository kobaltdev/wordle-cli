import wordle_functions

dico = "dicos/dico_test.txt"
dict_to_work_with = wordle_functions.set_file_path(dico)
wordle_functions.pick_word_from_list(dict_to_work_with)

