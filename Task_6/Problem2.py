from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    
    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
    
    def display_info(self):
        age = self.calculate_age()
        print(f"Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')}")
        print(f"Age: {age}")

# Example
person_one = Person("Ferdi Odilia", "France", "1963-07-12")
print("Person_one:")
person_one.display_info()