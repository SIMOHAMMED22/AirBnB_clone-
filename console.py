#!/usr/bin/python3
# Program contains the entry point of the command interpreter
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNB Command class"""

    prompt = '(hbnb) '

    cls = {'BaseModel': BaseModel, "User": User, "Place": Place,
           "Amenity": Amenity, "City": City,
           "Review": Review, "State": State}

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if len(line) == 0:
            print('** class name missing **')
            return

        if line in self.cls:
            obj = self.cls[line]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if len(line) == 0:
            print('** class name missing **')
            return

        twc = line.split()

        if len(twc) != 2:
            print('** instance id missing **')
            return
        else:
            if twc[0] in self.cls:
                key = twc[0] + '.' + twc[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
                    return
            else:
                print("** class doesn't exist **")
                return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if len(line) == 0:
            print('** class name missing **')
            return

        twc = line.split()
        if len(twc) != 2:
            print('** instance id missing **')
            return
        else:
            if twc[0] in self.cls:
                key = twc[0] + '.' + twc[1]
                if key in storage.all():
                    del(storage.all()[key])
                    storage.save()
                else:
                    print("** no instance found **")
                    return
            else:
                print("** class doesn't exist **")
                return

    def do_all(self, line):
        """Prints all instances based or not on the class name"""
        arr = []
        if len(line) == 0:
            for key in storage.all():
                arr.append(str(storage.all()[key]))
            print(arr)
            return
        else:
            for key in storage.all():
                if storage.all()[key].__class__.__name__ == line:
                    arr.append(str(storage.all()[key]))

            if arr == []:
                print("** class doesn't exist **")
                return
            else:
                print(arr)

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """just a new line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
