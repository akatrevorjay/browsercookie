#!/usr/bin/env python

from . import api
from pprint import pprint


def main():
    jar = api.load()
    pprint(jar)


if __name__ == '__main__':
    main()
