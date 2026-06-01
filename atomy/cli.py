import argparse

def main():
    parser = argparse.ArgumentParser(prog="atomy")
    parser.add_argument("command")
    args = parser.parse_args()

    if args.command == "run":
        print("Run your app entry point here")
