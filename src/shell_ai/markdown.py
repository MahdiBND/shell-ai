from threading import Lock
from rich.console import Console, ConsoleOptions, RenderResult
from rich.markdown import Markdown


class StreamingMarkdown:
    """Thread-safe Markdown renderable for live streaming."""

    def __init__(self) -> None:
        self._parts: list[str] = []
        self._lock = Lock()

    def append(self, text: str) -> None:
        """Append incoming text without triggering a render."""
        with self._lock:
            self._parts.append(text)

    def get_content(self) -> str:
        """Return the accumulated response."""
        with self._lock:
            return "".join(self._parts)

    def __rich_console__(
        self,
        console: Console,
        options: ConsoleOptions,
    ) -> RenderResult:
        """Render Markdown when Rich refreshes the display."""
        content = self.get_content()

        if content:
            yield from console.render(Markdown(content), options)
