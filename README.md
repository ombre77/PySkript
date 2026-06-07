# PySkript

PySkript is a transpiler that convert Python code into Skript scripts for the Minecraft server plugin.

## 1. Installation
Download and extract the zip or clone the git repo.
A command will be added in the future but for now, every action need to be done **inside** the PySkript folder.

## 2. Usage

### Setup

First, create a python file named `code.py` in the folder.
Write you code there (checkout the "**3. Code**" part)

### Run

Open a terminal inside the project folder and run the generator. If you use the included virtual environment, activate it first:

```bash
source .venv/bin/activate
```

Then run the generator (the current implementation reads `pyskript_test.py` by default):

```bash
python generator.py
```

After running, the generated Skript will be written to `skript.sk` in the project root.

## 3. Code

PySkript is separated into 2 functions:
- The Pyskript.py lib
- And the generator.py

The pyskript lib is here for sintax and autocompletion while the generator does the translation between Py and Sk.
One cannot work without the other!

### How to use?
In the `code.py` file you created earlier, you can write a python programm that will be translated into skript.

The following guide is here to help you writing it.

### 1.Events
In Sk, the code follow a simple rule:
```skript
on (event name):
 (code)
```
and that's all.

To recreate this in python, you need to use one of the **events decorator** :
```python
import pyskript

@pyskript.events.on_load
def on_load(event:pyskript.event.LoadEvent):
    pyskript.actions.send_message(pyskript.target.AllPlayers,"Skript loaded!")
```
`@pyskript.events.on_load` is what is telling to the translator "Hey thid function need to be ran when on load event!"
Your fucntion following this can be named how you want.
The code inside will be translated too.

### 2.Event class
```python
import pyskript

@pyskript.events.on_load
def on_load(event:pyskript.event.LoadEvent):
    pyskript.actions.send_message(pyskript.target.AllPlayers,"Skript loaded!")
```

In this example, `event:pyskript.event.LoadEvent` is where you get all the infos on the event like the targets (players, enitys, attacker, victim, etc...). You can then use them in your code.

### 2.1 Accessed values in Event class
Every Event class has their own attributes, heres a list:
- event.player
- event.entity
- event.block
- event.location (alias: event.pos)
    - A location contains:
        - A position (x, y and z)
        - A direction (vector)
        - A world
- event.command
    - With it, event.args
- event.sender
- event.respawn_point

### 2.2 List of Event class (and @events decorator)
- `LoadEvent` > `@skript.events.on_load`
- `JoinEvent` > `@skript.events.on_join`
- `QuitEvent` > `@skript.events.on_quit`
- `BreakEvent` > `@skript.events.on_break`
- `PlaceEvent` > `@skript.events.on_place`
- `CommandEvent` > `@skript.events.on_command`
- `RespawnEvent` > `@skript.events.on_respawn`

### 3.Global and Local vars
Whats the difference?
A Global var can be accessed in all of the code, but a local only in the event its been created.

In Sk a var is by default Global, bit if you add `_` before its name it will become a Local var.

In PySkript, a var is by default Local.
To make it Global, you need to annote it with the `pyskript.globals.GlobalVar` class.

Example:
```python
import pyskript

@pyskript.events.on_load
def on_load(event:pyskript.event.LoadEvent):
    player_count:pyskript.globals.GlobalVar #Make it global
    player_count=0

@pyskript.events.on_join
def on_join(event:pyskript.event.JoinEvent):
    player_count:pyskript.globals.GlobalVar #Make it global again
    player_count+=1
    pyskript.actions.send_message(event.player,f"Hi, {event.player.name}!")

@pyskript.events.on_quit
def on_quit(event:pyskript.event.QuitEvent):
    player_count:pyskript.globals.GlobalVar #Make it global again
    player_count-=1
```
---
Aaaand that's all for now! If this small doc wasn't enough, i rly recommand just checking the code to see how it work (its not simple, but its okay)

I will make a proper wiki and all, but for now, that is good enough.

If you have anymore questions, feel free to send me a message to my discord (@ombre77)