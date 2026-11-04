"""Personal assistant for agentkit: simple Q&A, one tool (get_current_time)."""

from __future__ import annotations

from agentkit import InMemorySessionStore, new_agent

from ..tools.assistant import get_current_time
from ..prompts.assistant import SYSTEM_PROMPT
from langchain_core.prompts import PromptTemplate


def init(
    instructions=SYSTEM_PROMPT,
    tools=[get_current_time],
    session_store=InMemorySessionStore(),
    **kwargs,
):
    prompt = PromptTemplate.from_template(instructions)
    prompt = prompt.format(**kwargs)

    return new_agent(prompt, tools=tools, session_store=session_store)
