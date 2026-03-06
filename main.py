#!/usr/bin/env python3

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="muvault",
        description="Muvault: A tool to manage and share music albums",
        epilog="Use 'muvault <command> --help' for more information on a command.",
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Sub-commands"
    )

    # Sub-command: runservice
    runservice_parser = subparsers.add_parser(
        "runservice", help="Run the Muvault service"
    )
    runservice_parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=20381,
        help="Specify the port to run the service on (default: 20381)",
    )
    runservice_parser.add_argument(
        "--network-response",
        "-n",
        type=str,
        default="all",
        choices=["all", "local", "remote"],
        help="Specify what network packets the service responds to (default: all)",
    )

    # Sub-command: remote
    remote_parser = subparsers.add_parser("remote", help="Add or edit a remote server")
    remote_parser.add_argument(
        "action", choices=["add", "edit"], help="Action to perform on the remote server"
    )
    remote_parser.add_argument("url", help="URL of the remote server")

    # Sub-command: ls
    ls_parser = subparsers.add_parser("ls", help="List all music stored locally")
    ls_parser.add_argument(
        "--search", help="Search the catalog for specific albums or tracks"
    )

    # Sub-command: push
    push_parser = subparsers.add_parser(
        "push", help="Push an album to the local registry"
    )
    push_parser.add_argument("album_name", help="Name of the album to push")

    # Sub-command: pull
    pull_parser = subparsers.add_parser(
        "pull", help="Pull an album into your music directory"
    )
    pull_parser.add_argument("album_name", help="Name of the album to pull")

    # Sub-command: storage
    storage_parser = subparsers.add_parser("storage", help="Change the storage method")
    storage_parser.add_argument(
        "method", choices=["folder", "genre"], help="Storage method to use"
    )

    args = parser.parse_args()

    # Handle sub-commands
    if args.command == "runservice":
        print(f"Running Muvault service on port {args.port}")
        # Add logic to start the service here

    # Handle sub-commands
    if args.command == "remote":
        print(f"Remote action: {args.action}, URL: {args.url}")
    elif args.command == "ls":
        if args.search:
            print(f"Searching catalog for: {args.search}")
        else:
            print("Listing all music in local storage")
    elif args.command == "push":
        print(f"Pushing album: {args.album_name}")
    elif args.command == "pull":
        print(f"Pulling album: {args.album_name}")
    elif args.command == "storage":
        print(f"Changing storage method to: {args.method}")


if __name__ == "__main__":
    main()
