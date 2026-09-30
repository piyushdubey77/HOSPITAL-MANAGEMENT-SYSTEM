import mysql.connector

# ---------------- Database Connection ---------------- #
con = mysql.connector.connect(
    host="localhost",
    user="root",       # your MySQL username
    password="mysql",   # your MySQL password
    database="hospital"
)

cursor = con.cursor()


# ---------------- Function to Add Patient ---------------- #
def add_patient():
    pid = int(input("Enter Patient ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (Male/Female): ")
    disease = input("Enter Disease: ")
    phone = input("Enter Phone Number: ")

    query = "INSERT INTO patients VALUES (%s, %s, %s, %s, %s, %s)"
    data = (pid, name, age, gender, disease, phone)

    try:
        cursor.execute(query, data)
        con.commit()
        print("Patient added successfully!\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}\n")


# ---------------- Function to Display All Patients ---------------- #
def display_patients():
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()

    if not rows:
        print("\nNo patient records found.\n")
    else:
        print("\n--- All Patients ---")
        for row in rows:
            print(row)
        print()


# ---------------- Function to Search Patient ---------------- #
def search_patient():
    pid = int(input("Enter Patient ID to search: "))
    query = "SELECT * FROM patients WHERE pid=%s"
    cursor.execute(query, (pid,))
    row = cursor.fetchone()

    if row:
        print("\nPatient Found:", row, "\n")
    else:
        print("Patient not found.\n")


# ---------------- Function to Update Patient ---------------- #
def update_patient():
    pid = int(input("Enter Patient ID to update: "))
    new_disease = input("Enter new disease: ")
    query = "UPDATE patients SET disease=%s WHERE pid=%s"
    cursor.execute(query, (new_disease, pid))
    con.commit()

    if cursor.rowcount> 0:
        print("Record updated successfully!\n")
    else:
        print("Patient not found.\n")


# ---------------- Function to Delete Patient ---------------- #
def delete_patient():
    pid = int(input("Enter Patient ID to delete: "))
    query = "DELETE FROM patients WHERE pid=%s"
    cursor.execute(query, (pid,))
    con.commit()

    if cursor.rowcount> 0:
        print("Record deleted successfully!\n")
    else:
        print("Patient not found.\n")


# ---------------- Main Menu ---------------- #
def main():
    while True:
        print("==== Hospital Management System ====")
        print("1. Add Patient")
        print("2. Display All Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if choice == 1:
            add_patient()
        elif choice == 2:
            display_patients()
        elif choice == 3:
            search_patient()
        elif choice == 4:
            update_patient()
        elif choice == 5:
            delete_patient()
        elif choice == 6:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")


# ---------------- Run the Program ---------------- #
if __name__ == "__main__":
    try:
        main()
    finally:
        # Ensures connection closes cleanly no matter how the program exits
        cursor.close()
        con.close()
