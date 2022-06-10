from fileinput import filename
import json
from os import path
from uuid import uuid4
import json

print("Enter any number \n \n 1:create \n 2: update \n 3: deleteById\n 4: readById\n")
userChoice = int(input("\nEnter Your choice\n"))


if userChoice == 1:
    def emp_data_json(new_emp_data, filename='emp_datas.json'):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            # file_data["emps_details"].append(new_emp_data)
            file_data.append(new_emp_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    emp_class = {
        "emp_id": str(uuid4()),
        "emp_name": input("\nEnter Your name\n"),
        "age": input("\n Enter your age\n"),
        "city": input("\n Enter your city\n"),
        "experience": input("\n Enter your Experience\n")
    }
    emp_data_json(emp_class)


elif userChoice == 2:
    given_id = input("Enter emp_id")
    with open("emp_datas.json", 'r+') as s_File:
        data = json.load(s_File)
        for idx, emp in enumerate(data):
            if given_id == emp['emp_id']:
                data[idx]["emp_name"] = input("\nEnter Your name\n")
                data[idx]["age"] = input("\n Enter your age\n")
                data[idx]["city"] = input("\n Enter your city\n")
                data[idx]["experience"] = input("\n Enter your Experience\n")
                with open('emp_datas.json', 'w') as data_file:
                    data = json.dump(data, data_file)
                break
            else:
                print("Invalid id")
elif userChoice == 3:

    given_id = input("Enter emp_id")
    with open("emp_datas.json", 'r+') as s_File:
        data = json.load(s_File)
        for idx, emp in enumerate(data):
            if given_id == emp["emp_id"]:
                # print(data[idx]["emp_id"])
                del(data[idx])
                with open('emp_datas.json', 'w') as data_file:
                    data = json.dump(data, data_file)
                break
        else:
                print("Invalid id")
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
