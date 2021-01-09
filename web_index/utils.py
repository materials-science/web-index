from functools import reduce


def ip_into_int(ip):
    return reduce(lambda x, y: (x << 8)+y, map(int, ip.split('.')))


def is_internal_ip(ip_str):
    ip_int = ip_into_int(ip_str)
    net_A = ip_into_int('10.255.255.255') >> 24
    net_B = ip_into_int('172.31.255.255') >> 20
    net_C = ip_into_int('192.168.255.255') >> 16
    net_ISP = ip_into_int('100.127.255.255') >> 22
    net_DHCP = ip_into_int('169.254.255.255') >> 16
    return ip_int >> 24 == net_A or ip_int >> 20 == net_B or ip_int >> 16 == net_C or ip_int >> 22 == net_ISP or ip_int >> 16 == net_DHCP


def get_ip_address(request):
    """
    获取ip地址
    :param request:
    :return:
    """
    ip = request.META.get("HTTP_X_FORWARDED_FOR", "")
    if not ip:
        ip = request.META.get('REMOTE_ADDR', "")
    client_ip = ip.split(",")[-1].strip() if ip else ""
    return client_ip
