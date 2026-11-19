###
# Writes patient data to a JSON file
#
import json                                    # moduł do plików JSON

# Dane pacjenta to słownik, w którym są kolejne słowniki i listy (tak jak w pliku JSON).
data = {
    "patient_record": {
        "patient_id": "P001234",
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1985-05-15",
        "gender": "Male",
        "contact_info": {
            "phone_number": "+1-555-123-4567",
            "email": "johndoe@example.com",
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA"
            }
        },
        "medical_history": {
            "allergies": ["Penicillin", "Peanuts"],
            "current_medications": ["Lisinopril 10mg", "Metformin 500mg"],
            "past_illnesses": ["Hypertension", "Type 2 Diabetes"],
            "surgeries": [
                {
                    "surgery_type": "Appendectomy",
                    "date": "2015-08-20"
                }
            ]
        }
    }
}                                              # cały rekord pacjenta

# Specify the file path and name
file_name = "patient.json"                     # nazwa pliku, który powstanie

# Open the file in write mode and use json.dump() to write the data to the file
with open(file_name, 'w') as file:             # otwieramy plik do zapisu
    json.dump(data, file, indent=4)            # zapisujemy słownik jako JSON; indent=4 robi wcięcia, żeby plik był czytelny

print("Data has been written to", file_name)   # informujemy, że zapis się udał
