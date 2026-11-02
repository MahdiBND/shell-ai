from threading import Lock
from rich.console import Console, ConsoleOptions, RenderResult
from rich.markdown import Markdown
from rich.text import Text


class StreamingMarkdown:
    """Thread-safe Markdown renderable for live streaming."""

    def __init__(self) -> None:
        self._parts: list[str] = []
        self._lock = Lock()

    def append(self, text: str) -> None:
        with self._lock:
            self._parts.append(text)

    def get_content(self) -> str:
        with self._lock:
            return "".join(self._parts)

    def __rich_console__(
        self,
        console: Console,
        options: ConsoleOptions,
    ) -> RenderResult:
        content = self.get_content()

        if not content:
            yield Text("\nDiscombobulating...", style="dim", end="\n\n")

        if content:
            yield Text("\n\nClara: ", style="bold blue", end="\n\n")
            yield Markdown(content)
            yield Text("\ndone", style="dim", end="\n\n")
