class Contact:
    def __init__(self, name, email, age):
        self.name = name  # Assign name to the instance
        self.email = email
        self.age = age
        self.validate()  # Validate the contact details

    def validate(self):
        Contact.validate_name(self.name)
        Contact.validate_email(self.email)
        Contact.validate_age(self.age)

    def validate_name(name):
        if len(name) > 50:
            raise ValueError('Name is too large!')

    def validate_email(email):
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email!')

    def validate_age(age):
        try:
            age = int(age)  # Python will raise ValueError if not numeric
            if age <= 0:
                # We ask Python to raise ValueError if <= 0
                raise ValueError
        except ValueError:
            raise ValueError('Invalid age!')

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"
