from .system_helpers import save_to_file, get_file_data, save_list_to_file
from .decorators_helpers import is_email_valid, is_phone_valid


@is_email_valid
@is_phone_valid
def save(
        email, first_name, last_name,
        phone, work_id, type
):
    new_employee = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "work_id": work_id,
        "type": type,
    }
    save_to_file(new_employee, "database/employees.json")


def update(id):
    employers = get_file_data("database/employees.json")
    found = False
    for employee in employers:
        if id == employee["id"]:
            found = True
            employee["email"] = input("Email: ")
            employee["first_name"] = input("First name: ")
            employee["last_name"] = input("Last Name: ")
            employee["phone"] = input("Phone: ")
            employee["work_id"] = input("Work id: ")
            employee["type"] = input("type: ")
    save_list_to_file(employers, "database/employees.json")
    if not found:
        print('id employee not found. Please try again.')


def get_all_employers():
    employees = get_file_data("database/employees.json")
    for employee in employees:
        print(employee["email"])
        print(employee["first_name"])
        print(employee["last_name"])
        print(employee["phone"])
        print(employee["work_id"])
        print(employee["type"])
        print('------------------')


def get_employee_by_email(email):
    employees = get_file_data("database/employees.json")
    for employee in employees:
        if employee["email"] == email:
            print(employee["email"])
            print(employee["first_name"])
            print(employee["last_name"])
            print(employee["phone"])
            print(employee["work_id"])
            print(employee["type"])
            return employee


def save_plant(name, address):
    new_plant = {"name": name, "address": address}
    save_to_file(new_plant, "database/plants.json")


def save_university(name, address):
    new_un = {"name": name, "address": address}
    save_to_file(new_un, "database/university.json")


def get_all_plants():
    plants = get_file_data("database/plants.json")
    for plant in plants:
        print(plant["name"])
        print(plant["address"])


def get_plant_by_id(id):
    plants = get_file_data("database/plants.json")
    found = False
    for plant in plants:
        if plant["id"] == id:
            found = True
            print(plant["name"])
            print(plant["address"])
    if not found:
        print('id plant not found. Please try again')


def get_university_by_id(id):
    univ = get_file_data("database/university.json")
    found = False
    for un in univ:
        if un["id"] == id:
            found = True
            print(univ["name"])
            print(univ["address"])
    if not found:
        print('id university not found. Please try again')


def save_salon(name, address):
    new_el = {"name": name, "address": address}
    save_to_file(new_el, "database/salons.json")


def get_salon_by_id(id):
    salons = get_file_data("database/salons.json")
    for salon in salons:
        if salon["id"] == id:
            print(salon["name"])
            print(salon["address"])


def delete_employee(id):
    employees = get_file_data("database/employees.json")
    for i in range(len(employees)):
        if id == employees[i]["id"]:
            del employees[i]
            break
    save_list_to_file(employees, "database/employees.json")
