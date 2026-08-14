import argparse


def register_add_parser(subparsers):
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", type=str, required=True)
    add_parser.add_argument("--amount", type=float, required=True)


def register_update_parser(subparsers):
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--description", type=str, required=True)
    update_parser.add_argument("--amount", type=float, required=True)


def register_delete_parser(subparsers):
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)


def register_summary_parser(subparsers):
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int, required=False, default=0)


def register_list_parser(subparsers):
    list_parser = subparsers.add_parser("list")


def parse_args() -> dict:
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    register_add_parser(subparsers)
    register_update_parser(subparsers)
    register_delete_parser(subparsers)
    register_summary_parser(subparsers)
    register_list_parser(subparsers)

    args = parser.parse_args()

    return vars(args)
