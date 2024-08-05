def file_list_txt_to_lowercase(filepath_abs: str):
    content_lower = []

    with open(filepath_abs, 'r') as f:
        content = f.readlines()

    for c in content:
        content_lower.append(c.lower())

    with open(filepath_abs, 'w') as f:
        for c in content_lower:
            f.write(c)


def clean_blank_spaces_in_file(filepath_abs: str):

    with open(filepath_abs, 'r') as f:
        content = f.readlines()
 
    for i in range(len(content)):
        content[i] = content[i].lstrip()

    with open(filepath_abs, 'w') as f:
        for c in content:
            f.write(c)


def clean_file(filepath_abs: str):
    newcontent = []

    with open(filepath_abs, 'r') as f:
        content = f.readlines()

    for i in range(len(content)):
        c = content[i].split(" :")
        newcontent.append(c[0] + "\n")
    
    with open(filepath_abs, 'w') as f:
        for c in newcontent:
            f.write(c)


