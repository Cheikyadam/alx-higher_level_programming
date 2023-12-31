#!/usr/bin/python3
"""Base classe"""
import json


class Base:
    """A base classe for the project

    Attributes:
        __nb_objects (int): to count object
        id (int): the id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ To init an object

        Parameters:
            id (int): to identify the object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str([])
        return str(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """to save a rectangle or square to a file"""
        if list_objs is None or len(list_objs) == 0:
            to_save = str([])
        else:
            to_save = []
            for obj in list_objs:
                to_save.append(obj.to_dictionary())
            to_save = Base.to_json_string(to_save)

        classname = str(cls)
        if "Rectangle" in classname:
            name = "Rectangle.json"
        else:
            name = "Square.json"
        with open(name, 'w', encoding="utf-8") as f:
            f.write(to_save)

    def from_json_string(json_string):
        """
        From json string

        Returns:
            list representation of json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creating form a dictionary"""
        classname = str(cls)
        if "Rectangle" in classname:
            dum = cls(5, 4)
        else:
            dum = cls(5)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """Load from json"""
        classname = str(cls)
        if "Rectangle" in classname:
            name = "Rectangle.json"
        else:
            name = "Square.json"
        try:
            with open(name, 'r', encoding='utf-8') as f:
                in_file = f.read()
            from_json = Base.from_json_string(in_file)
            instances = []
            for obj in from_json:
                instances.append(cls.create(**obj))
            return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """to save a rectangle or square to a file csv format"""

        classname = str(cls)
        if "Rectangle" in classname:
            name = "Rectangle.csv"
            if list_objs is None or len(list_objs) == 0:
                to_save = ""
            else:
                to_save = ""
                for obj in list_objs:
                    to_save += str(obj.id) + ","
                    to_save += str(obj.width) + ","
                    to_save += str(obj.height) + ","
                    to_save += str(obj.x) + ","
                    to_save += str(obj.y) + "\n"
        else:
            name = "Square.csv"
            if list_objs is None or len(list_objs) == 0:
                to_save = ""
            else:
                to_save = ""
                for obj in list_objs:
                    to_save += str(obj.id) + ","
                    to_save += str(obj.size) + ","
                    to_save += str(obj.x) + ","
                    to_save += str(obj.y) + "\n"

        with open(name, 'w', encoding="utf-8") as f:
            f.write(to_save)

    @classmethod
    def load_from_file_csv(cls):
        """Load from json"""
        classname = str(cls)
        if "Rectangle" in classname:
            name = "Rectangle.csv"
        else:
            name = "Square.csv"
        try:
            with open(name, 'r', encoding='utf-8') as f:
                in_file = f.read()
            instances = []
            if len(in_file) == 0 or in_file is None:
                return instances
            else:
                in_file = in_file[:-1]
                in_file_list = in_file.split("\n")
                for obj in in_file_list:
                    cur = obj.split(",")
                    if "Rectangle" in name:
                        instances.append(cls(int(cur[1]), int(cur[2]), int(
                            cur[3]), int(cur[4]), int(cur[0])))
                    else:
                        instances.append(cls(int(
                            cur[1]), int(cur[2]), int(cur[3]), int(cur[0])))
                return instances
        except FileNotFoundError:
            return []
