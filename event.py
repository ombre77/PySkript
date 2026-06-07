# this file is for event classes that give information about each event and its variables

import gen.objects as objects

class Event:
    """Base class for all events."""
    pass


class LoadEvent(Event):
    """Called when the script is loaded."""
    pass


class EntityEvent(Event):
    """Base class for events involving an entity/player."""

    player: objects.Player
    entity: objects.Entity


class BlockEvent(Event):
    """Base class for block-related events."""

    player: objects.Player
    block: objects.Block
    position: objects.Position

    @property
    def loc(self):
        return self.position


class CommandEvent(Event):
    """Called when a command is executed."""

    sender: objects.Player
    command: str
    args: list[str]


class JoinEvent(EntityEvent):
    """Called when a player joins."""
    player: objects.Player


class QuitEvent(EntityEvent):
    """Called when a player leaves."""
    player: objects.Player


class RespawnEvent(EntityEvent):
    """Called when a player respawns."""
    player: objects.Player
    respawn_point: objects.Position


class BreakEvent(BlockEvent):
    """Called when a player breaks a block."""
    player: objects.Player
    block: objects.Block


class PlaceEvent(BlockEvent):
    """Called when a player places a block."""
    player: objects.Player
    block: objects.Block