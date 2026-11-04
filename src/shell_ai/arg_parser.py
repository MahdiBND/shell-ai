import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generic argument parser demo",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        help="Input file path",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    parser.add_argument(
        "-c",
        "--exec",
        action="store_true",
        help="One Time exec",
    )

    parser.add_argument(
        "--dev",
        action="store_true",
        help="Use dev Agent",
    )

    parser.add_argument(
        "-p",
        "--path",
        type=Path,
        help="Output file path",
    )

    parser.add_argument(
        "query",
        type=str,
        nargs="?",  # optional
        help="String input / query",
    )

    return parser.parse_args()
