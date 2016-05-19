import socket
from scapy.all import *
from gsmpackets import *
from multiprocessing import Process
from detector import Detector

class A5Detector(Detector):


    def handle_packet(self, data):
        p = GSMTap(data)
        if p.payload.name is 'LAPDm' and p.payload.payload.name is 'GSMAIFDTAP' and p.payload.payload.payload.name is 'CipherModeCommand':
                cipher = p.payload.payload.payload.cipher_mode >> 1
                if cipher == 0:
                    self.update_s_rank(Detector.SUSPICIOUS)
                    self.comment = 'A5/1 detected'
                    # print 'A5/1 detected'
                elif cipher == 2:
                    # print 'A5/3 detected'
                    self.comment = 'A5/3 detected'
                    self.update_s_rank(Detector.NOT_SUSPICIOUS)
                else:
                    self.update_s_rank(Detector.UNKNOWN)
                    # print 'cipher used %s:' % cipher


