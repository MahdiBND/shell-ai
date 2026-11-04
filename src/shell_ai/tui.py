"""Terminal user interface for Shell AI."""

from collections.abc import Iterable
from typing import Any

from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.history import InMemoryHistory
from rich.console import Console
from rich.live import Live


from .markdown import StreamingMarkdown


class TerminalUI:
    """Interactive terminal interface."""

    def __init__(self) -> None:
        self.console = Console()
        self.session = PromptSession(history=InMemoryHistory())

    def prompt(self) -> str | None:
        """Get user input. Return None when the user exits."""
        try:
            value = self.session.prompt(
                [("class:prompt", "> ")],
                style=Style.from_dict(
                    {
                        "prompt": "#3498db bold",
                    }
                ),
            ).strip()

            if value.lower() in {"exit", "quit"}:
                return None

            return value

        except KeyboardInterrupt, EOFError:
            return None

    def render_response(self, stream: Iterable[Any]) -> None:
        """Render an AgentKit response with live Markdown updates."""

        response = StreamingMarkdown()
        streamed_text = False

        with Live(
            response,
            console=self.console,
            refresh_per_second=30,
            auto_refresh=True,
            transient=False,
            vertical_overflow="visible",
        ):
            for event in stream:
                if event.type == "text":
                    streamed_text = True
                    response.append(event.text)

                elif event.type == "tool_call":
                    self.console.print(f"\n[dim]Calling tool: {event.name}[/dim]\n")

                elif event.type == "final" and not streamed_text:
                    response.append(str(event.output))

        self.console.print()

    def show_error(self, message: str) -> None:
        self.console.print(f"\n[bold red]Error:[/bold red] {message}\n")

    def show_info(self, message: str) -> None:
        self.console.print(f"\n[dim]{message}[/dim]\n")

    def show_welcome(self) -> None:
        self.console.print(
            "[dim]Clara: Type `exit`, `quit`, or `ctrl+c` to quit.[/dim]\n"
        )

    def show_exec_ui(self) -> None:
        self.console.print("[dim]`ctrl+c` to quit.[/dim]\n")

    def show_goodbye(self) -> None:
        self.console.print("\n[dim]Goodbye![/dim]")
