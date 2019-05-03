#This program is a prototype for 1st layer abstraction of EO query searching by Abishek Seshan
#Input the query in the form of a simple phrase without spelling mistakes
#This sample code DOESN'T take date and time into account, since this is just a prototype.

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer

#All the functions defined here:

def process_content(sentence): #For tagging of the words in the query
    tagged = nltk.pos_tag(sentence)
    #chunkgram = r"""Chunk: {<NNP>+<CD>*?}"""
    #parser = nltk.RegexpParser(chunkgram)
    #chunked = parser.parse(tagged)
    return tagged

#Data List defined here.

#Make a list of possible types of data that can be extracted. 
datatype = ['videos','records','signals', 'photos', 'pictures', 'images']

#Satellite types:
satellites = [' Sentinel 2', ' TanSat', ' Theos', ' Gaofen 1', ' BelKA']

#Location types:
locations = [' Mount Everest', ' Mt . Everest', 'Africa',' Amazon', ' Kanchenjunga']

#MAIN code starts here

#Inputing the query 
query = input("Enter your query: ") 

qcopy = query #Making a copy of the query

tokenized = word_tokenize(qcopy) #Tokenized sentence

outss = process_content(tokenized) #Set of tagged and processed words
#print(outss)

named_objects = [] #List of named objects in the query.

for i in range(len(outss)-1): 
    if outss[i][1] == 'IN':
        string = ''
        for j in range(i+1,len(outss)):
            if outss[j][1]!= 'IN':
               string = string + ' ' + outss[j][0]
            else:
               break 
        named_objects.append(string) 

for i in range(len(outss)-1):
    if outss[i][1] == 'NNP':
        string = ''
        string = string + ' ' + outss[i][0]
        for j in range(i+1,len(outss)):
            if outss[j][1] == 'NNP' or outss[j][1] == 'CD':
                string = string + ' ' + outss[j][0] 
            else:
                break 
        if string not in named_objects:
            named_objects.append(string)


print("The named objects found in the query are: {}".format(named_objects))

type_of_object = [] #To find the type of object wanted from the query 

for i in range(len(outss)):
    if outss[i][1] == 'NNS' or outss[i][1] == 'NN':
        type_of_object.append(outss[i][0]) 

 
ls = LancasterStemmer()

#print("Your query was: {}".format(query)) 

for i in datatype:
    for j in type_of_object:
        if ls.stem(i.lower()) == ls.stem(j.lower()):
            finaltype = i
            print("You want : {}".format(finaltype))
            break

for i in satellites:
    for j in named_objects:
        if i.lower() == j.lower():
            print("You want {} from: {}".format(finaltype,i))
            break 

for i in locations:
    for j in named_objects:
        if i.lower() == j.lower():
            print("You want {} of: {}".format(finaltype,i))
            break




     




