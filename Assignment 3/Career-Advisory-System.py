from durable.lang import *


# used to store the answers to be printed(facts)
answer_list = []

des = "**********************************************************************************************\n"

# function asking whether to go to job sector or research rector
def job_questions():
    print("**********************************************************************************************")
    print("Where does your interest lie?\n")
    print("1. Would you like to enter the research field, where you would research on the unsolved problems?")
    print("2. Would you like to do enter the IT sector and work at a MNC?\n")
    opt = int(input("Choose from the options above: "))
    return opt

# function asking the preference of clubs
def club_questions():
    print("\n**********************************************************************************************")
    print("It is good to take care of your career, but one should take out some time for themselves.")
    print("There are various clubs at IIITD, which could help one to relieve the burden of studies and keep your mind fresh.\n")
    print("So kind of club are you interested in? Here are a few options. Please choose from the options below.\n")
    print("1. Coding")
    print("2. Computer Security")
    print("3. Data Science")
    print("4. Electronics")
    print("5. Entertainment - Singing/Dance/Drama")
    club_opt = int(input("\nEnter the option no of the type of club you'd like to join: "))

    club = ""

    if(club_opt == 1):
        club = "Coding"
    elif(club_opt == 2):
        club = "Computer Security"
    elif(club_opt == 3):
        club = "Data Science"
    elif(club_opt == 4):
        club = "Electronics"
    elif(club_opt == 5):
        club = "Entertainment"

    return club

