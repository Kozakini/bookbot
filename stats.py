def number_of_words(text):
    split_text = text.split()
    return len(split_text)
def sort_on(items):
    return items['num']
def number_of_letters(text):
    letters = {}
    lista=[]
    for c in text:
        lowered = c.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    for letter in letters:
            count = letters[letter]
            lista.append({'name':letter,'num':count})
    lista.sort(reverse=True,key=sort_on)
    for i in lista:
        print(f"{i['name']}: {i['num']}")
