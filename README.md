# Shell AI

A lightweight AI-powered terminal assistant built with `AgentKit`: currently private

Shell AI provides an interactive terminal interface with streaming responses, Markdown rendering, and persistent conversation context during each session.

## Features

- Interactive terminal UI powered by Prompt Toolkit.
- Markdown-rendered responses using Rich.
- Real-time streaming through AgentKit.
- Tool calling support.
- Session-based conversation context.
- Global and project-level environment configuration.
- Run via cloudflare tunnel.

## Installation

```bash
uv tool install .
```

## Configuration

Create a global environment file:

```bash
mkdir -p ~/.config/shell-ai
touch ~/.config/shell-ai/.env
```

Add env keys:

```env
GOOGLE_API_KEY=your_google_api_key
RELAY_URL=your_relay_url
```

## Usage

Start the assistant:

```bash
shai
```

Type your messages and interact with the assistant. Enter `exit` or `quit` to leave.

## Development

Clone the repository and install dependencies:

```bash
uv sync
uv run shai
```

After making changes, reinstall the CLI:

```bash
uv tool install .
```

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- AgentKit

## License

MIT