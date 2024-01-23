from faker import Faker
fake = Faker()

contacts_list = []


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
    
    
class BusinessContact(BaseContact):
    def __init__(self, job_title, company_name, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_title = job_title
        self.company_name = company_name
        self.work_phone = work_phone
        
    def __str__(self):
        return ("Bussiness contact\n"
                f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Job title: {self.job_title}\n"
                f"Comapny name: {self.company_name}\n"
                f"Work number: {self.work_phone}\n"
                f"Email address: {self.email_address}\n")
       
    def __repr__(self):
        return ("Bussiness contact\n"
                f"Index: {self.index}\n"
                f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Job title: {self.job_title}\n"
                f"Comapny name: {self.company_name}\n"
                f"Private number: {self.mobile_number}\n"
                f"Work number: {self.work_phone}\n"
                f"Email address: {self.email_address}\n"
                f"Full name length: {self.label_length}\n")
        
    def contact(self):
        print(f"Kontaktuję się z {self.first_name} {self.last_name}\n"
              f"Tel SŁUŻBOWY: {self.work_phone}\n")


def create_contacts(array, contact_type='private', how_many=1):
    if contact_type != 'private' and contact_type != 'bussiness':
        print("Error. Wrong contact type. Only private or bussiness.")
        return False
    for index in range(0, how_many):
        array.append(create_fake_base_contact_instance(index) if contact_type == 'private' 
                     else create_fake_bussiness_contact_instance(index))    

def create_fake_bussiness_contact_instance(index_in_array):
    return BusinessContact(
        fake.job(),
        fake.company(),
        fake.phone_number(),
        index_in_array,
        fake.first_name(),
        fake.last_name(),
        fake.phone_number(),
        fake.email(),
        )
    
def create_fake_base_contact_instance(index_in_array):
    return BaseContact(
        index_in_array,
        fake.first_name(),
        fake.last_name(),
        fake.phone_number(),
        fake.email(),
        )
        
def show_persons_in_array(array):
    for person in array:
        print(person)
        
        
create_contacts(contacts_list, 'private', 512)
create_contacts(contacts_list, 'bussiness', 128)
show_persons_in_array(contacts_list)
