#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from utils.split_string_with_space import split_string_with_space


class SwapMod:
    total = 0.0
    free = 0.0
    used = 0.0

    def __init__(self) -> None:
        self.total, self.free, self.used = compute_swap_stat(
            get_proc_swap_stat())


def compute_swap_stat(proc_memory_stat_list: list) -> list:
    swap_stat_list = []

    total = round(proc_memory_stat_list[14] / 1024.00 / 1024.00, 1)
    swap_stat_list.append(total)

    free = round(proc_memory_stat_list[15] / 1024.00 / 1024.00, 1)
    swap_stat_list.append(free)

    used = round((total - free), 1)
    swap_stat_list.append(used)

    return swap_stat_list


def get_proc_swap_stat() -> list:
    with open('/proc/meminfo', mode='r') as f:
        memory_stat_list = []
        for line in f:
            line = line \
                .replace(" ", "") \
                .replace('kB', '') \
                .replace('\n', '') \
                .split(':')[1]
            memory_stat_list.append(line)
        return list(map(int, memory_stat_list))


def main():
    result = SwapMod()
    print(result.total, result.used, result.free)


if __name__ == '__main__':
    main()
