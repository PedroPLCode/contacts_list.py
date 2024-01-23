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
            raise ValueError(f"Value {value} exceeds label_length of {self.label_length}")
       
    def __str__(self):
        return ("Private contact\n"
                f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Mobile number: {self.mobile_number}\n"
                f"Email address: {self.email_address}\n")
       
    def __repr__(self):
        return (f"Index: {self.index}\n"
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
              f"Tel prywatny: {self.mobile_number}\n")
    
    
    
    
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
        return (f"Index: {self.index}\n"
                f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Job title: {self.job_title}\n"
                f"Comapny name: {self.company_name}\n"
                f"Mobile number: {self.mobile_number}\n"
                f"Work number: {self.work_phone}\n"
                f"Email address: {self.email_address}\n"
                f"Full name length: {self.label_length}\n")
        
    def contact(self):
        print(f"Kontaktuję się z {self.first_name} {self.last_name}\n"
              f"Tel służbowy: {self.work_phone}\n")




def create_contacts(contact_type='private', how_many=1):
    if contact_type == 'private':
        create_multiple_base_contact_instances(contacts_list, how_many)
    elif contact_type == 'bussiness':
        create_multiple_bussiness_contact_instances(contacts_list, how_many)
    else:
        print("Error. Wrong contant type.")
       
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
    return BaseContact(index_in_array,
                  fake.first_name(),
                  fake.last_name(),
                  fake.phone_number(),
                  fake.email(),)
    
def create_multiple_base_contact_instances(array, how_many=1):
    for index in range(0, how_many):
        array.append(create_fake_base_contact_instance(index))
        
def create_multiple_bussiness_contact_instances(array, how_many=1):
    for index in range(0, how_many):
        array.append(create_fake_bussiness_contact_instance(index))
        
def show_persons_in_array(array):
    for person in array:
        print(person)
        
        
        
create_contacts('private', 512)
create_contacts('bussiness', 128)
show_persons_in_array(contacts_list)

by_first_name = sorted(contacts_list, key=lambda person: person.first_name)
by_last_name = sorted(contacts_list, key=lambda person: person.last_name)
by_email_address = sorted(contacts_list, key=lambda person: person.email_address)
by_mobile_number = sorted(contacts_list, key=lambda person: person.mobile_number)
