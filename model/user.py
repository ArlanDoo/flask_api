class User:

    def __init__(self, first_name: str, second_name: str, age: int, email: str):
        self.first_name = first_name
        self.second_name = second_name
        self.full_name = f'{first_name} {Second_name}'
        self.age = age
        self.email = email