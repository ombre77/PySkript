# this file is for class like Player, Block or Entity that serve for other class in the lib
class Entity:
    uuid: str
    location: "Location"
    world: "World"
    healt: float

    def kill(self,reason="void") -> None : ...

class Player(Entity):
    name: str
    velocity: "Vector"
    inventory: "Inventory"
    tool: "Item"
    offhand_item: "Item"


class Block:
    location: "Location"
    world: "World"
    name: str

class Position:
    location: "Location"
    direction: "Vector"
    world: "World"

class Location:
    x: float
    y: float
    z: float

class Vector:
    x: float
    y: float
    z: float

    def length(self) -> float: ...
    def normalize(self) -> "Vector": ...
    def dot(self, other: "Vector") -> float: ...
    def cross(self, other: "Vector") -> "Vector": ...

class World:
    name:str

class Item:
    name: str
    amount: int

class Inventory:
    size: int

    def clear(self) -> None: ...

    def add_item(self, item: Item) -> None: ...

    def remove_item(self, item: Item) -> None: ...

    def getitem(self, slot: int) -> Item: ...

    def setitem(self, slot: int, item: Item) -> None: ...