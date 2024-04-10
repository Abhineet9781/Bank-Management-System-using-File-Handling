import os

def new_customer():
    print("\t\t\tWELCOME TO OUR BANK")
    a=input("ENTER YOUR NAME: ")
    b=input("ENTER YOUR FATHER'S NAME: ")
    c=input("ENTER YOUR ADDRESS:")
    d=input("ENTER YOUR MOBILE NUMBER: ")
    e=input("TYPE OF GOVT ID(PAN/AADHAAR): ")
    h=input("ACCOUNT TYPE(SAVING/CURRENT): ")
    g=input("ENTER AMOUNT TO DEPOSIT:")
    if(a == '')or(b == '')or(c == '')or(d == '')or(e == '')or(h == '')or(g == ''):
        print("ALL FEILDS ARE MANDATORY AND CANNOT BE EMPTY!!!!")
    elif(not d.isdigit()):
        print('MOBILE NUMBER CANNOT BE IN ALPHABETS!!!!')
    elif(not g.isdigit()):
        print('DEPOSIT AMOUNT CANNOT BE IN ALPHABETS')
    elif(len(d)!=10):
        print('MOBILE NUMBER MUST BE OF 10 DIGITS!!!')
    else:        
        print("_"*80,"\n\t\t\tYOUR ACCOUNT HAS SUCCESFULLY REGISTERED!!!!!")
        print("_"*80)
        if(os.path.exists("bank_data.txt")):
            f=open("bank_data.txt",'r')
            temp=f.read()
            f.close()
            if 'ACCOUNT NO.:' in temp:
                i=temp.count('ACCOUNT NO.:')
                acc=i+1
            else:
                acc=1
        else:
            acc=1
        f=open("bank_data.txt",'a')
        f.write('ACCOUNT NO.:'+str(acc)+'\nName :'+a+"\nFather's name :"+b+'\nAddress :'+c+'\nMobile no. :'+str(d)+'\nGovt ID type :'+e+'\nACCOUNT TYPE:'+h+'\nBalance:'+str(g)+'\n')
        f.close()
        f=open("bank_data.txt",'r')
        temp=f.read()
        j=temp.find('ACCOUNT NO.:'+str(acc))
        print(temp[j:])
        f.close()
        choice=input("\nDO YOU WANT TO ADD ANOTHER ACCOUNT(y/n): ")
        if(choice=='y'):
            new_customer()


def existing_customer():
    global i
    "for existing users"
    print("\t\t\tWELCOME BACK")
    a=int(input("\nENTER YOUR ACCOUNT NUMBER: "))
    f=open("bank_data.txt",'r')
    temp=f.readlines()
    f.close()
    if "ACCOUNT NO.:"+str(a)+'\n' in temp:
        i=temp.index("ACCOUNT NO.:"+str(a)+'\n')
        s=''
        s=''.join([str(j) for j in temp[i:i+8]])
        print(s)
        other()
    else:
        print("ACCOUNT DOES NOT EXIST!!!")

def other():
    global i
    f=open("bank_data.txt",'r')
    temp=f.readlines()
    f.close()
    print("\n1) DEPOSIT MONEY","\n2) WITHDRAW MONEY","\n3) CHECK BALANCE")
    choice=int(input("\nENTER YOUR CHOICE: "))
    d=str(temp[i+7])
    d=d[8:]
    d=int(d)
    if(choice==1):
        amount=int(input("ENTER AMOUNT: "))
        e=amount+d
        temp[i+7]='BALANCE:'+str(e)+'\n'
        f=open("bank_data.txt",'w')
        s=''
        s=''.join([str(j) for j in temp])
        temp=f.write(s)
        f.close()
        print("\nRs",amount,"HAVE BEEN CREDITED TO YOUR ACCOUNT!!!!","\nYOUR NEW ACCOUNT BALANCE IS Rs",d+amount)
    elif(choice==2):
        amount1=int(input("ENTER AMOUNT TO WITHDRAW: "))
        if(amount1<=d):
            d1=d-amount1
            print("WITHDRAW SUCCESSFUL!!PLEASE COLLECT YOUR MONEY!!!","\nYOUR NEW ACCOUNT BALANCE IS Rs",d1)
            f=open("bank_data.txt",'r')
            temp=f.readlines()
            f.close()
            temp[i+7]='BALANCE:'+str(d1)+'\n'
            f=open("bank_data.txt",'w')
            s=''
            s=''.join([str(j) for j in temp])
            temp=f.write(s)
            f.close()
        else:
            print("!!!!!!!!!!INSUFFICIENT BALANCE!!!!!!!!!!!","\nYOUR ACCOUNT BALANCE IS Rs",d)
    elif(choice==3):
        print("YOUR ACCOUNT BALANCE IS Rs",d)
    else:
        print("!!!!!WRONG CHOICE!!!!!")

while True:
    print("_"*80,"\n\t\t\tWELCOME TO BANK MANAGEMENT SYSTEM")
    print("_"*80)
    print("\n1) NEW CUSTOMER","\n2) EXISTING CUSTOMER","\n3) EXIT")
    choice=int(input("ENTER CHOICE: "))
    if(choice==1):
        new_customer()
    elif(choice==2):
        existing_customer()
    elif(choice==3):
        exit()
    else:
        print("WRONG CHOICE!!!!!")
