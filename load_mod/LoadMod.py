#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class LoadMod:
    avg_1_min = 0
    avg_5_min = 0
    avg_15_min = 0

    def __init__(self) -> None:
        self.avg_1_min, self.avg_5_min, self.avg_15_min = get_proc_load_stat()


def get_proc_load_stat():
    with open('/proc/loadavg', mode='r') as f:
        proc_load_stat = f.readline().split(' ')[:3]
        return proc_load_stat


def main():
    result = LoadMod()
    print(result.avg_1_min, result.avg_5_min, result.avg_15_min)


if __name__ == '__main__':
    main()
