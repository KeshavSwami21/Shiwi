from datetime import date
from enum import Enum
from uuid import uuid4
from dataclasses import dataclass
from skills import factory
from ai import AI

class Status(Enum):
    """ The Todo Statuses """
    NOT_STARTED = 0
    IN_PROGRESS =  1
    COMPLETED = 2

class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

class Item():
    __creation_date = date.today()
    __title = "empty"
    __status = Status.NOT_STARTED
    __priority = Priority.LOW
    __flag = False 
    __url = ""
    __due_date = date
    __icon = ""
    __state = False
    __notes = ""

    def __init__(self, title:str=None):
        if title is not None:
            self.__title = title
        self.__id = str(uuid4())

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value:str):
        self.__title = value

    @property
    def priority(self):
        return self.__priority.name
    
    @priority.setter
    def priority(self, value:Priority):
        self.__priority = value

    @property
    def creation_date(self):
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value):
        self.__creation_date = value

    @property
    def age(self):
        return self.__creation_date - date.today()
    
    @property
    def status(self):
        return self.__status.name
    @status.setter
    def status(self, value:Status):
        self.__status = value

    @property
    def id(self):
        return self.__id
    
    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, value:bool):
        self.__flag = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value:str):
        self.__url = value
    
    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value:date):
        self.__due_date = value
    
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, value:str):
        self.__icon = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value:bool):
        self.__state = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value:str):
        self.__value = value

class Todo():
    __todos = []

    def __init__(self):
        print("new todo list created")
        self._current = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < len(self.__todos) -1 :
            self._current += 1
            print(self.__todos[self._current].title)
            return self.__todos[self._current]
        else:
            self._current = -1
        raise StopIteration

    def __len__(self):
        """ Returns the number of items in the Todo List """
        return len(self.__todos)


    def new_item(self, item:Item):
        self.__todos.append(item)
    
    @property
    def items(self)->list:
        return self.__todos

    def show(self):
        print("*"*80)
        for item in self.__todos:
            print(item.title, item.status, item.priority, item.age)
        
    @classmethod
    def show(cls):
        print("*"*80)
        print("Todo Items")
        print('*'*80)
        count = 1
        if len(cls.__todos) == 0:
            print("No items in list!")
        else:
            for item in cls.__todos:
                print(count, item.title, item.status, item.priority, item.age, item.id)
                count += 1 
            print("")

    def remove_item(self, uuid:str=None, title:str=None)->bool:
        if title is None and uuid is None:
            print("You need to provide some details for me to remote it, either UUID or title")
        if uuid is None and title:
            for item in self.__todos:
                if item.title == title:
                    # del self.__todos[item
                    self.__todos.remove(item)  
                    return True
            print("Item with title", title, 'not found')
            return False
        if uuid:
            self.__todos.remove(uuid)
            return True
    
@dataclass
class Todo_skill():
    name = 'todo_skill'

    def commands(self, command:str):
        return ["add to-do","add to do", "add item","list todos", "list todo", "list to do", 
                "list to-do", "list to do's",'list items',"remove todo", 
                "remove item", "mark done", "remove todos", "remove to-do", "remove to do's"]

    def handle_command(self, command:str, ai:AI):
        if command in ["add to-do","add to do", "add item"]:
            add_todo()
        command = ""
        if command in ["list todos", "list todo", "list to do", "list to-do", "list to do's",'list items']:
            list_todos()
        command = ""
        if command in ["remove todo", "remove item", "mark done", "remove todos", "remove to-do", "remove to do's"]:
            remove_todo()
        return command

def initialize():
    factory.register('jokes_skill', Jokes_skill)
    print("Jokes Skill initialized")

todo = Todo()

def add_todo(shiwi:AI)->bool:
    item = Item()
    shiwi.say("Tell me what to add to the list")
    try:
        item.title = shiwi.listen()
        todo.new_item(item)
        message = "Added " + item.title
        shiwi.say(message)
        return True
    except:
        print("oops there was an error")
        return False
    
def list_todos(shiwi:AI):
    if len(todo) > 0:
        shiwi.say("Here are your to do's")
        for item in todo:
            shiwi.say(item.title)
    else:
        shiwi.say("The to do list is empty!")

def remove_todo(shiwi:AI)->bool:
    shiwi.say("Tell me which item to remove")
    try:
        item_title = shiwi.listen()
        todo.remove_item(title=item_title)
        message = "Removed " + item_title
        shiwi.say(message)
        return True
    except:
        print("opps there was an error")
        return False