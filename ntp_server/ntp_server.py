# -*- coding:utf-8 -*-
import socket
import ntp_message.ntp_message


class ntp_server:
    def __init__(self, host, port=123):
        self.host = host
        self.port = port
        self.s = None
        self.return_msg = ""

    def ntp_send(self, msg):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.sendto(msg, (self.host, self.port))
        self.s.close()

    def ntp_receive(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("0.0.0.0", 0))
        self.return_msg, addr = self.s.recvfrom(2048)
        if not self.return_msg:
            print "client has exist"
        print "received:", self.return_msg, "from", addr
        self.s.close()

if __name__ == "__main__":
    host = raw_input("Please input host ip:")
    ns = ntp_server(host)
    ns.ntp_send(ntp_message.ntp_message.NTPData().toString())
    ns.ntp_receive()