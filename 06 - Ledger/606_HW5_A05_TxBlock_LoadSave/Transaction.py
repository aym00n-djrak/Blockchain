#!/usr/bin/env python3
""" 
The goal of this exercise is to complete the transaction module.
In this exercise you need to add a __repr__() function that will be used
to show the details of transaction. 

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this exercise located in same folder.

To test run 'TxBlock_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * Check previous tutorials for more information on this topic
"""

from Signature import *


class Tx:
    inputs = None
    outputs = None
    sigs = None
    reqd = None

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.sigs = []
        self.reqd = []

    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))

    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))

    def add_reqd(self, addr):
        self.reqd.append(addr)

    def sign(self, private):
        message = self.__gather()
        newsig = sign(message, private)
        self.sigs.append(newsig)

    def is_valid(self):
        total_in = 0
        total_out = 0
        message = self.__gather()
        for addr, amount in self.inputs:
            found = False
            for s in self.sigs:
                if verify(message, s, addr):
                    found = True
            if not found:
                # print ("No good sig found for " + str(message))
                return False
            if amount < 0:
                return False
            total_in = total_in + amount
        for addr in self.reqd:
            found = False
            for s in self.sigs:
                if verify(message, s, addr):
                    found = True
            if not found:
                return False
        for addr, amount in self.outputs:
            if amount < 0:
                return False
            total_out = total_out + amount

        if total_out > total_in:
            # print("Outputs exceed inputs")
            return False

        return True

    def __gather(self):
        data = []
        data.append(self.inputs)
        data.append(self.outputs)
        data.append(self.reqd)
        return data

    # TODO :
    # Complete __repr__() method.
    # for the desired format, check the 'output.txt' file.
    # INPUTS:
    # 1 from b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA17Qc21PHEjqP7CLg1v1l\nYaSRy4gu5MXWcjbflmInox6IbMD/7P37kuvWRw/ruVCidoy8JmwasDGDv6Z9vRfN\nYSIssLziMcbhWUdEMLlI5Qu1Vf1eUzAxUEhQ4SBUi21BYX5uKoZm+rzd/idTi00W\nLI9c3/mKx5+i8pUBNFOXAijlqr5akxmqox2CN5cynKt2YK3ADOJPY8+hFT7s99Vd\np/3EWf4hyFWXWSnMTCs+n42pYf5ZA3/kRFzMI8x070zfNNqjgseXQuyc0br4U1Jt\nnAJaE4OzKez4rEF1tyZ9YBxX+D1ZshZpozdLxIyO4JUa4913zHFlz6CcIMH3a1hI\nVQIDAQAB\n-----END PUBLIC KEY-----\n'
    # OUTPUTS:
    # 1 to b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxGLdr2pV+nnQBH7oDP/9\nnBx5rc8zQJAsXSyL/HQAb+x3bhxRditCqsrShEIZpix7OZmMy8R8C8R+M6OAmeMy\nKGXxGD80WINSJgzSy2SZwAbKVNCzFEPVg/5tNgAzZBkeAZ8ddgrFzago2eeJwjyr\nthcdfnlJzw+LIXkIbG0AmU9XGRE3HpxlY0k5BJZ1LoWVezq+ip/nAO2i0Ht/rGxN\njmJvvDjGkawaHbeNIGdhEqIJp2/sKCJg0OyU7r1QbAwlbF61fEyzCVEH+PrqHmlI\nnCrP/qkxr/7bcWADbM2rX1sB8ueSAu70EIPeFtdGCDr+vzc7qphelFnzK8ekwiFD\nYQIDAQAB\n-----END PUBLIC KEY-----\n'
    # EXTRA REQUIRED SIGNATURES:
    # b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1HKkpz+xIVe4B7oT7I+V\nx6FYBlT0H9BRUdOnYHKaUVNdR8WnlJBFzdl5oDOOfpzvtJdQtM6RD1lKPdKhvelE\nlemnTqBKT4aeZtSrbmTHhbJgS7cgyVTi3w2Ct7ye/ypyMPoFZlLCI7L7UGyzLKlQ\npnOJTouYzwgN7m7T3IaAYYwrRwCMczq+IKARPPfA8wMcdb1/tM7voqGmiSb5Z0fz\nHsd/MWcKuL3ZGBkx3lT2QEXuTT3OO6V8LdVWMU0kEaM0lS30KzVIT7CNmbyBe7kc\nsBnZ0Q79GlQaLnsDphPUrbndsr3jp4Wmx0H9JzLNNnJrvmOnWKTgHi5BTylVxMe7\nWQIDAQAB\n-----END PUBLIC KEY-----\n'
    # SIGNATURES:
    # b'G\xcb\xc0\xf4ULc|~4#{\xc7\xf2\x8f:\xa7\xef\xb5H@&\xaaQ,K/\x9b\x92\xaa\xbd\xa7\xe66\xf5q\xf1\x90XD\xf5>AO\x19\x11\x9f\x89\x0b\xcc\xb9]Zu\xf0x\xe8k&\x8b\xb6k\xeb9\x81\x9a\x0b\xf7\\yl\xdcc7\xfbP\xd5W\xb5\xa2\x1bY\x1a\\d\xfe\xe8.\xf9\xecG%\xc9\xcb\x1ab\xee<nu\x08<\xe9\x90X\xd6\xa6qd\xd6#\xcd\x13\xc5I\x99\xd7\xfc\xaaP\xf4t\xf7\x14\x92\xcbu\xa2\xdeE\x19\xd3\x82\xb4S\xa3L\xe4\xe8\x85\x92\x12O\xd3@H\xf4OR\x0b\x82\tI\x9eR\xc1xW\xbe8\x82\\\xaf\x00\xf5\xc5\xbfN\xc3\xcde\xc7\xd2\x93\xba\x11\xf7\xf9]\xf6\xb1\xbb(7\xf8H\xec\xbb\xf1Y\xc5\xd6q\xb21\xe5\x90"7 \xe1\')\x8e\x0c\xae\x9a\xc8\x05*hF\x86\xed\x12\x08\xe2\x96U \xcb\xea\xe2\xed\xean\x12\xc9\xd1\x80\xdb\xd6\xf7\xffJ\x19\xdeTv5!\xaf\xee\x95\xf3\xa0\xc3g\xe7\xc6e\xa2,E\xf0\x16'
    # b'\x05\xf0\xd3\xd1\xde^\xceB\xb6\x03.\xcf\x92`\xc4\xe3\x9d%\xc1\xce\xaa\xfao\x80\xe77\xfcg\x7f\x8a\xbb\x87\x1fz\x81\xad\x96\xc64\x07\xd9%\x01f\x04\xf1\xfa\xa5\xad?\xf5I9\x9de%\xe8\xf13\x1c.w\x0eT\x10hb\x04\x1c\xf9\xe5\x1b!\x99\xb5fr\xe3\x87\xc3?\xec\xe7^;w\xb3\xcdT\xd6\x82Zb\xa7 \x9e\x85k8\xf5\x98\xf6\x9d\xf3\xaf\x88^\x8f5\xe8\xa4}\xa4Q@G\x1f\xa8\xf6\xcf\xdbG\x8fHG\xe7x\\\xb7\xf6\xed\xe1\x03?\x81\xcavS_\xcc\xc0\xa6\xf0\x99\xaa\x86ZZQ\xebI*6\xaf!\xec\xe9l\x9f\x13\x93\xf4\xce\x94,\xd0.\x19`\xefV\x87/l#x\x84<%\x19\xba\xa8\x12\xec\xd3\x88_vW\x9ak\xa60\t\x80k\xda\xf4\xd2\xf6\xa0b\x9e]\xe1N\x06\xbd\xe5J\xc8\x7f\\`\x01]Q\xbf\xa8\x83\xc0\xab\xe1\x8c\xc3\x7f\xcf\xbf\xd2s#\xb5&,gP\x03\xb4\x95\xe5\xdf\xf7I@\xdb\xe4$\xe76l\xa4\xbeMN59'
    # END

    def __repr__(self):
        repr_str = "INPUTS:\n"
        for input_data in self.inputs:
            repr_str += f"  {input_data[1]} from {input_data[0]}\n"

        repr_str += "OUTPUTS:\n"
        for output_data in self.outputs:
            repr_str += f"  {output_data[1]} to {output_data[0]}\n"

        repr_str += "EXTRA REQUIRED SIGNATURES:\n"
        for reqd_sig in self.reqd:
            repr_str += f"  {reqd_sig}\n"

        repr_str += "SIGNATURES:\n"
        for sig in self.sigs:
            repr_str += f"  {sig}\n"

        repr_str += "END\n"

        return repr_str
