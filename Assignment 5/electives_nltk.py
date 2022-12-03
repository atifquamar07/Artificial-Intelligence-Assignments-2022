import nltk
from pyswip import Prolog
from nltk.stem import PorterStemmer

# decides which branch the user belongs to
def tellBranch(sentence):
    
    branch = ""
    for w in sentence:
        if(ps.stem(w) == ps.stem('engineering') or ps.stem(w) == ps.stem('cse')):
            branch = 'CSE'
        if(ps.stem(w) == ps.stem('artificial') or ps.stem(w) == ps.stem('ai')):
            branch = 'CSAI'
        if(ps.stem(w) == ps.stem('mathematics') or ps.stem(w) == ps.stem('math')):
            branch = 'CSAM'
        if(ps.stem(w) == ps.stem('biosciences') or ps.stem(w) == ps.stem('biology') or ps.stem(w) == ps.stem('bio')):
            branch = 'CSB'
        if(ps.stem(w) == ps.stem('design') or ps.stem(w) == ps.stem('des')):
            branch = 'CSD'
        if(ps.stem(w) == ps.stem('electronics') or ps.stem(w) == ps.stem('communication') or ps.stem(w) == ps.stem('ece')):
            branch = 'ECE'
            
    return branch
    
# determines the branch of subject the user wants to study
def tellSubjectBranch(sentence):
    
    subs = ''
    for w in sentence:
        if(ps.stem(w) == ps.stem('artificial') or ps.stem(w) == ps.stem('ai') or ps.stem(w) == ps.stem('machine')):
            subs = 'Artificial Intelligence/Machine Learning'
        if(ps.stem(w) == ps.stem('mathematics') or ps.stem(w) == ps.stem('math')):
            subs = 'Applied Mathematics'
        if(ps.stem(w) == ps.stem('biosciences') or ps.stem(w) == ps.stem('biology') or ps.stem(w) == ps.stem('bio')):
            subs = 'BioSciences'
        if(ps.stem(w) == ps.stem('design') or ps.stem(w) == ps.stem('des')):
            subs = 'Design'
        if(ps.stem(w) == ps.stem('electronics') or ps.stem(w) == ps.stem('communication') or ps.stem(w) == ps.stem('ece')):
            subs = 'Electronics' 
            
    return subs


# determines the the courses the student wants to study
def fieldOfStudy(sentence):
    
    fields = []
    for w in sentence:
        
        # MACHINE LEARNING
        if(ps.stem(w) == ps.stem('machine') or ps.stem(w) == ps.stem('ml')):
            fields.append("ML")
        # NATURAL LANGUAGE PROCESSING
        elif(ps.stem(w) == ps.stem('language') or ps.stem(w) == ps.stem('nlp')):
            fields.append("NLP")
        # INTRODUCTION TO COMPUTATIONAL NEUROSCIENCE
        elif(ps.stem(w) == ps.stem('neuroscience') or ps.stem(w) == ps.stem('neuro')):
            fields.append("ICN")
        # COMBINATORICS AND ITS APPLICATIONS
        elif(ps.stem(w) == ps.stem('combinatorics') or ps.stem(w) == ps.stem('permutation')):
            fields.append("CIA")
        # CALCULUS IN R(n)
        elif(ps.stem(w) == ps.stem('calculus') or ps.stem(w) == ps.stem('integration') or ps.stem(w) == ps.stem('differentiation')):
            fields.append("CRN")
        # DIGITAL VLSI DESIGN
        elif(ps.stem(w) == ps.stem('chips') or ps.stem(w) == ps.stem('microelectronics') or ps.stem(w) == ps.stem('vlsi')):
            fields.append("DVD")
        # INTRODUCTION TO BLOCKCHAIN AND CRYPTOGRAPHY
        elif(ps.stem(w) == ps.stem('blockchain') or ps.stem(w) == ps.stem('cryptography') or ps.stem(w) == ps.stem('cryptocurrency')):
            fields.append("IBC")
        # DIGITAL IMAGE PROCESSING
        elif(ps.stem(w) == ps.stem('image') or ps.stem(w) == ps.stem("dip")):
            fields.append("DIP")
        
            
    return fields


# Main function
print("********************************************************************************************************************")
print('                                 WELCOME TO ELECTIVES ADVISORY SYSTEM (NL INTERFACE)')
print("********************************************************************************************************************")

print('This electives advisory system will suggest you various courses based on your interests and aptitude')
print('and also will suggest you possible and good future career choices.')

print('Let us begin')
print('Firstly, we will ask you some basic questions regarding your background.')


ps = PorterStemmer()

name = input("What is your name? : ")
print("\nHi {0}, Hope that we can be of help to you.\n".format(name))

inp = input("Tell us about your branch of study here at IIITD, the branch of study you want to explore, and your specific area of interest in that branch?\n\n")

# changing all the words to lowercase
inp = inp.lower()

# breaking down the paragraph into a list of sentences.
chunks = nltk.sent_tokenize(inp)

# Here we are going to make an assumption that the information about the user's branch would be in the first sentence,
# the branch of engineering the user wants to explore would be in the second line, and the specific interest of the user
# in a particular field (e.g:- Machine Learning, VLSI Design, etc.) would be in the third sentence.

# storing branch of the user
words1 = nltk.word_tokenize(chunks[0])
branch = tellBranch(words1)

# storing the branch, whose related courses the user's wants to do 
words2 = nltk.word_tokenize(chunks[1])
branch_related_courses = tellSubjectBranch(words2)

# storing the fields of study the user wants to explore.
words3 = nltk.word_tokenize(chunks[2])
fields = fieldOfStudy(words3)

# consulting the electives information from the eletives.pl Prolog file
prolog = Prolog()
prolog.consult("electives.pl")

for course in fields:
    prolog.assertz("take('{0}')".format(course))
    
# recommending the courses
print("\n********************************************************************************************************************")
print("                                 RECOMMENDED COURSES FOR YOU")
print("********************************************************************************************************************\n")
print("{0} is a really good branch to pursue here at IIITD. We see that you want to pursue courses from the {1} branch.\n".format(branch, branch_related_courses))
print("We have compiled a list of courses for you, which you can take in your stay here at IIITD.")
print("Details of the courses along with their code and names are given below.\n\n")


answer = list(prolog.query("main"))

