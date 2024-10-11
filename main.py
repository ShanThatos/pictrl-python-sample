import time

from faker import Faker

fake = Faker()

while True:
    print(fake.name())
    time.sleep(5)