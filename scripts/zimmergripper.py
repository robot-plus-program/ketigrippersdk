#!/usr/bin/env python3

import ctypes

class KetiZimmer:
    def __init__(self, so_file):
        print(so_file)
        self.lib = ctypes.cdll.LoadLibrary(so_file)
        
        self.lib.SetGripper.restype = ctypes.c_void_p
        self.module = self.lib.SetGripper()

    def Connect(self, ip='192.168.0.253', port=502):        
        self.lib.Connect.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
        self.lib.Connect(self.module, ip.encode('utf-8'), port)

    def Disconnect(self):
        self.lib.Disconnect.argtypes = [ctypes.c_void_p]
        self.lib.Disconnect(self.module)

    def Init(self):
        self.lib.Init.argtypes = [ctypes.c_void_p]
        self.lib.Init(self.module)

    def Grip(self):
        self.lib.Grip.argtypes = [ctypes.c_void_p]
        self.lib.Grip(self.module)

    def Release(self):
        self.lib.Release.argtypes = [ctypes.c_void_p]
        self.lib.Release(self.module)

    def IsConnected(self):
        self.lib.IsAlive.argtypes = [ctypes.c_void_p]
        self.lib.IsAlive.restype = ctypes.c_bool
        return self.lib.IsAlive(self.module)
    
    def Move(self, position):
        self.lib.Move.argtypes = [ctypes.c_void_p, ctypes.c_uint16]
        self.lib.Move(self.module, position)

import time, os
if __name__ == '__main__':
    gripper = KetiZimmer(f'{os.getcwd()}/../libzimmergripper.so')
    gripper.Connect('192.168.137.254', 502)
    gripper.Init()
    
    gripper.Grip()
    gripper.Release()
    
    