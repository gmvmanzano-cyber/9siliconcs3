class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = str(name)

    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(self, bill_amount):
        self.__bill_amount = float(bill_amount)
    def display_patient_type(self):
        return "Regular Patient"

    def calculate_bill(self):
        print("Hospital Billing System\n-----------------------------------")
        print("Patient Name:",self.get_name())
        print("Patient:", self.display_patient_type())
        print(f"Original Bill: ₱{self.get_bill_amount():,.2f}")
        print(f"Final Bill: ₱{self.get_bill_amount():,.2f}")


class SeniorPatient(Patient):
    def display_patient_type(self):
        return "Senior Citizen"
    def calculate_bill(self):
        print("\nPatient Name:", self.get_name())
        print("Patient:", self.display_patient_type())
        print(f"Original Bill: ₱{self.get_bill_amount():,.2f}")
        print(f"Final Bill: ₱{self.get_bill_amount() - self.get_bill_amount() * 0.20:,.2f}")


class PhilHealthPatient(Patient):
    def display_patient_type(self):
        return "PhilHealth Member"
    def calculate_bill(self):
        print("\nPatient Name:", self.get_name())
        print("Patient:", self.display_patient_type())
        print(f"Original Bill: ₱{self.get_bill_amount():,.2f}")
        print(f"Final Bill: ₱{self.get_bill_amount() - self.get_bill_amount() * 0.15:,.2f}")
JDC = Patient("Juan Dela Cruz", 15000)
JDC.set_name("Juan Dela Cruz")
JDC.set_bill_amount(15000)
JDC.calculate_bill()

MS = SeniorPatient("Maria Santos", 15000)
MS.set_name("Maria Santos")
MS.set_bill_amount(15000)
MS.calculate_bill()

PR = PhilHealthPatient("Pedro Reyes", 15000)
PR.set_name("Pedro Reyes")
PR.set_bill_amount(15000)
PR.calculate_bill()