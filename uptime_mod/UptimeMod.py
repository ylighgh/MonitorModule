#!//usr//bin//env python3
# -*- coding:utf-8 -*-


class UptimeMod:
    uptime_stat = ""

    def __init__(self) -> None:
        uptime_info = get_uptime_info()
        self.uptime_stat = format_uptime_info(uptime_info)


def get_uptime_info() -> float:
    """
    获取启动时间(秒)
    :return:
    """
    with open('//proc//uptime', mode='r') as f:
        uptime_info = float(f.readline().split(' ')[0])
        return uptime_info


def format_uptime_info(uptime_info: float) -> str:
    """
    处理启动时间
    :param uptime_info:
    :return:
    """
    if uptime_info < 3600.00:
        minutes = int(((uptime_info % (60.00 * 60.00)) // 60.00))
        seconds = int((((uptime_info * 1000.00) % (1000.00 * 60.00)) // 1000.00))
        uptime_stat = f'{minutes}分钟{seconds}秒'
    else:
        hours = int((uptime_info % (60.00 * 60.00 * 24.00) // (60.00 * 60.00)))
        minutes = int(((uptime_info % (60.00 * 60.00)) // 60.00))
        seconds = int((((uptime_info * 1000.00) % (1000.00 * 60.00)) // 1000.00))
        uptime_stat = f'{hours}小时{minutes}分钟{seconds}秒'
    return uptime_stat


def main():
    result = UptimeMod()
    print(result.uptime_stat)


if __name__ == '__main__':
    main()
