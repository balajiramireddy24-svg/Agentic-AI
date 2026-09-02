#1.Patient Registation 
patients_records = []
doctor_records = []
appointment_records =[]
bills = []

def register_patient():
    patient = {
        "id": int(input("Enter Patient ID: ")),
        "name": input("Enter Patient Name: "),
        "age": int(input("Enter Age: ")),
        'Gender':input("Enter the Patient Gender :"),
        "Contact No": int(input("Enter Phone No: "))
    }

    patients_records.append(patient)
    print("Patient registered successfully!")


register_patient()

print(patients_records)



#2.Doctor RegistationDoctor ID
'''Doctor Id
Doctor name
Specialization
Experience
Consultation charge
Availability'''
doctor_records = []
def doctor_register():
    doctor= {
        'Doctor Id':input("Enter the Doctor ID:"),
        'Doctor Name':input("Ente rthe Doctor Name :"),
        'Specialization':input("Enter the Doctor Specialzatio :"),
        'Doctor Charges' :int(input("Enter the Doctor Consultiom Fee:"))
        }
    
    doctor_records.append( doctor)
    print("Doctor registered successfully!")

doctor_register()

print(doctor_records)


#3. Doctor Allocation 
def allocate_doctor():

    patient_id = int(input("Enter Patient ID: "))
    doctor_id = int(input("Enter Doctor ID: "))

    if patient_id in patients and doctor_id in doctors:

        patients[patient_id]["doctor_id"] = doctor_id

        print("Doctor allocated successfully!")
        print("Patient:", patients[patient_id]["name"])
        print("Doctor:", doctors[doctor_id]["name"])

    else:
        print("Invalid Patient ID or Doctor ID")


#4.Book Appointment
def book_appointments():
    appointment = {
        'patient_id':int(input("Enter the Patient Id :")),
                'doctor_id':input("Enter the Doctor Id:"),
                'Date':input("Enter the Appointment Date :"),
                'Time':input("Enter the Appointment Time: ")
    }
    appointment_records.append(appointment)
    print(" Booking Appointment Successfully! Completed.....")
book_appointments()
print(appointment_records)

#5. Appointment Cancellation 
def cancel_appointment():
    patient_id = int(input("Enter Patient ID: "))

    for appointment in appointment_records:
        if appointment["patient_id"] == patient_id:
            appointment["status"] = "Cancelled"
            print("Appointment cancelled!")
            return

    print("Appointment not found.")
cancel_appointment()

#6. Medical History 
def add_medical_history():

    patient_id = int(input("Enter Patient ID: "))

    if patient_id in patients:

        date = input("Enter Visit Date: ")
        disease = input("Enter Disease: ")
        doctor = input("Enter Doctor Name: ")
        treatment = input("Enter Treatment: ")
        medicine = input("Enter Medicine: ")

        history = {
            "date": date,
            "disease": disease,
            "doctor": doctor,
            "treatment": treatment,
            "medicine": medicine
        }

        patients[patient_id]["medical_history"].append(history)

        print("Medical history added successfully!")

    else:
        print("Patient not found!")



#7.Consultation Charges
def consultation_charge():
    doctor_id = int(input("Enter Doctor ID: "))

    for doctor in doctors:
        if doctor["id"] == doctor_id:
            print("Doctor:", doctor["name"])
            print("Consultation Charge: ₹", doctor["charge"])
            return

    print("Doctor not found.")
consultation_charge()

#8.Billing 
def generate_bill():

    patient_id = int(input("Enter Patient ID: "))

    if patient_id in patients:

        consultation_charge = float(input("Enter Consultation Charge: "))
        medicine_charge = float(input("Enter Medicine Charge: "))
        test_charge = float(input("Enter Test Charge: "))

        total = consultation_charge + medicine_charge + test_charge

        bills[patient_id] = {
            "consultation_charge": consultation_charge,
            "medicine_charge": medicine_charge,
            "test_charge": test_charge,
            "total": total
        }

        print("\n===== PATIENT BILL =====")
        print("Patient Name:", patients[patient_id]["name"])
        print("Consultation Charge:", consultation_charge)
        print("Medicine Charge:", medicine_charge)
        print("Test Charge:", test_charge)
        print("-------------------------")
        print("Total Bill:", total)

    else:
        print("Patient not found!")


#9. Search Patient
def search_patient():
    patient_id= int(input("Enter the Patient Id :"))
    for pateint in patients_records:
        if patient["id"] == patient_id:
            print("\nPatient Found")
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Phone:", patient["phone"])
            return

    print("Patient not found.")

search_patient()




#10.Daily Appointment Report
def appointment_report():
    print("\n===== APPOINTMENT REPORT =====")

    for appointment in appointments:
        print(
            appointment["patient_id"],
            appointment["doctor_id"],
            appointment["date"],
            appointment["time"],
            appointment["status"]
        )



#9.Add a Main Menu
while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Register Patient")
    print("2. Register Doctor")
    print("3. Book Appointment")
    print("4. Cancel Appointment")
    print("5. Search Patient")
    print("6. Consultation Charges")
    print("7. Generate Bill")
    print("8. Appointment Report")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_patient()

    elif choice == "2":
        register_doctor()

    elif choice == "3":
        book_appointment()

    elif choice == "4":
        cancel_appointment()

    elif choice == "5":
        search_patient()

    elif choice == "6":
        consultation_charge()

    elif choice == "7":
        generate_bill()

    elif choice == "8":
        appointment_report()

    elif choice == "9":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")















