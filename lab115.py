import csv
def signup():
    '''sp = "!@#$%^&*()_+{}:<>?,./;'\|][".split()
    sp.append('"')'''
    lc=uc=sp=d=ss=0
    with open (r"C:\Users\Fathima\Desktop\coding\lab +2\login11.csv","r") as fr:
        with open("login11.csv","a",newline="") as f:
            data = csv.reader(fr)
            w = csv.writer(f)
            l = []
            for i in data:
                l = i
                break
            print(l)
            if "UserID" not in l:
                w.writerow(["UserID","Password"])                
            else:
                pass
            while True:
                uid = input("Enter User id:")
                for i in data:
                    if uid in i[0]:
                        print("UserID exist.Enter another id")
                        break
                else:
                    break
            while True:
                A = True
                pas =input("Enter Password:")
                '''if for j in pas:
                    if j.isspace == True:
                        print("Password must not contain space.Try again")
                        A = False
                if len(pas)<8:
                    print("Password must contain 8 characters.Try Again")
                    A = False
                elif pas == uid:
                    print("Password cannot be user id.Try again")
                    A = False
                for i in pas:
                    if i.isupper():
                        break
                else:
                    print("Password must contain atleast 1 Uppercase")
                    A = False
                for i in pas:
                    if i.islower():
                        break
                else:
                    print("Password must contain atleast 1 lowercase")
                    A = False
                for i in pas:
                    if i.isdigit():
                        break
                else:
                    print("Password must contain atleast 1 digit")
                    A = False
                for k in sp:
                    if k in pas:
                        break
                else:
                    print("Password must contain a special character:")
                    A = False'''
                for i in pas:
                    if i.isupper():
                       uc+=1
                    elif i.islower():
                        lc+=1
                    elif i.isdigit():
                        d+=1
                    elif i.isspace():
                        print("Password cannot contain space.Try again")
                        break
                    else:
                        sp+=1
                if pas == uid:
                    print("Password cannot be same as user id")
                elif len(pas)<8:
                    print("Password must atleast contain 8 character.")
                elif uc == 0:
                    print("Password must contain atleast 1 uppercase")
                elif lc == 0:
                    print("Password must contain atleast 1 lowercase")
                elif d ==0:
                    print("Password must contain atleast 1 digit")
                else:
                    cpas = input("Confirm password:")
                    if pas != cpas:
                        print("Password not matching.Try again")
                    else:
                        w.writerow([uid,pas])
                        print("Account created")
                        break
                
signup()

            
        
        
