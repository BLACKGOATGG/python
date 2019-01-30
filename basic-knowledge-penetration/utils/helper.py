# =============================常用方法封装=================================
import socket


def get_host_ip():
    """
    查询本机ip地址
    亲测本方法在mac、windows和Linux系统下均可正确获取IP地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def get_host():
    """
    查询本机ip地址
    使用socket.gethostbyname()方法获取本机IP地址，但有时候获取不到(比如没有正确设置主机名称)
    :return: ip
    """
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    return {
        'hostName': hostname,
        'hostIp': ip
    }


