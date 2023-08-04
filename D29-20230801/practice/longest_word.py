sentence=input("enter the sentence: ")
# def longest(sentence):
#     words=sentence.split()
#     longest=0
#     longest_word=""
    
#     for word in words:
#         if len(word)>longest:
#             longest=len(word)
#             longest_word=word
#     return "The longest word is: ",longest_word
# print(longest(sentence))

def longest(sentence):
    words = []  
    word = ""

    for i in sentence:
        if i != " ":  
            word += i 
        else:
            words+=[word]
            word = ""  
    
    words+=[word] 

    longest = 0
    longest_word = ""
    
    for word in words:
        length=0
        if length>longest:
            longest=length
        longest_word=word
    return "The longest word is : ",longest_word
print(longest(sentence))

