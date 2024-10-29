def process_sentence(sentence):
    white_space = 0
    check = False
    sentence = input ("Enter your sentence: ")
    for alphabet in sentence:
        if alphabet == " ":
            white_space +=1
    if "python" in sentence:
        check = bool(sentence.lower())
    new_sentence = sentence.replace("Javascript", "Python")
    print (f"{new_sentence.lower()}, {check}, {white_space}")


process_sentence(str)








