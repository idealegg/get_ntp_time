# -*- coding:utf-8 -*-
import time
import struct


secondsFrom1900To1970 = ((1970-1900)*365+((1970-1900)/4+1))*86400 + 8*3600
class NtpTime:
    # rfc1305的ntp时间中，时间是用64bit来表示的，记录的是1900年后的秒数（utc格式）
    # 高32位是整数部分，低32位是小数部分'''
    def __init__(self, seconds=0, fraction=0):
        self.seconds = seconds
        self.fraction = fraction

    def ToString(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.seconds-secondsFrom1900To1970))


class NTPData:
    def __init__(self):
        self.header = self.GetHeader()
        self.Stratum = 1 # 系统时钟的层数，取值范围为1～16，它定义了时钟的准确度
        self.Poll = 1 # 轮询时间，即两个连续NTP报文之间的时间间隔
        self.Precision = 1 # 系统时钟的精度
        self.rootDelay = 0
        self.rootDispersion = 0
        self.ReferenceIdentifier = 0
        self.ReferenceTimestamp = NtpTime()
        self.OriginateTimestamp = NtpTime()
        self.ReceiveTimestamp = NtpTime()
        self.TransmitTimestamp = NtpTime()

    def GetHeader(self):
        LI = "00"
        VN = "011" # NTP的版本号为3
        Mode = "011" # 客户模式
        return int("".join([LI, VN, Mode]), 2)

    def toString(self):
        s = struct.Struct('>BBBBIIIIIIIIIII')
        return s.pack(self.header,
                       self.Stratum,
                       self.Poll,
                       self.Precision,
                       self.rootDelay,
                       self.rootDispersion,
                       self.ReferenceIdentifier,
                       self.ReferenceTimestamp.seconds,
                       self.ReferenceTimestamp.fraction,
                       self.OriginateTimestamp.seconds,
                       self.OriginateTimestamp.fraction,
                       self.ReceiveTimestamp.seconds,
                       self.ReceiveTimestamp.fraction,
                       self.TransmitTimestamp.seconds,
                       self.TransmitTimestamp.fraction)


