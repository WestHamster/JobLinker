import textract
import threading
import re
import string
import pandas as pd
import time
import random


def _test():

    print('\nBefore asking you some questions, we like to know more about you!')

    print('\nAre you a student? (eg:Yes or No, Y/N, y/n)')
    stud_input = input("Your Answer:")

    if stud_input.lower() in ['no','n']:
        print('\n\nWhich work location do you prefer? (eg: Bangalore, Hyderabad,etc)')
        place_inp = input("Your Answer:")

        print('\nHow many years of work exp. do you have? (eg: 1,1.5,0.5,etc)')
        exp_inp = float(input("Your Answer:"))

        print('\nAny preferable work position you\'re looking for? (eg: SDE-1,SDE 2, Data Analyst,ML Engineer,etc)')
        pos_input = input("Your Answer:")

        print('\nCompanies you\'ve worked for from latest to previous? (eg: Amazon,Google,Goldman Sachs,etc)')
        exp_inp = input("Your Answer:")

        print('\nPurpose of Change. (eg: Not paid well, no development in career, bad work environment)')
        purpose_input = input("Your Answer:")

        print('\nWe\'re almost there! Just bear with me for some more time :)')

        print('\nAny prefered company? (\n1: MNC, \n2.Mid-size firm \n3.Consultancy based firm \n4.Startup)')
        pref_company = int(input("Your Answer:"))

    elif stud_input.lower() in ['yes','y']:
        print('\nEducation Level? (eg: btech,mtech,ms,bs, etc.)')
        edu_input = input("Your Answer:")

        print('\nGraduation Year? (eg: 2015,2019,2017, etc.)')
        grad_input = input("Your Answer:")

        print('\nLanguages known by you? (eg: C++,C,Python,etc.)')
        lang_input = input("Your Answer:")

        print('\nDo you contribute to Open Source? If yes, we would love to know which places have you contributed else NA (eg: added fetching extension to firefox,na, etc.)')
        opens_input=input("Your Answer:")

        print('\nAny experience in internship? If yes, please write number of years else \'NA\' (eg: 1,0.3,na,NA)')
        intern_exp = input("Your Answer:")

    else:
        print('\n\nC\'mon man don\'t start off in a wrong way, you got it!' )
        print('\n\nNow TRY AGAIN\n')
        _test()

    print('\n\nYou did pretty well up there! Now let\'s see how quick you can think.')
    print('\nWhile attempting the question, be careful that your time is being recorded by us in order to judge you!')
    print('\nAll the best!!\n\n')



    question_dict = {'There are 3 ants sitting on three corners of a triangle.All ants randomly pick a direction and start moving along edge of the triangle. What is the probability that any two ants collide?':0.25,
    'On selling 17 balls at Rs. 720, there is a loss equal to the cost price of 5 balls. The cost price of a ball is:': 60,
    'A person\'s present age is two-fifth of the age of his mother. After 8 years, he will be one-half of the age of his mother. How old is the mother at present?': 40}

    print("\n\n")
    print('Your 1st question for the day is: \n')
    start = time.time()
    print(random.choice(list(question_dict)))
    print()
    answer1_input = float(input("Enter your answer: "))
    end = time.time()

    res1 = end-start
    print(f'\nYour result was recieved in {res1} seconds')

    return res1


