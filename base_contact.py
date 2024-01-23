class BaseContact:
    
    def __init__(self, index, first_name, last_name, mobile_number, email_address):
        self.index = index
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.email_address = email_address
        self._label_length = len(f"{first_name} {last_name}")
        
    @property
    def label_length(self):
        return self._label_length
    
    @label_length.setter
    def label_length(self, value):
        if value <= self.label_length:
            self.label_length = value
        else:
            raise ValueError(f"Value {value} exceeds label_length {self.label_length}")
       
    def __str__(self):
        return ("Private contact\n"
                f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Mobile number: {self.mobile_number}\n"
                f"Email address: {self.email_address}\n")
       
    def __repr__(self):
        return ("Private contact\n"
                f"Index: {self.index}\n"
                f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Mobile number: {self.mobile_number}\n"
                f"Email address: {self.email_address}\n"
                f"Full name length: {self.label_length}\n")
        
    def __eq__(self, other):
        return all (
            (
                self.first_name == other.first_name,
                self.last_name == other.last_name,
            )
        )
        
    def contact(self):
        print(f"Kontaktuję się z {self.first_name} {self.last_name}\n"
              f"Tel PRYWATNY: {self.mobile_number}\n")