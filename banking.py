#write a program to deposite and withdraw money with a bank account
def UserLogin():
    acc=input("Enter the account number: ")
    name=input("Enter your name: ")
    u_pass=input("Enter your password: ")
    for i in accounts:
        if acc==i and UserDetails[acc][1]==name and UserDetails[acc][2]==u_pass:
            f=1
    if f==0:
        print("Invalid acccount number/password")
        
    if f==1:
        while True:
            print("Enter 1 to Deposite.")
            print("Enter 2 to Withdraw.")
            print("Enter 3 to check UserDetails")
            print("Enter 4 to transfer amount")
            print("Enter 5 to exit")
            ch2=int(input("Enter the choice: "))
            if ch2==1:
                amount=int(input("Enter the amount you want to deposite: "))
                UserDetails[acc][0]=UserDetails[acc][0]+amount
                print("Amount Deposited \nCurrent balance:",UserDetails[acc][0])
            elif ch2==2:
                amount=int(input("Enter the amount you want to withdraw: "))
                if (UserDetails[acc][0]-amount > 0):
                    UserDetails[acc][0]=UserDetails[acc][0]-amount
                    print("Withdral Succssful \nCurrent balance:",UserDetails[acc][0])
                else:
                    print("Insufficient Amount")
            elif ch2==3:
                print("Your current UserDetails: ",UserDetails[acc][0])
            elif ch2==4:
                t=0
                transfer=input("Enter the account number: ")
                t_name=input("Enter recievers name:")
                for i in accounts:
                    if i==transfer and UserDetails[i][1]==t_name:
                        t=1
                        break
                if t==0:
                    print("Invalid account number")
                else:
                    t_amount=int(input("Enter the amount you want to transfer: "))
                    if t_amount>UserDetails[acc][0]:
                        print("Insufficient amount to transfer.Please check your balance first")
                    else:
                        UserDetails[acc][0]=UserDetails[acc][0]-t_amount
                        UserDetails[transfer][0]+=t_amount
                        print(f"Your account has been debited rupess {t_amount}.\nSuccessfully transfered.")
            elif ch2==5:
                return 0
    else:
        print("Invalid Account Number/Not register.Please register")

Admin_accont={'A101':['afzal','1'],'A102':['jinnur','2']}
accounts=['101','102']
UserDetails={'101':[2000,'afzal','1'],'102':[4000,'jinnur','2']}
while True:
    print("Enter 1 to register.")
    print("Enter 2 to Login.")
    print("Enter 3 to close")
    f=0
    ch=int(input("Enter your choice: "))
    if ch==1:
        a_n=str(int(accounts[-1])+1)
        name=input("Enter Your name: ")
        u_pass=input("Enter a new password: ")
        am=int(input("Enter amount to deposite: " ))
        l=[]
        l.append(6000)
        l.append('tiyasa')
        l.append('220')
        UserDetails['103']=l
        print("Succesfully registered and your account number is : ",a_n)
        print(UserDetails)
                    
    elif ch==2:
        UserLogin()
    elif ch==3:
        break
