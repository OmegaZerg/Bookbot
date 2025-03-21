#Define stat functions for main
def get_words(string):
    words = []
    words = string.split()
    return len(words)

def char_count(string):
    characters = {}
    for char in string:
        if char.lower() in characters:
            characters[char.lower()] +=1
        elif char.lower() not in characters:
            characters[char.lower()] = 1
    return characters

def sort_on(dic):
    return dic['Count']

def char_sort(dictionary):
    list = []
    for pair in dictionary:
        dic = {'Character': pair, 'Count': dictionary[pair]}
        list.append(dic)
        list.sort(reverse=True, key=sort_on)
    return list