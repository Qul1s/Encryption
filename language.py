def is_English(text):
    text = text.lower()
    if text.find('a') != -1 or text.find('b') != -1 or text.find('c') != -1 or text.find('d') != -1 or text.find('f') != -1 or text.find('g') != -1 or text.find('p') != -1 or text.find('i') != -1 or text.find('j') != -1 or text.find('k') != -1 or text.find('l') != -1 or text.find('m') != -1 or text.find('n') != -1 or text.find('o') != -1 or text.find('p') != -1 or text.find('q') != -1 or text.find('r') != -1 or text.find('s') != -1 or text.find('t') != -1 or text.find('u') != -1 or text.find('v') != -1 or text.find('w') != -1 or text.find('x') != -1 or text.find('y') != -1 or text.find('z') != -1:
        return True
    else:
        return False

def is_Russian(text):
    text = text.lower()
    if text.find('а') != -1 or text.find('б') != -1 or text.find('в') != -1 or text.find('г') != -1 or text.find('д') != -1 or text.find('е') != -1 or text.find('ё') != -1 or text.find('ж') != -1 or text.find('з') != -1 or text.find('и') != -1 or text.find('й') != -1 or text.find('к') != -1 or text.find('л') != -1 or text.find('м') != -1 or text.find('н') != -1 or text.find('о') != -1 or text.find('п') != -1 or text.find('р') != -1 or text.find('с') != -1 or text.find('т') != -1 or text.find('у') != -1 or text.find('ф') != -1 or text.find('х') != -1 or text.find('ц') != -1 or text.find('ч') != -1 or text.find('ш') != -1 or text.find('щ') != -1 or text.find('ъ') != -1 or text.find('ы') != -1 or text.find('ь') != -1 or text.find('э') != -1 or text.find('ю') != -1 or text.find('я') != -1:
        return True
    else:
        return False


##print("Введите что-нибудь, чтобы проверить язык: ")
##text = input()
##print(is_Russian(text))
##print(is_English(text))