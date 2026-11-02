"""Simple chat CLI for agentkit.

Keeps conversation history while the program runs, streams the reply,
and exits on 'exit' / 'quit' (or Ctrl+C / Ctrl+D).
"""

import uuid

from .loadenv import global_path, load_dotenv

load_dotenv(global_path)

# from assistant import build_assistant
from shell_ai import build_assistant
from .typing import typing_disabled

# from agentkit import configure_logging
# configure_logging()        # or configure_logging("DEBUG")

EXIT_WORDS = {"exit", "quit"}


def main() -> None:
    agent = build_assistant()
    session_id = str(uuid.uuid4())

    print("Chat started. Type 'exit' or 'quit' to leave.\n")

    while True:
        try:
            user_input = input("you> ").strip()
        except EOFError, KeyboardInterrupt:
            print()
            break

        if not user_input:
            continue
        if user_input.lower() in EXIT_WORDS:
            break

        try:
            with typing_disabled():
                stream = agent.stream(user_input, session_id=session_id)
                respond(stream)
        except KeyboardInterrupt:
            print("\n(interrupted)")
            break

        print("\n")

    print("Bye!")


def respond(stream):
    print("agent> ", end="", flush=True)
    streamed_text = False

    for e in stream:
        if e.type == "text":
            streamed_text = True
            print(e.text, end="", flush=True)
        elif e.type == "tool_call":
            print(f"\n[calling {e.name}]\nagent> ", end="", flush=True)
        elif e.type == "final" and not streamed_text:
            # e.g. structured output: nothing streamed token by token
            print(e.output, end="", flush=True)


if __name__ == "__main__":
    main()
