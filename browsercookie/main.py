#!/usr/bin/env python

from . import api
from pprint import pprint


def main():
    jar = api.load()
    for cookie in jar:
        pprint(cookie)


if __name__ == '__main__':
    main()
