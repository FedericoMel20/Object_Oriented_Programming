class MedicalRecord:
    def __init__(self, record_id, diagnosis, treatment):
        self.record_id = record_id
        self.diagnosis = diagnosis
        self.treatment = treatment

    def __str__(self):
        return f"[Record {self.record_id}] Diagnosis: {self.diagnosis}, Treatment: {self.treatment}"


class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.records = []  # Composition: Patient owns MedicalRecords

    def add_record(self, record):
        self.records.append(record)

    def __str__(self):
        return f"Patient {self.name} (ID: {self.patient_id}, Age: {self.age})"


class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.patients = []  # Aggregation: Doctor has patients, but doesn't own them

    def assign_patient(self, patient):
        self.patients.append(patient)

    def __str__(self):
        return f"Dr. {self.name} (ID: {self.doctor_id}, Specialty: {self.specialty})"


class Department:
    def __init__(self, name):
        self.name = name
        self.doctors = []  # Composition: Department owns Doctors

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def __str__(self):
        return f"Department: {self.name}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.departments = []  # Composition: Hospital owns Departments

    def add_department(self, department):
        self.departments.append(department)

    def find_patient(self, patient_id):
        for dept in self.departments:
            for doc in dept.doctors:
                for patient in doc.patients:
                    if patient.patient_id == patient_id:
                        return patient
        return None

    def display_structure(self):
        print(f"Hospital: {self.name}")
        for dept in self.departments:
            print(f" - {dept}")
            for doc in dept.doctors:
                print(f"    - {doc}")
                for patient in doc.patients:
                    print(f"       - {patient}")
                    for record in patient.records:
                        print(f"           - {record}")


# Example usage
if __name__ == "__main__":
    # Create hospital
    hospital = Hospital("City General Hospital")

    # Create departments
    cardiology = Department("Cardiology")
    neurology = Department("Neurology")

    # Create doctors
    doc_smith = Doctor(1, "Smith", "Cardiologist")
    doc_lee = Doctor(2, "Lee", "Neurologist")

    # Add doctors to departments
    cardiology.add_doctor(doc_smith)
    neurology.add_doctor(doc_lee)

    # Add departments to hospital
    hospital.add_department(cardiology)
    hospital.add_department(neurology)

    # Create patients
    patient_a = Patient(101, "Alice", 30)
    patient_b = Patient(102, "Bob", 45)

    # Assign patients to doctors
    doc_smith.assign_patient(patient_a)
    doc_lee.assign_patient(patient_b)

    # Add medical records to patients
    patient_a.add_record(MedicalRecord(1, "Hypertension", "Medication"))
    patient_b.add_record(MedicalRecord(2, "Migraine", "Rest and medication"))

    # Display the whole hospital structure
    hospital.display_structure()
