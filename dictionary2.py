def programma_eisodou() :
    from dictionary1 import username_and_password as us_pas
    username = input("usename?")
    password = (input("password?"))
    if username in us_pas:
        if password == us_pas[username]["password"]:
            print("welcome",username)
        else:
            print("wrong password entry forbidden")
    else:
        print ("user not found entry forbidden")

#programma_eisodou()