# RuleSet segregating branches and CGPA, and asserting facts based on them, and branching out to clubs ruleset
with ruleset("Study_Field"):

    # **********************************************************************************************
    #                               Computer Science Study Field
    # **********************************************************************************************

    # CSE best gpa (8 <= CGPA <= 10)
    @when_all((m.branch == 'CSE') & (m.grade >= 8.0) & (m.grade <= 10.0))
    def cse_good_gpa(obj):

        job_opt = job_questions()

        path = ""
        if(job_opt == 1):
            path = "Research"
        elif(job_opt == 2):
            path = "Job"

        club = club_questions()

        advice = "You are good to take 6xx or higher level (difficult) courses.\nYou can take courses such as:\n1. Artificial Intelligence\n2. Machine Learning\n3. Cloud Computing\n4. Computer Vision"

        obj.assert_fact("Career", {"branch" : "CSE", "grade" : 10.0, "field" : path});
        obj.assert_fact("Clubs", {"club_type" : club})
        obj.assert_fact({"subject_suggestion": advice})


    # CSE average gpa (7 <= CGPA < 8)
    @when_all((m.branch == 'CSE') & (m.grade >= 7.0) & (m.grade < 8.0))
    def cse_fair_gpa(obj):

        opt = job_questions()

        path = ""

        if(opt == 1):
            path = "Research"
        elif(opt == 2):
            path = "Job"

        club = club_questions()

        advice = "Try to take 5xx or less, level courses. This would be beneficial for you in improving your CGPA and you could perform good in them as well.\nYou can take courses such as:\n1. Algorithm Design and Analysis\n2. Advanced Biometrics\n3. Modern Algorithm Design\n"

        obj.assert_fact("Career", {"branch" : "CSE", "grade" : 7.5, "field" : path})
        obj.assert_fact("Clubs", {"club_type" : club})
        obj.assert_fact({"subject_suggestion": advice })
        

    # CSE gpa not good (7 < CGPA)
    @when_all((m.branch == 'CSE') & (m.grade <= 7.0))
    def cse_poor_gpa(obj):

        opt = job_questions()

        path = ""

        if(opt == 1):
            path = "Research"
        elif(opt == 2):
            path = "Job"

        club = club_questions()

        advice = "Try to take 4xx or less, level courses. This would be beneficial for you in improving your CGPA and you could perform good in them as well.\nYou can take courses such as:\n1. Data Structures and Algorithms\n2. Operating Systems\n3. Database Management Systems\n"

        obj.assert_fact("Career", {"branch" : "CSE", "grade" : 6.0, "field" : path})
        obj.assert_fact("Clubs", {"club_type" : club})
        obj.assert_fact({"subject_suggestion": advice })


    # **********************************************************************************************
    #                            Electronics and Communication Study Field
    # **********************************************************************************************

    # ECE best gpa (8 <= CGPA <= 10)
    @when_all((m.branch == 'ECE') & (m.grade >= 8.0) & (m.grade <= 10.0))
    def ece_good_gpa(obj):

        opt = job_questions()

        path = ""

        if(opt == 1):
            path = "Research"
        elif(opt == 2):
            path = "Job"

        club = club_questions()

        advice = "You are good to take 6xx or higher level (difficult) courses.\nYou can take courses such as:\n1. Advanced Embedded Logic Design\n2. Memory Design and Testing\n3. Stochastic Estimation and Control\n"

        obj.assert_fact("Career", {"branch" : "ECE", "grade" : 9.0, "field" : path})
        obj.assert_fact("Clubs", {"club_type" : club})
        obj.assert_fact({"subject_suggestion": advice})


    # ECE average gpa (7 <= CGPA < 8)
    @when_all((m.branch == 'ECE') & (m.grade >= 7.0) & (m.grade < 8.0))
    def ece_fair_gpa(obj):

        opt = job_questions()

        path = ""

        if(opt == 1):
            path = "Research"
        elif(opt == 2):
            path = "Job"

        club = club_questions()

        advice = "Try to take 5xx or less, level courses. This would be beneficial for you in improving your CGPA and you could perform good in them as well.\nYou can take courses such as:\n1. Computer Architecture\n2. VLSI Design Flow\n3. Statistical Signal Processing\n"

        obj.assert_fact("Career", {"branch" : "ECE", "grade" : 7.5, "field" : path})
        obj.assert_fact("Clubs", {"club_type" : club})
        obj.assert_fact({"subject_suggestion": advice })
        

    # ECE gpa not good (7 < CGPA)
    @when_all((m.branch == 'ECE') & (m.grade <= 7.0))
    def ece_poor_gpa(obj):

        opt = job_questions()

        path = ""

        if(opt == 1):
            path = "Research"
        elif(opt == 2):
            path = "Job"

        club = club_questions()

        advice = "Try to take 4xx or less, level courses. This would be beneficial for you in improving your CGPA and you could perform good in them as well.\nYou can take courses such as:\n1. Solid State Devices\n2. Digital Communication Systems\n3. Radar Systems\n"

        obj.assert_fact("Career", {"branch" : "ECE", "grade" : 6.0, "field" : path})
        obj.assert_fact("Clubs", {"club_type" : club})
        obj.assert_fact({"subject_suggestion": advice })



    # **********************************************************************************************
    #                            Computational Biology Study Field
    # **********************************************************************************************

    # CB best gpa (8 <= CGPA <= 10)
    @when_all((m.branch == 'CB') & (m.grade >= 8.0) & (m.grade <= 10.0))
    def cb_good_gpa(obj):

        opt = job_questions()

        path = ""

        if(opt == 1):
            path = "Research"
        elif(opt == 2):
            path = "Job"

        club = club_questions()

        advice = "You are good to take 5xx or higher level (difficult) courses.\nYou can take courses such as:\n1. Computing for Medicine\n2. Data Sciences for Genomics\n3. Introduction to Computational Neuroscience\n"

        obj.assert_fact("Career", {"branch" : "CB", "grade" : 9.0, "field" : path})
        obj.assert_fact("Clubs", {"club_type" : club})
        obj.assert_fact({"subject_suggestion": advice})

    # CB average gpa (7 <= CGPA < 8)
    @when_all((m.branch == 'CB') & (m.grade >= 7.0) & (m.grade < 8.0))
    def cb_fair_gpa(obj):

        opt = job_questions()

        path = ""

        if(opt == 1):
            path = "Research"
        elif(opt == 2):
            path = "Job"

        club = club_questions()

        advice = "Try to take 5xx or less, level courses. This would be beneficial for you in improving your CGPA and you could perform good in them as well.\nYou can take courses such as:\n1. Biophysics\n2. Algorithms in Bioinformatics\n3. Practical Bioinformatics\n"

        obj.assert_fact("Career", {"branch" : "CB", "grade" : 7.5, "field" : path})
        obj.assert_fact("Clubs", {"club_type" : club})
        obj.assert_fact({"subject_suggestion": advice })
        

    # CB gpa not good (7 < CGPA)
    @when_all((m.branch == 'CB') & (m.grade <= 7.0))
    def cb_poor_gpa(obj):
        
        opt = job_questions()

        path = ""

        if(opt == 1):
            path = "Research"
        elif(opt == 2):
            path = "Job"

        club = club_questions()

        advice = "Try to take 4xx or less, level courses. This would be beneficial for you in improving your CGPA and you could perform good in them as well.\nYou can take courses such as:\n1. Genetics and Molecular Biology\n2. Introduction to Quantitative Biology\n3. Cell Biology and Bio-Chemistry\n"

        obj.assert_fact("Career", {"branch" : "CB", "grade" : 6.0, "field" : path})
        obj.assert_fact("Clubs", {"club_type" : club})
        obj.assert_fact({"subject_suggestion": advice })

    # **********************************************************************************************
    #                            Generate List of Facts of Courses
    # **********************************************************************************************

    # appending all the facts in the answer_list list.
    @when_all(+m.subject_suggestion)
    def output(obj):
        sp = "                                     "
        answer_list.append('\n{0}{1}COURSE CHOICES\n{2}\n{3}\n'.format(des, sp, des, obj.m.subject_suggestion))



