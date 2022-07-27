#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class HostNameMod:
    hostname_stat = ""

    def __init__(self) -> None:
        self.hostname_stat = get_hostname_info()


def get_hostname_info() -> str:
    with open('/etc/hostname', mode='r') as f:
        return f.readline()


def main():
    result = HostNameMod()
    print(result.hostname_stat)


if __name__ == '__main__':
    main()
