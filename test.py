from fileinput import filename
import json
from os import path
from uuid import uuid4
import json

print("Enter any number \n \n 1:create \n 2: update \n 3:deleteById\n 4: readById\n")
userChoice = int(input("\nEnter Your choice\n"))


if userChoice == 1:
    def emp_datas_json(new_emp_data, filename='emp_datas.json'):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            new_emp_data["emp_id"]='A2002'+str(len(file_data))
            file_data.append(new_emp_data)
            # print(len(file_data))
            # # file_data["emps_details"].append(new_emp_data)
            # listemp=[int(emp_id[-1]['emp_id'])]
            # emp_id= listemp[-1]+1
            # listemp.append("A2002"+str(emp_id))

            # file_data.append(new_emp_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    
    emp_class = {
        "emp_id": list[0],
        "emp_firstname": str(input("\nEnter employee first name\n")),
        "emp_lastname": str(input("\nEnter employee last name\n")),
        "age": int(input("\n Enter employee age\n")),
        "city": str(input("\n Enter employee city\n")),
        "CTC": int(input("\n Enter employee CTC\n")),
        "experience":int(input("\n Enter employee Experience\n")),
        "contactno": int(input("\n Enter employee Contactno\n"))
    }
    emp_datas_json(emp_class)


elif userChoice == 2:
    given_id = input("Enter emp_id")
    with open("emp_datas.json", 'r+') as s_File:
        data = json.load(s_File)
        for idx, emp in enumerate(data):
            if given_id == emp['emp_id']:
                data[idx]["emp_firstname"] = input("\nEnter employee first name\n")
                data[idx]["emp_lastname"] = input("\nEnter employee last name\n")
                data[idx]["age"] = input("\n Enter employee age\n")
                data[idx]["city"] = input("\n Enter employee city\n")
                data[idx]["CTC"] = input("\n Enter employee CTC\n")
                data[idx]["experience"] = input("\n Enter employee Experience\n")
                data[idx]["contactno"] = input("\n Enter employee Contactno\n")
                with open('emp_datas.json', 'w') as data_file:
                    data = json.dump(data, data_file, indent=4)
                break

elif userChoice == 3:
    given_id = input("Enter emp_id")
    with open("emp_datas.json", 'r+') as s_File:
        data = json.load(s_File)
        for idx, emp in enumerate(data):
            if given_id == emp["emp_id"]:
                # print(data[idx]["emp_id"])
                del(data[idx])
                print('deleted successfully')
                with open('emp_datas.json', 'w') as data_file:
                    data = json.dump(data, data_file, indent=4)
                break

elif userChoice == 4:
    given_id = input("Enter emp_id")
    with open("emp_datas.json", 'r+') as s_File:
        data = json.load(s_File)
        for idx, emp in enumerate(data):
            if given_id == emp["emp_id"]:
                print(data[idx])
                break
else:
    print("Invalid entry")
