import re


#patterns = ['term1','term2']
#text = 'term1'

#for pattern in patterns:
    #print("I am searching for:"+pattern)
    
    
#match = re.search('term1',text)
#print(match.start())   

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')
        
#test_phrase = 'sdsd..sssdddd..sdddsddd..dsds...dssssss...sdddddd'
#test_phrase = "This is a string ! But it has punctuation. How can we remove that"
test_phrase = "This is the string with number 123412 and a symbol #hashtag"

#test_patterns = ['s[sd]+']
#test_patterns = ['[^!.?]+']
test_patterns = [r'\d+']
multi_re_find(test_patterns,test_phrase)
        