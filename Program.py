#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Program():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

    def feladat(self):
        self.gs.reset_angle(0)

        while self.us.distance() > 100:
            print(self.gs.angle())
            if self.gs.angle() <= 1 and self.gs.angle() >= -1:
                self.jm.run(100)
                self.bm.run(100)
            else:
                if self.gs.angle() > 0:
                    self.jm.run(70)
                    self.bm.run(100)
                elif self.gs.angle() < 0:
                    self.jm.run(100)
                    self.bm.run(70)
                    

