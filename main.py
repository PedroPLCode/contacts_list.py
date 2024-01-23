from base_contact import BaseContact
from bussiness_contact import BusinessContact
from faker import Faker
import time

fake = Faker()

def create_contacts_and_count_time(func):
    start_time = time.perf_counter()
    def wrapper(contact_type, how_many):
        result = func(contact_type, how_many)
        return result
    end_time = time.perf_counter()
    run_time = (end_time - start_time)
    print(f"Function {func.__name__}() executed in {run_time:.6f}s")
    return wrapper

@create_contacts_and_count_time
def create_contacts(contact_type='private', how_many=1):
    if contact_type == 'private' or contact_type == 'bussiness':
        array = []
        for index in range(0, how_many):
            array.append(
                create_fake_base_contact_instance(index) if contact_type == 'private' 
                else create_fake_bussiness_contact_instance(index)
                )    
        return array
    else:
        print("Error. Wrong contact type. Only private or bussiness.")
        return False

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
    if not array:
        print("Error. Array in not iterable.")
    else: 
        for person in array:
            print(person)
    

contacts_list = create_contacts('bussiness', 1024)
show_persons_in_array(contacts_list)
