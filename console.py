#!/usr/bin/python3
""" The command line interpreter for the AIRBNB project """
import cmd, sys
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """A command line interpreter"""

    prompt = '(hbnb) '
    
    project_classes = ["User", "State", "City", "Place", "BaseModel"]

    def do_create(self, line):
        """create an instance of baseModel"""
        instance_obj = line.split(" ")
        if not line:
            print("** class name missing **")
        elif instance_obj[0] not in HBNBCommand.project_classes:
            print ("** class doesn't exist **")
        elif instance_obj[0] == "BaseModel":
            new_instance = BaseModel()
            
            #save the instance to json file
            new_instance.save()
            print(new_instance.id)
            storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance based on the
            class name and id
        """
        all_objec = storage.all()
        instance_obj = line.split(" ")
        if not line:
            print("** class name missing **")
        elif instance_obj[0] not in HBNBCommand.project_classes:
            print("** class doesn't exist **")
        elif len(instance_obj) < 2:
            print("** instance id missing **")
        else:
            # Removing quotes if present in the ID
            # Checking if the ID starts and ends with quotes
            if instance_obj[1].startswith('"') and insatnce_obj[1].endswith('"'):
                # Remove the quotes
                instance_obj[1] = instance_obj[1][1:-1]
            # Creating a unique identifier for the instance
            class_id = instance_obj[0] + "." + instance_obj[1]

            # Checking if the instance exists in the storage
            if class_id not in all_objec.keys():
                print("** no instance found **")
            else:
                print(all_objec[class_id])
 
    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id (save the change into
            the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        all_objec = storage.all()
        instance_obj = line.split(" ")
        if not line:
            print("** class name missing **")
        elif instance_obj[0] not in HBNBCommand.project_classes:
            print("** class doesn't exist **")
        elif len(instance_obj) < 2:
            print("** instance id missing **")
        else:
            if instance_obj[1].startwith('"') and instance_obj.endwith('"'):
                instance_obj[1] = instance_obj[1][1:-1]
            class_id = instance[0] + "." + instance_obj[1]

            if class_id not in all_objec.keys():
                print(" ** no instance found **")
            else:
                del all_objec[class_id]
                storage.save()
    
    def do_all(self, line):
        """
            Prints all string representation of all instances based or not on the
            class name. Ex: $ all BaseModel
        """
        all_object = storage.all()
        instance_obj = line.split(" ")

        if instance_obj not in HBNBCommand.project_classes:
            print("** class doesn't exist **")
        else:
            

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """ Handle the end-of-file condition (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