# RuleSet judging the career of the student based on CGPA and choice of job field.
with ruleset("Career"):

    # **********************************************************************************************
    #                                       Research Career
    # **********************************************************************************************

    @when_all((m.grade >= 8.0) & (m.grade <= 10.0) & (m.field == "Research"))
    def good_research(obj):
        obj.assert_fact({"future_plan" : "You really have a great academic record. You should try to pursue higher education and work under professors at IIITD and possibly aim to join big Research companies of your field of study."})

    @when_all((m.grade >= 7.0) & (m.grade < 8.0) & (m.field == "Research"))
    def avg_research(obj):
        obj.assert_fact({"future_plan" : "Your CGPA is currently mediocre for a person who wishes to pursue the side of research, but not so poor. You should try and improve that. Take light courses which would help you improve your CGPA, as mentioned below. Try and work under professors at IIITD and then possibly aim to join big Research companies of your field of study."})

    @when_all((m.grade < 7.0) & (m.field == "Research"))
    def poor_research(obj):
        obj.assert_fact({"future_plan" : "Your CGPA is currently really not upto the mark. Research instituions prefer candidates with CGPA above 8. Try to improve it. Take light courses which would help you improve your CGPA, as mentioned below. Try and work under professors at IIITD and then possibly aim to join big Research companies of your field of study."})


    # **********************************************************************************************
    #                                 Computer Science Job Careers
    # **********************************************************************************************
    @when_all((m.branch == "CSE") & (m.grade >= 8.0) & (m.grade <= 10.0) & (m.field == "Job"))
    def good_job(obj):
        obj.assert_fact({"future_plan" : "You really have a great academic record. You should try improving your competitive programming skills, which could land you in high paying HFT job profiles and product-based companies. "})

    @when_all((m.branch == "CSE") & (m.grade >= 7.0) & (m.grade < 8.0) & (m.field == "Job"))
    def avg_job(obj):
        obj.assert_fact({"future_plan" : "You really have a decent academic record. You should try improving your data structures and algorithms, which could land you in great product-based companies. "})

    @when_all((m.branch == "CSE") & (m.grade < 7.0) & (m.field == "Job"))
    def poor_job(obj):
        obj.assert_fact({"future_plan" : "You don't have a great academic record. You should work really hard in building your profile and improve your CGPA. Improve your DSA skills, and you can aim to crack good product based companies. "})

    # **********************************************************************************************
    #                            Electronics and Communication Job Careers
    # **********************************************************************************************
    @when_all((m.branch == "ECE") & (m.grade >= 8.0) & (m.grade <= 10.0) & (m.field == "Job"))
    def good_job(obj):
        obj.assert_fact({"future_plan" : "You really have a great academic record. You can make your career in niche profiles as a Computer Vision, Signal Processing or a Speech analysis Engineer"})

    @when_all((m.branch == "ECE") & (m.grade >= 7.0) & (m.grade < 8.0) & (m.field == "Job"))
    def avg_job(obj):
        obj.assert_fact({"future_plan" : "You really have a decent academic record. You can make your career as a Silicon Design engineer, Silicon Validation Engineer or a Silicon Verification Engineer"})

    @when_all((m.branch == "ECE") & (m.grade < 7.0) & (m.field == "Job"))
    def poor_job(obj):
        obj.assert_fact({"future_plan" : "You don't have a great academic record. You should try to improve your CGPA. You can make your carrer as a PCB Design Engineer, Testing Engineer, or an Embedded Engineer"})

    # **********************************************************************************************
    #                                Computational Biology Job Careers
    # **********************************************************************************************

    @when_all((m.branch == "CB") & (m.grade >= 8.0) & (m.grade <= 10.0) & (m.field == "Job"))
    def good_job(obj):
        obj.assert_fact({"future_plan" : "You really have a great academic record. You can try to apply for foreign universities and get higher education. You could go for companies abroad as a bioinformatician, or any field of your type."})

    @when_all((m.branch == "CB") & (m.grade >= 7.0) & (m.grade < 8.0) & (m.field == "Job"))
    def avg_job(obj):
        obj.assert_fact({"future_plan" : "You really have a decent academic record. You should prepare aim for good computational biologist companies such as Corteva Agriscience, Cognizant and many more."})

    @when_all((m.branch == "CB") & (m.grade < 7.0) & (m.field == "Job"))
    def poor_job(obj):
        obj.assert_fact({"future_plan" : "You don't have a great academic record. You should work really hard in building your profile and improve your CGPA. Improve your skills, and you may land into a good company as a computational biologist."})


    # **********************************************************************************************
    #                            Generate List of Facts of Careers
    # **********************************************************************************************

    # appending all the facts in the answer_list list.
    @when_all(+m.future_plan)
    def output(obj):
        answer_list.append('Future Plan: {0}'.format(obj.m.future_plan))


