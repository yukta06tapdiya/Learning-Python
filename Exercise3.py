import random
questions=["International Literacy Day",
           "The language of Lakshadweep, Union Territory of India",
           "Bahubali Festival is related to",
           "Which day is observed as World Standards Day?",
           "Who is the author of the epic'Meghdoot'",
           "Newspapers are not published from which of thr following indian states",
           "The National Open university is run by",
           "Feild Marshal is Highest rank in "
           ,"Delhi became capital of India in"]

options=[['A:Sep 8','B:Nov 28','C:May 2','D:Sep 22'],
         ['A:Tamil','B:Hindi','C:Malyalam','D:Telgu'],
         ['A:Islam','B:Hinduism','C:Buddhism','D:Jainism'],
         ['A:June 26','B:Oct 14','C:Nov 15','D:Dec 2'],
         ['A:Vishakadatta','B:Valmiki','C:Banabhatta','D:Kalidas'],
         ['A:Assan','B:Manipur','C:Mizoram','D:Arunachal Pradesh'],
         ['A:CBSE','B:UGC','C:IGNOU','D:NCERT'],
         ['A:Army','B:Navy','C:Air Force','D:Teritorial Army'],
         ['A:1910','B:1911','C:1916','D:1923']]

answers=['A','C','D','B','D','D','B','A','B']
money=[1000,2000,3000,4000,5000,6000,7000,8000,9000]
combined=list(zip(questions,options,answers))
random.shuffle(combined)

def Answer():
    print()
    
    answer=input("Enter Your Option")
    if answer==answers[i]:
        print("your answer is correct")
        print("You won prize of ",money[i])
    elif(answer=='QUIT'):
        print("You can exit the game")  
        if(i==0):
            print("Your Winning Prize is ",0)
        else:
            print('Your Winning money:',money[i-1])
        return 0
    else:
        print("Your anwer is wrong")

i=0
while i<9:
    x=0
    print(f'{questions[i]}')
    for j in options[i]:
        print(f'{j}')
    a=Answer()
    
    if x==1:
        break
    i+=1


        











