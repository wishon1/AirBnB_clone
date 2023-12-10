#!/usr/bin/python3

class User:
    @classmethod
    def show(cls, id):
        # This is a mock implementation assuming it returns some data based on the ID
        return ("ClassName", f"show({id})")

# Using the User class
command = User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")

show_command = command[1].strip("show(").strip(")").split()
print(show_command)
print(show_command[0])

class_name = command[0]
print(command[0])

obj_id = show_command[0]
class_id = class_name + "." + obj_id
print(class_id)

