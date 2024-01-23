from base_contact import BaseContact
from bussiness_contact import BusinessContact
from faker import Faker

fake = Faker()
contacts_list = []

def create_contacts(array, contact_type='private', how_many=1):
    if contact_type == 'private' or contact_type == 'bussiness':
        for index in range(0, how_many):
            array.append(
                create_fake_base_contact_instance(index) if contact_type == 'private' 
                else create_fake_bussiness_contact_instance(index)
                )    
    else:
        print("Error. Wrong contact type. Only private or bussiness.")

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
