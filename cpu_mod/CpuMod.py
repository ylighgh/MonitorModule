#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from utils.split_string_with_space import split_string_with_space
import time


class ProcCpuStat:
    user = 0
    system = 0
    nice = 0
    idle = 0
    iowait = 0
    irq = 0
    softirq = 0
    steal = 0
    total = 0

    def __init__(self) -> None:
        proc_cpu_list = get_proc_cpu_stat()
        self.user, self.system, self.nice, self.idle, self.iowait, \
        self.irq, self.softirq, self.steal = proc_cpu_list[:8]
        self.total = sum(proc_cpu_list[:8])


class CpuStat:
    us = 0
    sy = 0
    ni = 0
    id = 0
    wa = 0
    hi = 0
    si = 0
    st = 0

    def __init__(self) -> None:
        pre_cpu_stat = ProcCpuStat()
        time.sleep(2)
        cur_cpu_stat = ProcCpuStat()
        cpu_stat_list = compute_cpu_stat(pre_cpu_stat, cur_cpu_stat)
        self.us, self.sy, self.ni, self.id, self.wa, self.hi, self.si, self.st = cpu_stat_list


def get_proc_cpu_stat() -> list:
    with open('/proc/stat', mode='r') as f:
        """
        cpu  326791 2039 101326 18262052 6680 55131 10123 0 0 0
        """
        proc_cpu_stat_list = list(map(int, split_string_with_space(f.readline())[2:10]))
        return proc_cpu_stat_list


def compute_cpu_stat(pre_cpu: object, cur_cpu: object) -> list:
    cpu_stat_list = []

    cpu_total = cur_cpu.total - pre_cpu.total

    us = round(((cur_cpu.user - pre_cpu.user) * 100.00) / cpu_total, 1)
    cpu_stat_list.append(us)

    sy = round(((cur_cpu.system - pre_cpu.system) * 100.00) / cpu_total, 1)
    cpu_stat_list.append(sy)

    ni = round(((cur_cpu.nice - pre_cpu.nice) * 100.00) / cpu_total, 1)
    cpu_stat_list.append(ni)

    id = round((((cur_cpu.idle - pre_cpu.idle) + (cur_cpu.steal - pre_cpu.steal)) * 100.00) / cpu_total, 1)
    cpu_stat_list.append(id)

    wa = round(((cur_cpu.iowait - pre_cpu.iowait) * 100.00) / cpu_total, 1)
    cpu_stat_list.append(wa)

    hi = round(((cur_cpu.irq - pre_cpu.irq) * 100.00) / cpu_total, 1)
    cpu_stat_list.append(hi)

    si = round(((cur_cpu.softirq - pre_cpu.softirq) * 100.00) / cpu_total, 1)
    cpu_stat_list.append(si)

    st = round(((cur_cpu.steal - pre_cpu.steal) * 100.00) / cpu_total, 1)
    cpu_stat_list.append(st)

    return cpu_stat_list


def main():
    result = CpuStat()
    print(result.us, result.sy, result.ni, result.id, result.wa, result.hi, result.si, result.st)


if __name__ == '__main__':
    main()
