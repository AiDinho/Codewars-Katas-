######jUmble up words#####
import random
import re

def change(word):
    returned=word
    return_flag=True
    if len(word)>3:
        while(return_flag):
            if(word[-1] in '[a-z]'):
                returned=word[0]+''.join(random.sample(word[1:-1], len(word[1:-1])))+word[-1]
            elif(len(word[:-1])<=3):
                returned=word
                return_flag=False
            else:
                returned=word[0]+''.join(random.sample(word[1:-2],len(word[1:-2])))+word[-2]+word[-1]
            if (returned!=word):
                return_flag=False
                
        return returned
    else:
        return returned
def mix_words(string):
    try:
        
        #words= re.findall(r"[\w',!;]+$",string)
        #words= re.findall(r"[\w']+",string)
        words=string.split(' ')
        #print words
    
        return ' '.join(map(change,words))
    except AttributeError:
        return "undefined"
        
if __name__=="__main__":
    print mix_words("hello, Pippi!")
    print mix_words("hello") 
    print mix_words("hello Pippi")
    print mix_words("Hi")
    print mix_words("Hey?")
