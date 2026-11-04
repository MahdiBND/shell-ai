import uuid
from .tui import TerminalUI
from .loadenv import loadenv, current_path


def run(args, bot):
    path, context = setup_space(args)

    agent = bot.init(output_directory=path, additional_context=context)
    session_id = new_session_id()

    loop = not args.exec
    query = args.query

    if loop:
        start_tui(agent, session_id)
    else:
        run_once(agent, query)


def setup_space(args):
    loadenv()

    path = args.path or current_path
    context = args.input or ""

    return (path, context)


def new_session_id():
    return str(uuid.uuid4())


def run_once(agent, query):
    ui = TerminalUI()
    ui.show_exec_ui()

    try:
        stream(query, ui, agent)
    except Exception as exc:
        ui.show_error(str(exc))
    finally:
        ui.show_goodbye()


def start_tui(agent, session_id=None):
    """Start the interactive Shell AI session."""

    try:
        ui = TerminalUI()
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
        query = ui.prompt()

        if query is None:
            break

        if not query:
            continue

        try:
            stream(query, ui, agent, session_id)

        except KeyboardInterrupt:
            ui.show_info("Response interrupted.")
            continue


def stream(query, ui, agent, session_id=None):
    try:
        stream = agent.stream(query, session_id=session_id)
        ui.render_response(stream)

    except Exception as exc:
        ui.show_error(str(exc))
