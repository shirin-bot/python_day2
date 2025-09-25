contacts=[]
def add_contact():
    name = input("name:")
    phone = input("phone:")
    contacts.append({"name":name,"phone":phone})
    print(f"{name} added successfully\n") 
def show_contact():
    if contacts:
        for i in contacts:
            print(f"name : {i['name']},phone : {i['phone']}")
            print()
    else:
        print("no contacts found")      
def search_contacts():
    s = input("name?")
    for c in contacts:
        if c["name"]==s:
            print(f"{c['phone']}\n")
            return
    print("not found") 
def del_contacts():
    d = input("name?")
    for c in contacts:
        if c["name"]== d:
            contacts.remove(c)
            print("deleted")
            return
        print("not found")
while True:
    ch=input("what do you want to do?(add/show/search/delete/exit):")
    if ch=="add":
        add_contact()
    elif ch =="show":
        show_contact()
    elif ch =="search":
        search_contacts()
    elif ch =="delete":
        del_contacts()
    elif ch =="exit":
        print("end")
        break
    else:
        print("try again")
    