# RuleSet suggesting the clubs to the user based in his/her interest.
with ruleset("Clubs"):

    @when_all(m.club_type == "Coding")
    def coding(obj):
        obj.assert_fact({"clubToJoin" : "You can join \"Foobar : The competitive programming club of IIITD.\""})

    @when_all(m.club_type == "Data Science")
    def coding(obj):
        obj.assert_fact({"clubToJoin" : "You can join clubs like BioBytes and Lean"})

    @when_all(m.club_type == "Computer Security")
    def coding(obj):
        obj.assert_fact({"clubToJoin" : "You can join the D4rkcode club of IIITD."})

    @when_all(m.club_type == "Electronics")
    def coding(obj):
        obj.assert_fact({"clubToJoin" : "You can join Electroholics club of IIITD."})

    @when_all(m.club_type == "Entertainment")
    def coding(obj):
        obj.assert_fact({"clubToJoin" : "You can join clubs like Audiobytes, Machaan, Madtoes."})

    @when_all(+m.clubToJoin)
    def output(obj):
        sp = "                                     "
        answer_list.append('\n{0}{1}CLUB CHOICES\n{2}\n{3}\n'.format(des, sp, des, obj.m.clubToJoin))

# **********************************************************************************************
#                                     Main function
# **********************************************************************************************

print("**********************************************************************************************")
print("                      WELCOME TO THE CAREER ADVISORY SYSTEM")
print("**********************************************************************************************\n")

print("This career advisory system will suggest you various courses based on your interests and aptitude")
print('and also will suggest you possible and good future career choices.\n')

print("Let us begin.\n")
print("Firstly, we will ask you some basic questions regarding your background.\n")


name = input("Enter your name: ")
print()
print("**********************************************************************************************")
print("Here are the Course Branches at IIITD\n")
print("1. Computer Science Engineering")
print("2. Electronics and Communication Engineering")
print("3. Computational Biology\n")

branch = int(input("Enter the option no. of your branch of study at IIITD from the above options: "))
print()
cgpa = float(input("Enter your cumulative grade point till now (CGPA): "))
print()
name_branch = ""

if(branch == 1):
    name_branch = "CSE"
elif(branch == 2):
    name_branch = "ECE"
elif(branch == 3):
    name_branch = "CB"


# asserting the initial fact.
assert_fact("Study_Field", {"branch": name_branch, "grade": cgpa})

print()
print("**********************************************************************************************")
print("                                FUTURE CAREER SUGGESTIONS")
print("**********************************************************************************************\n")
print("Hi {0}. Here are the suggestions for you which we assessed based upon your answers.\n".format(name))

for i in answer_list:
    print(i)
