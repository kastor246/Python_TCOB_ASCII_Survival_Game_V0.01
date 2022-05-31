import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler


def main() -> None:
    screen_width = 100
    screen_height = 70

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="ASCII Game V0.01",
            vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height,
                                    order="F")  # Creates our "console" which is what we draw to.
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()


if __name__ == "__main__":
    main()
