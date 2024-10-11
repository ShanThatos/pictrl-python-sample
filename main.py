import time

from faker import Faker

fake = Faker()

while True:
    print(fake.name(), fake.email(), fake.phone_number())
    time.sleep(5)