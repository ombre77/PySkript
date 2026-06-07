from typing import Callable, Any

# this file is for events decorator like @pyskript.events.on_break

EventHandler = Callable[..., Any]

def on_load(func: EventHandler) -> EventHandler:
    """Called when the script is loaded."""
    return func

def on_join(func: EventHandler) -> EventHandler:
    """Called when a player joins."""
    return func

def on_quit(func: EventHandler) -> EventHandler:
    """Called when a player leaves."""
    return func

def on_break(func: EventHandler) -> EventHandler:
    """Called when a player breaks a block."""
    return func

def on_place(func: EventHandler) -> EventHandler:
    """Called when a player places a block."""
    return func

def on_command(func: EventHandler) -> EventHandler:
    """Called when a command is executed."""
    return func

def on_respawn(func: EventHandler) -> EventHandler:
    """Called when a player respawns."""
    return func
