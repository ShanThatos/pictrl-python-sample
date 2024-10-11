import time

from faker import Faker

fake = Faker()

while True:
    print(fake.name(), fake.email())
    time.sleep(5)