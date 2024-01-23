from base_contact import BaseContact

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