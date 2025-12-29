def signup():
    username=input("Enter your Username: ")
    password=input("Enter your Password: ")
    passcross=input("Confirm Password: ")
    if password==passcross:
        return(username,password)
    else:
        print("Password Mismatch. Try again")
        e.entry()
def login():
    userID=int(input("Enter your User ID: "))
    password=input("Enter your Password: ")
    return (password,userID)

class teacher:
    def signup(a):
        global tusername
        # tusername="swetha"
        global tpassword
        # tpassword='12'
        try:
            if tusername:
                print("Professor has already created an account!")
                e.entry()
        except:
            tusername,tpassword=signup()
        print("You have succesffully signed in!")
        print("Hello Professor!")
        print()
        t.act()
    def act(a):
        print("1.No. of students enrolled\t\t2.Examination Questions\t\t3.Evaluation\t\t4.Exit")
        t1=int(input("Choose your Preference: "))
        if t1==1:
            for i in range(len(student.susernameall)):
                print(student.IDall[i],student.susernameall[i])
            if (len(student.susernameall))==0:
                print("Students haven't enrolled still")
            t.act()
        if t1==2:
            global tnqa
            global tqit
            global tnoq
            global tansall
            try:
                if len(tnqa)>0:
                    print("Question paper has been set already!")
            except:
                tnoq=int(input("Please enter total no.of questions: "))
                tnqa=[];tqit=[];tansall=[]
                for i in range(1,tnoq+1):
                    tail=[]
                    tqi=input('Question %i:'%i)
                    tqo=(int(input("Enter total no.of options for this question: ")))
                    for j in range(1,tqo+1):
                        tai=input('Option %i:'%j)
                        tail=tail+[tai]
                    tans=input("Enter the correct answer: ")
                    tansall+=[tans]
                    tnq=[]+[tqi]
                    tnqa+=[tail]
                    tqit+=[tqi]
                print("Question Paper has been successfully set!")
                print("Students can attend the exam!")
                # tnqa=[['meaning', 'thesaurus'], ['red', 'green'],['right','wrong']]
                # tqit=['what is definition?', 'which colour is this?','What will be your choice?']
                # tansall=['meaning', 'red','right']
                # tnoq=3
            t.act()
        if t1==3:
            for i in student.stestIDall:
                print(i)
            global markall
            markall=[]
            if (len(student.stestIDall))==0:
                print("Students have not written the exam")
            else:
                for i in range(len(student.stestIDall)):
                    mark=0
                    for j in range(len(student.allsa[i])):
                        if tansall[j]==student.allsa[i][j]:
                            mark+=1
                    markall+=[mark]
                print("You have sucessfully evaluated all students")
            t.act()
        if t1==4:
            print("You have successfully logged Out")
            e.entry()
    
    def login(a):
        tlun=input("Enter your User Name: ")
        if tusername==tlun:
            tlp=input("Enter your Password: ")
            if tpassword==tlp:
                print('You have successfully logged in Professor!')
                t.act()
            else:
                print("Password is incorrect")
                e.entry()
        else:
            print("Username doesn't exist. Please Sign Up")
            t.signup()
t=teacher()

class student():
    ID=1001
    IDall=[]
    susernameall=[]
    spasswordall=[]
    def signup(a):
        susername,spassword=signup()
        student.susernameall+=[susername]
        student.spasswordall+=[spassword]
        if susername!=0:
            print("Your ID number is: ",student.ID)
            sinput=input("Make a note of your ID and enter 'yes': ")
            student.IDall+=[student.ID]
            student.ID+=1
            s.act((student.ID-1))
    stestIDall=[]
    allsa=[]
    def act(a,slID):
        print("1. Write exam\t\t2. View Result\t\t3.Logout")
        s1=int(input("Choose your Preference: "))
        if s1==1:
            try:
                if slID in student.stestIDall:
                    print("You have already attended the exam!")
                else:
                    print("Total No.of Questions: %i"%tnoq)
                    snqaa=[]
                    for f in range(len(tqit)):
                        print('Question %i:'%(f+1))
                        print(tqit[f])
                        for j in range(1,len(tnqa[f])+1):
                            print('Option %i:'%j,tnqa[f][j-1])
                        snqa=input("Enter your answer: ")
                        snqaa+=[snqa]
                    student.allsa+=[snqaa]
                    print("You have attended the test successfully!")
                    student.allsa+=[snqaa]
                    student.stestIDall+=[slID]
                s.act(slID)
            except:
                print()
                print("Teacher hasn't set the question paper!")
                print("Try after some time")
                print()
                s.act(slID)
        if s1==2:
            try:
                smark=(markall[(student.stestIDall).index(slID)])
                print(smark)
                result="Pass" if smark>=(tnoq/2) else "Fail"
                print("RESULT: ",result)
            except:
                print("Teacher haven't evaluated")
            s.act(slID)
        if s1==3:
            e.entry()
    def login(a):
        slpa,slID=login()
        if slID in student.IDall and student.spasswordall[(student.IDall).index(slID)]==slpa:
            s.act(slID)
s=student()

# Program starts
print("Examination System")
print()
class entrance():
    def entry(a):
        print('1.Professor \t\t2.Student\t\t3.Exit')
        a=int(input("Enter your Designation: "))
        if a==1:
            print("Professor's Desk!!!")
            print("1.Login\t\t2.Sign Up\t\t3.Exit")
            b=int(input("Choose your preference: "))
            if b==1:
                t.login()
            if b==2:
                t.signup()
            if b==3:
                e.entry()
        if a==2:
            print("Student's Desk!!!")
            print("1.Login\t\t2.Sign Up\t\t3.Exit")
            b=int(input("Choose your preference: "))
            if b==1:
                s.login()
            if b==2:
                s.signup()
            if b==3:
                e.entry()
        if a==3:
            exit()
e=entrance()
e.entry()
