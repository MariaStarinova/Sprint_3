from faker import Faker

def generate():
    fake = Faker()

    name = fake.name()
    email = fake.email()
    password = fake.password(length=6)

    return name, email, password


name, email, password = generate()

