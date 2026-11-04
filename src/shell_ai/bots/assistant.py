"""Personal assistant for agentkit: simple Q&A, one tool (get_current_time)."""

from __future__ import annotations

from agentkit import InMemorySessionStore, new_agent

from ..tools.assistant import get_current_time
from ..prompts.assistant import SYSTEM_PROMPT


def init(
    instructions=SYSTEM_PROMPT,
    tools=[get_current_time],
    session_store=InMemorySessionStore(),
):
    return new_agent(instructions, tools=tools, session_store=session_store)
