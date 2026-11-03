"""Shell Script Agent for agentkit: write scripts"""

from __future__ import annotations

from agentkit import InMemorySessionStore, new_agent

from ..prompts.shell_agent import SYSTEM_PROMPT
from ..tools.shell_agent import write_new_file


def build_assistant(session_store=None):
    """Create the assistant. Keeps chat history for as long as the store lives."""
    return new_agent(
        SYSTEM_PROMPT,
        tools=[write_new_file],
        session_store=session_store or InMemorySessionStore(),
    )
