n = int(input(""))
words = []
for i in range(n): # loop through each number of number of words and append input to list
    words.append(input("")) # append to list

#NOW we have list of words #for exaple our list look like this ["word", "information", "fdgjnsdfgjshfgklsdjlkgjdklfg"]
    #let's check if this words lenghth > 10 or < 10

 
def shortcuts(n, words): #2 variables number of words and what words
    outputList = [] #in this list we are going to append all results
    for i in range(n): # how many words is going to appear 
        if len(words[i]) > 10: #if length of word[number of word in list bigger than 10
            outputList.append(words[i][0] + str(len(words[i])-2) + words[i][-1]) # add to list word number first
        else:
            outputList.append(words[i]) #if word's lenght < 10 character 
    for i in outputList:
        print(i)
shortcuts(n, words)