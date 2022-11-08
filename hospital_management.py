list_of_patients = []
no_of_beds = 0

admin_credentials = {"username" :"admin", "password":"admin"}
while (1):
    opn = int(input("Please choose an option 1) Add a patient's record 2) Delete a patient's record 3) List the number of patients 4) List the number of beds "))
    
    if opn == 1 or opn == 2 or opn == 3:
        username = input("Enter the admin username ")
        if username == admin_credentials["username"]:
            password = input("Enter the admin passowrd ")
            if password == admin_credentials["password"]:
                if opn == 1:
                    data = input("Enter the new patient id, name, age and 4 digit aadhar number(4digits) and symptoms ")
                    data = data.split(",")
                    is_id = False
                    is_aadhar = False
                    for i in list_of_patients:
                        if data[0] == i["id"]:
                            is_id = True
                            print("Please enter a new id")
                        if data[3] == i["aadhar number"]:
                            is_aadhar = True
                            print("Please enter a different aadhar number")
                    if not is_id and not is_aadhar:
                        if len(data[3]) != 4:
                            print("Please enter a valid 4 digit aadhar number")
                        else:
                            list_of_patients.append({"id": data[0], 
                            "name": data[1], 
                            "age": data[2],
                            "aadhar number": data[3], 
                            "symptoms": data[4]
                            })
                            no_of_beds+=1
                            print("The list of patients is %s" %list_of_patients)
                            print("The number of beds occupied = %d" %no_of_beds)
                if opn == 2:
                    id = input("Enter the patient id you want to delete ")
                    is_id = False
                    for i in list_of_patients:
                        if id == i["id"]:
                            is_id = True
                            list_of_patients.remove(i)
                            no_of_beds-=1
                            print("The patient with the given id is removed")
                            print("The list of patients %s" %list_of_patients)
                            print("The number of beds occupied = %d"%no_of_beds)
                    if not is_id:
                        print("Please enter a valid id number")
                if opn == 3:
                    print("The list of patients %s " %list_of_patients)
            else:
                print("Wrong credentials")
        else:
            print("Wrong credentials")
    if opn == 4:
        print("The number of beds occupied = %d" %no_of_beds)
