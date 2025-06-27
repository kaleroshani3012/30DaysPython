from pydantic import BaseModel, EmailStr, field_validator, ValidationError

class UserData(BaseModel):
    name : str
    email : EmailStr
    age : int

    @field_validator('age')
    @classmethod
    def age_validate(cls, v):
        if not 18<= v <=100:
            raise ValueError("Age must be between 18 - 100")
        return v


in_name = input("Enter your Name: ")
in_email = input("Enter Email id: ")

try:
    in_age = int(input("Enter your Age: "))
except ValueError:
    print("Age must be in number.")
    exit()


try:
    user = UserData(name = in_name, email = in_email, age = in_age)
    print("Valid User Profile")
    print(user.model_dump_json(indent=4))

except ValidationError as e:
    print("Validation Error")
    print(e.json(indent=4))