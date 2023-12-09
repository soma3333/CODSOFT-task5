name=[]
phno=[]
email=[]
address=[]

print("****CONTACT BOOK****")
print("")
print("INSTRUCTIONS: ")
print("1:To Add new contact")
print("2:To  update the contact ")
print("3:To display all contact details")
print("4:To search the contact either by name or phone number")
print("5:To delete the contact  by name")
print("6:To Exit the contact book")

def addcontact():
    print("Provide your details----")
    a=input("Your name :")
    b=input("Your phone number :")
    c=input("Your email id :")
    d=input("Your address :")

    name.append(a)
    phno.append(b)
    email.append(c)
    address.append(d)
    print("***Your contact added successfully***")

def Display():
    print("Contact list :")
    for i  in range(len(name)):
        print("name :",name[i])
        print("phone no  :",phno[i])

def search():
    e=input("Enter Your name or phone number to  get details :")
    for i in range(len(name)):
        if e==name[i]:
            print("name :",name[i])
            print("phone no  :",phno[i])
            print("email :",email[i])
            print("address  :",address[i])
            break
        elif e==phno[i]:
            print("name :",name[i])
            print("phone no  :",phno[i])
            print("email :",email[i])
            print("address  :",address[i])
            break

def delete():
    dlt=input("Enter the contact name u want to delete :")
    for i in range(len(name)):
        if dlt==name[i]:
            name.pop(i)
            phno.pop(i)
            email.pop(i)
            address.pop(i)
    print("***Contact  name ",dlt,"is successfully deleted***")

def Update():
    na=input("Enter the name of  the contact u want to update : ")
    for i in range(len(name)):
        if na==name[i]:
            print("1:To update name")
            print("2:To update phono")
            print("3:To update email")
            print("4:To update address")
            cho=int(input("enter the choice u have to update :"))
            if cho==1:
                 name[i]=input("enter new name :")
                 print("new name updated.....")
            elif cho==2:
                 phno[i]=input("enter new phone no :")
                 print("new phone no updated.....")
            elif cho==3:
                 email[i]=input("enter new email :")
                 print("new email updated.....")
            elif cho==4:
                address[i]=input("enter new address :")
                print("new address updated.....")
            else:
                print("choose correct choice")
            break
def contact():
    print("")
    choice=int(input("Enter the choice number : "))
    if choice==1:
        addcontact()
        contact()
    elif choice==2:
        Update()
        contact()
    elif choice==3:
        Display()
        contact()
    elif choice==4:
        search()
        contact()
    elif choice==5:
        delete()
        contact()
    elif choice==6:
        print("THANK YOU!...")
    else:
        print("Enter correct choice")

contact()