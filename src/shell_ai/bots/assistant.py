"""Personal assistant for agentkit: simple Q&A, one tool (get_current_time)."""

from __future__ import annotations

from agentkit import InMemorySessionStore, new_agent

from ..tools.assistant import get_current_time
from ..prompts.assistant import SYSTEM_PROMPT


def build_assistant(session_store=None):
    """Create the assistant. Keeps chat history for as long as the store lives."""
    return new_agent(
        SYSTEM_PROMPT,
        tools=[get_current_time],
        session_store=session_store or InMemorySessionStore(),
    )
