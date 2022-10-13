import sys
import xml.etree.ElementTree as ET
import json
import xml


#Напишите классы для предметной области пассажирский транспорт. Возможные классы: автобус и самолёт.
#В 4-м и 5-м пунктах хранение объектов одного класса реализовать в формате JSON, другого − в формате XML.

class ErrorValues(Exception):
    message = "Value can't be negative"

class Bus: 
    def __init__ (self, id: int, capacity: int, passengers: int, length: int):
        self.id = id
        self.capacity = capacity
        self.passengers = passengers
        self.length = length

    def BusGo(self):
        print("Bus " + self.id + "is going")


class Airplane:
    def __init__(self, id:str, mass:int, number_of_engines:int):
        self.id = id
        self.mass = mass
        self.number_of_engines = number_of_engines

    def fly(self):
        print("Airplane " + self.id + "is flying")


class Magic:
    @staticmethod
    def go_to_XML(airplans):
        try:
            root = ET.Element("Airplane")
            for it in airplans:
                idAir = ET.Element(it.id)
                mAir = ET.SubElement(idAir, "Mass")
                mAir.text = str(it.mass)
                engAir = ET.SubElement(idAir, "Number_of_engines")
                engAir.text = str(it.number_of_engines)
                root.append(idAir)

            s = ET.tostring(root, encoding="utf-8", method="xml")
            s = s.decode("UTF-8")
            with open(f"airplanes.xml", "w") as wf:
                wf.write(s)
        except Exception as e:
            print(e)

    @staticmethod
    def go_to_airplane(path: str = "airplanes.xml"):
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            arr = []
            for it in root:
                arr.append(Airplane(it.tag, int(it[0].text), int(it[1].text)))
            return arr
        except FileNotFoundError:
            print("File not found")
        except xml.etree.ElementTree.ParseError:
            print("Error on file")
        except Exception as e:
            print(e)

    @staticmethod
    def go_to_json(buses):
        try:
            with open("buses.json", "w") as wf:
                data = {}
                bus = {}
                for it in buses:
                    bus[it.id] = it.__dict__
                data["Bus"] = bus
                json.dump(data, wf, indent = 4)
        except Exception as e:
            print(e)

    @staticmethod
    def go_to_bus(path:str = "buses.json"):
        try:
            with open(path, 'r') as rf:
                 data = json.load(rf)
                 arr = []
                 for it in data["Bus"]:
                    arr.append(Bus(it, int(data["Bus"][it]["capacity"]), int(data["Bus"][it]["passengers"]), int(data["Bus"][it]["length"])))
            return arr
        except json.JSONDecodeError:
            print("Error on file")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(e)


class For_user:

    buses = []
    airplanes = []

    @staticmethod
    def create_bus():
        print("Write: id, capacity(int), passengers(int), length(int)")
        try:
            id = input()
            capacity = int(input())
            if(capacity<=0):
                raise ErrorValues
            passengers = int(input())
            if(passengers<0):
                raise ErrorValues
            length = int(input())
            if(length<=0):
                raise ErrorValues
            For_user.buses.append(Bus(id, capacity, passengers, length))
        except AttributeError:
            print("Attribute error")
        except ErrorValues as e:
            print(e.message)
        except TypeError:
            print("Incorected value")
        except Exception as e:
            print(e)

    @staticmethod
    def create_airplane():
        print("Write: id, capacity(int), passengers(int), length(int)")
        try:
            id = input()
            mass = int(input())
            if mass <= 0:
                raise ErrorValues
            number_of_engines = int(input())
            if number_of_engines <= 0:
                raise ErrorValues
            For_user.airplanes.append(Airplane(id, mass, number_of_engines))
        except ErrorValues as e:
            print(e.message)
        except AttributeError:
            print("Attribute error")
        except TypeError:
            print("Incorected value")
        except Exception as e:
            print(e)

    @staticmethod
    def createJSON():
        Magic.go_to_json(For_user.buses)

    @staticmethod
    def createXML():
        Magic.go_to_XML(For_user.airplanes)

    @staticmethod
    def create_bus_from_json():
        print("Write path")
        path = input()
        arr = []
        arr = Magic.go_to_bus(path)
        if type(arr) == list:
            For_user.buses = For_user.buses + arr

    @staticmethod
    def create_airplane_from_xml():
        print("Write path")
        path = input()
        arr = []
        arr = Magic.go_to_XML(path)
        if type(arr) == list:
            For_user.airplanes = For_user.airplanes + arr

    @staticmethod
    def print_all_transport():
        print("Buses:")
        for it in For_user.buses:
            print(it.__dict__)
        print("\nAirplanes:")
        for it in For_user.airplanes:
            print(it.__dict__)

    @staticmethod
    def menu():
        while True:
            print("Enter: 1 - create bus;  2 - create airplane;  3 - create JSON;  4 - create XML;")
            print("5 - create bus from JSON;  6 - create airplane for XML;  7 - print all transport;  8 - close")
            s = input()
            if s == '1':
                For_user.create_bus()
            elif s == '2':
                For_user.create_airplane()
            elif s == '3':
                For_user.createJSON()
            elif s == '4':
                For_user.createXML()
            elif s == '5':
                For_user.create_bus_from_json()
            elif s == '6':
                For_user.create_airplane_from_xml()
            elif s == '7':
                For_user.print_all_transport()
            elif s == '8':
                sys.exit()



For_user.menu()
