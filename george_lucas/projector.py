#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import telnetlib
import time


class Reel(object):

    def __init__(self, host, frame_break):
        self.host = host
        self.frame_break = frame_break

    def __iter__(self):
        self.source = telnetlib.Telnet(self.host)
        data = b''
        try:
            while True:
                new_data = self.source.read_some()
                if not new_data:
                    raise EOFError
                data += new_data
                frames = data.split(self.frame_break)
                for frame in frames[:-1]:
                    yield (self.frame_break + frame).decode('ascii')
                data = frames[-1]
        except EOFError:
            raise StopIteration
        finally:
            self.source.close()


class Movie(object):

    def __iter__(self):
        self.reel = Reel(self.host, self.frame_break)
        for frame in self.reel:
            yield frame

    def start_movie(self):
        for frame in self:
            print(frame)
            time.sleep(self.frame_rate)


class StarWars(Movie):

    host = 'Towel.blinkenlights.nl'
    frame_break = b'\x1b[H'
    frame_rate = 0.5
