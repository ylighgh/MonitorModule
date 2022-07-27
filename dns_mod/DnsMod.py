#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class DnsMod:
    dns_stat = []

    def __init__(self) -> None:
        self.dns_stat = get_dns_list()


def get_dns_list():
    """
    获取DNS信息
    :return:
    """
    dns_list_info = []
    with open('/etc/resolv.conf', mode='r') as f:
        for dns_info in f.readlines():
            if 'nameserver' in dns_info:
                dns = format_dns_info(dns_info)
                dns_list_info.append(dns)
            else:
                continue
    return dns_list_info


def format_dns_info(dns_info: str) -> str:
    return (dns_info.strip()).split(' ')[1]


def main():
    result = DnsMod()
    print(result.dns_stat)


if __name__ == '__main__':
    main()
