import pywifi
from pywifi import const  # 引用一些常量

#判断是否已经连接到WiFi
def gic():
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # 获取到第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 打印网卡的名称
    print(ifaces.name())
    # 列表
    print(ifaces)
    # 打印网卡连接状态 0 未连接
    print(ifaces.status())

gic()