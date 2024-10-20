import string
def text_process(file):
    #step01: text reading
    with open(file) as files:
        text = files.read()
        print(text.rstrip())
    #step02:
    #remove punctuation
    text_no_pun = text.translate(str.maketrans('', '' , string.punctuation))
    print("The text with no punctuation",text_no_pun)
    #step03:character counting
    char_cou ={}
    for chara in text_no_pun:
        if chara != ' ':
            char_cou[chara] = char_cou.get(chara ,0)+1
    print("The character count in the text",char_cou)
    #step04:word counting
    word_count ={}
    wordscal = text_no_pun.lower().split()
    for words in wordscal:
        word_count[words]=word_count.get(words,0)+1
    print("The word count in text",word_count)
    #step05:delete high freq word
    if word_count:
        max_word = max(word_count, key=word_count.get)  
        del word_count[max_word] 
    print(f"The most frequent '{max_word}' deleted")

text_process('poem.txt')
#Text processing helps in analyzing and understanding large amounts of text data.
# It can be used in chatbots to understand user queries and provide relevant responses.


