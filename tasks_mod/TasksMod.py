#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import os
from utils.split_string_with_space import split_string_with_space

DIRECTORY = '/proc'


class TasksMod:
    running_task_num = 0
    sleeping_task_num = 0
    stop_task_num = 0
    zombie_task_num = 0
    total_task_num = 0

    def __init__(self) -> None:
        pid_directory_list = get_pid_directory()
        for stat_file in pid_directory_list:
            with open(stat_file, mode='r') as f:
                pid_stat_list = split_string_with_space(f.read())
                match pid_stat_list[2]:
                    case 'R':
                        self.running_task_num += 1
                    case 'S' | 'I':
                        self.sleeping_task_num += 1
                    case 'T':
                        self.stop_task_num += 1
                    case 'Z':
                        self.zombie_task_num += 1
            self.total_task_num += 1


def get_pid_directory() -> list:
    pid_directory_list = []
    for pid in os.listdir(DIRECTORY):
        f = os.path.join(DIRECTORY, pid, 'stat')
        # /proc/7351/stat
        if re.findall(r'.*/\d+/.*', f):
            pid_directory_list.append(f)
    return pid_directory_list


def main():
    result = TasksMod()
    print(result.total_task_num, result.running_task_num,
          result.sleeping_task_num, result.stop_task_num,
          result.zombie_task_num)


if __name__ == '__main__':
    main()