def _resume(options_available):
    print("\n\n\t So there are few steps while uploading the resume. Please follow the steps for the parser to run successfully.")
    print("\n\t1. Check there are no tables,rows or columns present.")
    print("\n\t2. Check there is no styling present as the resume parser may fail to extract it.")
    print("\n\t3. Check there are no tables,rows or columns present.")
    print("\n\t4. See that all items are aligned in a single sided manner.")
    print("\n\t5. For the experience part, write the format as DD/MM/YY to \"current\" if you're in the same company/organisation.")
    print("\n\n\t\t If all these are checked, please feel free to proceed.")
    print("\n\n\n\tWhile entering resume name be sure to write in format \"resumename.extension\". Enter your resume name:")
    try:
        _resume_inp = input()
        text = textract.process(_resume_inp,method="pdfminer")
        decode_text = text.decode('utf-8')
        bad_chars = ['\xc2','\xa0','\n','\xe2','\x80','\x8b']
        clean_text = decode_text.replace(bad_chars[1],'')
        #print(clean_text)
        clean_text1= clean_text.replace('\u200b','')
        print("\n\nCheck if this is the input given.\n")
        print(clean_text1)
        words = clean_text1.split()
    except:
        print("\n\n\tPlease check the correct format above and then enter")

    return clean_text1

def _job_openings():
    print("\n\tBut before you approach make sure you've uploaded your resume, if not, please upload.")
    print("\n\t1.Uploaded\t2.Not uploaded")
    _option_resume = int(input())
    if _option_resume == 1:
        print("\n\tFine! Now let's check your profile for the above options.\n\n\t...Oops first select an option from openings:")
        _job = int(input())
    elif _option_resume == 2:
        _resume(_option_resume)
        _job_openings()
    else:
        print("\n\tPlease see that you've chosen the correct input!")
        _job_openings()


def _bot():
    print("\n\tHello! Hope you're fine!")
    print("\n\tHow can I help you today?\n")
    print("\t1. Number of Openings\n\t2. Find my match to requirement (System based)")
    _option = int(input())
    df = pd.read_excel('job_requirement.xlsx',usecols=['REQUIREMENT','EXPERIENCE','SKILLS','Others'])
    if _option == 1:
        print("\n\tIf you are searching for another role, please find the mail link below to\n\t send your application and don't forget to maintain the format")
        print("\n\n\tNumber of openings right now:")
        print(df)
        _option_job = int(input())
        if _option_job>=0 and _option_job<3:
            print('\n\nHi again! I\'ve come back just for you!\n We won\'t be assessing you on some old school version. We have something else in our pandora box!' )
            print('\nWe have some questions for you to get the answer.\nThese questions will tell us how fit you are for the job!!')
            res = _test()
            print("\n\n\t RECIEVED YOUR APPLICATION! Please check our other categories as we evaluate your profile.")
        else:
            print('\n\n\tCheck the number entered again!')
            _bot()

    elif _option == 2:
        print("\n\n\tNumber of openings right now:")
        values = [x for x in df["REQUIREMENT"]]
        for x in range(len(values)):
            print("\t",values[x])
        _job_openings()



    else:
        print("\n\n\t INCORRECT OPTION!!    Try again.")
        _bot()
    print("\n\t\t\ttheguyknowsyoubetter@gmail.com\n\n")

_bot()






#text = textract.process("Resume_pl.pdf",method="pdfminer")
#decode_text = text.decode('utf-8')
#bad_chars = ['\xc2','\xa0','\n','\xe2','\x80','\x8b']
#clean_text = decode_text.replace('\xa0','')
##print(clean_text)
#clean_text1= clean_text.replace('\u200b','')
#words = clean_text1.split()
#print(words[:400])

#p = "Percentage"
#percent = clean_text.find(p)
#print("Percentage = {}".format(clean_text[219:224]))

#loc = ("job_requirement.xlsx")
#wb = xlrd.open_workbook(loc)
#sheet = wb.sheet_by_index(0)
#sheet.cell_value(0,0)
#wb = xlrd.open_workbook(loc)
#sheet = wb.sheet_by_index(0)
#for r in xrange(sheet.nrows):
#  row = sheet.row(r)
#  if row[0].value == "Quality Assurance":
#    print(row_value)

#for sh in xlrd.open_workbook(loc).sheets():
#    for row in range(sh.nrows):
#        for col in range(sh.ncols):
#            myCell = sh.cell(row, col)
#            print(myCell.value)
#store it into matrix
