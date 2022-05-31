import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(
        screen_width / 2)  # Places the Player in the middle of the screen, the int() ensures TCOD doesn't throw an error in case of a float
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    event_handler = EventHandler()

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
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)  # Updates the screen

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
