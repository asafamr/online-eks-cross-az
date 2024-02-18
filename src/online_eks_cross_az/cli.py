"""Console script for the_answer_asaf."""

import argparse
import sys
from .lib import get_csv


def main():
    """Console script for the_answer_asaf."""

    parser = argparse.ArgumentParser(description="EKS Cross AZ Log")

    parser.add_argument(
        "--cluster-name",
        metavar="N",
        type=ascii,
        help="EKS cluster name (DEFAULT: extracted from context)",
    )
    parser.add_argument(
        "--minutes", metavar="N", type=int, default=5, help="minutes of accumulation"
    )
    parser.add_argument(
        "--quiet",
        action=argparse.BooleanOptionalAction,
        help="run without confirmation",
    )
    parser.add_argument(
        "--verbose", action=argparse.BooleanOptionalAction, help="verbose log"
    )
    parser.add_argument(
        "--verbose", action=argparse.BooleanOptionalAction, help="verbose log"
    )

    args = parser.parse_args()

    try:
        get_csv(
            accumulation_minutes=args.minutes,
            quite=args.quiet,
            cluster_name=args.cluster_name,
            verbose=args.verbose,
        )
    except Exception as e:
        print(f"Exception while running script: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
