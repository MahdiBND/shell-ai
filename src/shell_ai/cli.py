"""Shell AI command-line entry point."""

from agentkit import configure_logging

from .arg_parser import parse_args
from .bots import assistant, dev
from .runner import run


def main() -> None:
    args = parse_args()

    # set dev mode
    agent = dev if args.dev else assistant

    if args.verbose:
        configure_logging()

    run(args, agent)


if __name__ == "__main__":
    main()
