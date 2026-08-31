from datetime import datetime


# Parent Class
class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone


# Patient Class - Inheritance
class Patient(Person):
    def __init__(self, patient_id, name, age, phone):
        super().__init__(name, age, phone)
        self.patient_id = patient_id
        self.doctor = ""
        self.history = []

    def display(self):
        print("\nPatient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)
        print("Doctor:", self.doctor)

        if self.history:
            print("Medical History:")
            for h in self.history:
                print("-", h)
        else:
            print("Medical History: No records")


# Doctor Class - Inheritance
class Doctor(Person):
    def __init__(self, doctor_id, name, age, phone, specialization, charge):
        super().__init__(name, age, phone)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.charge = charge
        self.available = True

    def display(self):
        print("\nDoctor ID:", self.doctor_id)
        print("Name:", self.name)
        print("Specialization:", self.specialization)
        print("Phone:", self.phone)
        print("Consultation Charge:", self.charge)
        print("Available:", self.available)


# Lists
patients = []
doctors = []
appointments = []


# ---------------- FILE HANDLING ----------------

def save_patients():
    try:
        file = open("patients.txt", "w")

        for p in patients:
            data = {
                "id": p.patient_id,
                "name": p.name,
                "age": p.age,
                "phone": p.phone,
                "doctor": p.doctor
            }

            file.write(str(data) + "\n")

        file.close()

    except Exception as e:
        print("File Error:", e)


def save_doctors():
    try:
        file = open("doctors.txt", "w")

        for d in doctors:
            data = {
                "id": d.doctor_id,
                "name": d.name,
                "specialization": d.specialization,
                "phone": d.phone,
                "charge": d.charge
            }

            file.write(str(data) + "\n")

        file.close()

    except Exception as e:
        print("File Error:", e)


def save_appointments():
    try:
        file = open("appointments.txt", "w")

        for a in appointments:
            file.write(str(a) + "\n")

        file.close()

    except Exception as e:
        print("File Error:", e)


# ---------------- PATIENT REGISTRATION ----------------

def patient_registration():

    try:
        patient_id = input("Enter Patient ID: ")

        # Check duplicate ID
        for p in patients:
            if p.patient_id == patient_id:
                print("Patient ID already exists!")
                return

        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        phone = input("Enter Phone Number: ")

        patient = Patient(patient_id, name, age, phone)

        patients.append(patient)

        save_patients()

        print("Patient registered successfully!")

    except ValueError:
        print("Age must be a number.")

    except Exception as e:
        print("Error:", e)


# ---------------- DOCTOR REGISTRATION ----------------

def doctor_registration():

    try:
        doctor_id = input("Enter Doctor ID: ")

        for d in doctors:
            if d.doctor_id == doctor_id:
                print("Doctor ID already exists!")
                return

        name = input("Enter Doctor Name: ")
        age = int(input("Enter Doctor Age: "))
        phone = input("Enter Phone Number: ")
        specialization = input("Enter Specialization: ")
        charge = float(input("Enter Consultation Charge: "))

        doctor = Doctor(
            doctor_id,
            name,
            age,
            phone,
            specialization,
            charge
        )

        doctors.append(doctor)

        save_doctors()

        print("Doctor registered successfully!")

    except ValueError:
        print("Age and charge must be numbers.")

    except Exception as e:
        print("Error:", e)


# ---------------- DOCTOR ALLOCATION ----------------

def doctor_allocation():

    patient_id = input("Enter Patient ID: ")

    patient = None

    for p in patients:
        if p.patient_id == patient_id:
            patient = p
            break

    if patient is None:
        print("Patient not found!")
        return

    print("\nAvailable Doctors:")

    for d in doctors:
        if d.available:
            print(
                d.doctor_id,
                "-",
                d.name,
                "-",
                d.specialization
            )

    doctor_id = input("Enter Doctor ID: ")

    for d in doctors:

        if d.doctor_id == doctor_id:

            if d.available:

                patient.doctor = d.name
                d.available = False

                save_patients()

                print("Doctor allocated successfully!")

            else:
                print("Doctor is not available.")

            return

    print("Doctor not found!")


# ---------------- APPOINTMENT BOOKING ----------------

def appointment_booking():

    patient_id = input("Enter Patient ID: ")

    patient_found = False

    for p in patients:
        if p.patient_id == patient_id:
            patient_found = True
            break

    if not patient_found:
        print("Patient not found!")
        return

    doctor_id = input("Enter Doctor ID: ")

    doctor_found = False

    for d in doctors:
        if d.doctor_id == doctor_id:
            doctor_found = True
            break

    if not doctor_found:
        print("Doctor not found!")
        return

    date = input("Enter Appointment Date (DD-MM-YYYY): ")
    time = input("Enter Appointment Time (HH:MM): ")

    try:
        appointment_date = datetime.strptime(
            date + " " + time,
            "%d-%m-%Y %H:%M"
        )

        appointment = {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": date,
            "time": time,
            "status": "Booked"
        }

        appointments.append(appointment)

        save_appointments()

        print(
            "Appointment booked on:",
            appointment_date.strftime("%d-%m-%Y %H:%M")
        )

    except ValueError:
        print("Invalid date or time format!")


# ---------------- APPOINTMENT CANCELLATION ----------------

def appointment_cancellation():

    patient_id = input("Enter Patient ID: ")

    found = False

    for a in appointments:

        if (
            a["patient_id"] == patient_id
            and a["status"] == "Booked"
        ):

            a["status"] = "Cancelled"

            save_appointments()

            print("Appointment cancelled successfully!")

            found = True
            break

    if not found:
        print("No booked appointment found.")


# ---------------- MEDICAL HISTORY ----------------

def medical_history():

    patient_id = input("Enter Patient ID: ")

    for p in patients:

        if p.patient_id == patient_id:

            treatment = input("Enter Treatment / Medical History: ")

            date = datetime.now().strftime("%d-%m-%Y")

            record = date + " : " + treatment

            p.history.append(record)

            save_patients()

            print("Medical history added successfully!")

            return

    print("Patient not found!")


# ---------------- CONSULTATION CHARGES ----------------

def consultation_charges():

    doctor_id = input("Enter Doctor ID: ")

    for d in doctors:

        if d.doctor_id == doctor_id:

            print("Doctor:", d.name)
            print("Specialization:", d.specialization)
            print("Consultation Charge: ₹", d.charge)

            return

    print("Doctor not found!")


# ---------------- BILLING ----------------

def billing():

    patient_id = input("Enter Patient ID: ")

    patient = None

    for p in patients:

        if p.patient_id == patient_id:
            patient = p
            break

    if patient is None:
        print("Patient not found!")
        return

    doctor_name = patient.doctor

    if doctor_name == "":
        print("No doctor allocated.")
        return

    charge = 0

    for d in doctors:

        if d.name == doctor_name:
            charge = d.charge
            break

    print("\n========== HOSPITAL BILL ==========")
    print("Patient ID:", patient.patient_id)
    print("Patient Name:", patient.name)
    print("Doctor:", doctor_name)
    print("Consultation Charge: ₹", charge)
    print("-----------------------------------")
    print("Total Bill: ₹", charge)
    print("Date:", datetime.now().strftime("%d-%m-%Y"))
    print("===================================")


# ---------------- PATIENT SEARCH ----------------

def patient_search():

    patient_id = input("Enter Patient ID: ")

    for p in patients:

        if p.patient_id == patient_id:

            p.display()
            return

    print("Patient not found!")


# ---------------- DAILY APPOINTMENT REPORT ----------------

def daily_appointment_report():

    today = datetime.now().strftime("%d-%m-%Y")

    print("\n====== DAILY APPOINTMENT REPORT ======")
    print("Date:", today)

    found = False

    for a in appointments:

        if a["date"] == today:

            print("\nPatient ID:", a["patient_id"])
            print("Doctor ID:", a["doctor_id"])
            print("Time:", a["time"])
            print("Status:", a["status"])

            found = True

    if not found:
        print("No appointments for today.")


# ---------------- MAIN MENU ----------------

def main():

    while True:

        print("\n======================================")
        print("   HOSPITAL MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Patient Registration")
        print("2. Doctor Registration")
        print("3. Doctor Allocation")
        print("4. Appointment Booking")
        print("5. Appointment Cancellation")
        print("6. Medical History")
        print("7. Consultation Charges")
        print("8. Billing")
        print("9. Patient Search")
        print("10. Daily Appointment Report")
        print("11. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                patient_registration()

            elif choice == 2:
                doctor_registration()

            elif choice == 3:
                doctor_allocation()

            elif choice == 4:
                appointment_booking()

            elif choice == 5:
                appointment_cancellation()

            elif choice == 6:
                medical_history()

            elif choice == 7:
                consultation_charges()

            elif choice == 8:
                billing()

            elif choice == 9:
                patient_search()

            elif choice == 10:
                daily_appointment_report()

            elif choice == 11:
                print("Thank you for using Hospital Management System!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number.")

        except Exception as e:
            print("Error:", e)


# Start Program
main()