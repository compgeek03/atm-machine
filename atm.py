#bugs
# 1.making the passwd encrypted
# 2.proper DB-create UserID for each user-usename already exists-new user saving-combinations,balance,deposit and new balance
# 3.only deposit problem
# 4.for y and n if any charecter is used it accepts

#temporary DB  
combinations={
    "joey":"jim",
    "ross":"pam",
}
balance={
    "joey":10000,
    "ross":10000,
}
new_balance={
    "joey":" ",
    "ross":" ",
}

pos="yyesYESYYes"

print("\n\n                                                     Welcome to The ATN Bank !!!                                            \n")
#if an existing customer 
are_user=input("Do you have an account? ")
print("\n")
#login and operations

if are_user  in pos:
    
    #user input for name and pass
    user_name=input("USERNAME: ")
  
    user_input=input("PIN/PASSWORD: ")
   
    print("\n")
    #pass not match/user dne
    if  user_input.lower()!=combinations[user_name]:
         print("not valid password") 
    
    else: 
        #user operations choices
            make_withdraw=input("Do you want to make widthdrawal? ")
            check_balance=input("Do you want to check balance? ")
            deposit=input("Do you want to deposit a sum? ")
            
            
            #user widthraw amount  min balance=1000
            if make_withdraw.lower() in pos:
                user_withdraw=int(input("how much widthdraw:"))
                
                if user_withdraw <=(balance[user_name]-1000):
                    print("making withdrawal....")
                    new_balance[user_name]=balance[user_name]- user_withdraw
                    print("youre current balance is :"+str(new_balance[user_name]))    
                else:
                    print("amount not valid")

            #user checks balance
            if  check_balance.lower() in pos :
                print("your current balance is:"+str(new_balance[user_name] or balance[user_name]))
            
            #user makes a deposit    
            if deposit.lower() in pos:
                user_deposit=int(input("how much do you want to deposit? : "))
                print("depositing...")
                print("Amount Deposited")
                new_balance[user_name]=new_balance[user_name]+user_deposit
                print("your current balance is :"+str(int(new_balance[user_name])))
            print("\n                                 Thank You! Visit Us Soon \n           ")
            
#user sign up and initial deposit with vild userID generation   
else:
    print("Signing You Up!")
    new_username=input("Username:")
    new_password=input("Password:")
    re_password=input("Rewrite the password:")
    if new_username==combinations:
        print("user already exists")
    if new_password==re_password: 
        new_userid=print("new user id is:")
        new_deposit=input("How much do you want to deposit?: ")
        if int(new_deposit)>1000:
            print("depositing...\nAmount Deposited")
            print("your current balance is "+str(new_deposit))
            print("\n                                       Thank You for signing up! Visit Us Soon \n             ")
        else:
            print("ERROR:Minimum balance has to be 1000, Try Again")
    else:
        print("Password Not Matching")