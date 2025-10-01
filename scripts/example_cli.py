#!/usr/bin/env python
import argparse
from unilab import hello, mean

def main():
    parser = argparse.ArgumentParser(description="CLI example using the lib unilab.")
    parser.add_argument("--name", default="Nilton")
    parser.add_argument("--nums", nargs="*", type=float, default=[1,2,3])
    args = parser.parse_args()

    print(hello(args.name))
    print("mean:", mean(args.nums))

if __name__ == "__main__":
    main()