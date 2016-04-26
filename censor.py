def censor(text, word):
    out = ""
    for i in text.split():
        if i == word:
            out += ("*" * len(word)) + " "
        else:
            out += i + " "
    return out[0:-1]

text = input("Enter phrase: ")
word = input('Enter word to censor: ')

print(censor(text,word))



def censorRF(text,word):
text=text.replace(word,"*" * len(word))
return text
