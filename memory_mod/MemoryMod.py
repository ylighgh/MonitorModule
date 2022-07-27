#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from utils.split_string_with_space import split_string_with_space


class MemoryMod:
    total = 0.0
    free = 0.0
    avail = 0.0
    buff = 0.0
    cache = 0.0
    used = 0.0

    def __init__(self) -> None:
        self.total, self.free, self.avail, self.buff, self.cache, self.used = compute_memory_stat(
            get_proc_memory_stat())


def compute_memory_stat(proc_memory_stat_list: list) -> list:
    memory_stat_list = []

    total = round(proc_memory_stat_list[0] / 1024.00 / 1024.00, 1)
    memory_stat_list.append(total)

    free = round(proc_memory_stat_list[1] / 1024.00 / 1024.00, 1)
    memory_stat_list.append(free)

    avail = round(proc_memory_stat_list[2] / 1024.00 / 1024.00, 1)
    memory_stat_list.append(avail)

    buff = round(proc_memory_stat_list[3] / 1024.00 / 1024.00, 1)
    memory_stat_list.append(buff)

    cache = round(proc_memory_stat_list[4] / 1024.00 / 1024.00, 1)
    memory_stat_list.append(cache)

    used = round(total - (free + buff + cache), 1)
    memory_stat_list.append(used)

    return memory_stat_list


def get_proc_memory_stat() -> list:
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
    result = MemoryMod()
    print(result.total, result.used, result.free, result.buff, result.cache, result.avail)


if __name__ == '__main__':
    main()
