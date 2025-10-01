#!/usr/bin/env python
"""Exemplo de script CLI que usa o pacote local."""
import argparse
from unilab import hello, mean

def main():
    parser = argparse.ArgumentParser(description="Exemplo de CLI para o projeto.")
    parser.add_argument("--name", default="Nilton")
    parser.add_argument("--nums", nargs="*", type=float, default=[1,2,3])
    args = parser.parse_args()

    print(hello(args.name))
    print("mean:", mean(args.nums))

if __name__ == "__main__":
    main()