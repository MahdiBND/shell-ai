"""Shell AI command-line entry point."""

import uuid

from .loadenv import global_path, load_dotenv

load_dotenv(global_path)

from .assistant import build_assistant
from .tui import TerminalUI


def main() -> None:
    """Start the interactive Shell AI session."""

    ui = TerminalUI()

    try:
        agent = build_assistant()
        session_id = str(uuid.uuid4())

        ui.show_welcome()

        input_loop(ui, agent, session_id)

    except KeyboardInterrupt:
        pass

    except Exception as exc:
        ui.show_error(str(exc))

    finally:
        ui.show_goodbye()


def input_loop(ui, agent, session_id):
    while True:
        user_input = ui.prompt()

        if user_input is None:
            break

        if not user_input:
            continue

        try:
            # AgentKit streaming API
            stream = agent.stream(
                user_input,
                session_id=session_id,
            )

            ui.render_response(stream)

        except KeyboardInterrupt:
            ui.show_info("Response interrupted.")
            continue

        except Exception as exc:
            ui.show_error(str(exc))


if __name__ == "__main__":
    main()
