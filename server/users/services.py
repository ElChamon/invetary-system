import uuid
from .models import User

def createUser(name, dni, phone_number):
  id = uuid.uuid4()
  user = User(id, name, dni, phone_number)
  user.save()
