#!/usr/bin/env python
#! -*- encoding: utf-8 -*-


import json
import os
from pkg_resources import resource_string
import telnetlib
import time


class TelnetReel(object):

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


class JsonReel(object):

    def __init__(self, movie_title, frame_break):
        self.title = movie_title
        self.frame_break = frame_break
        self.load_reel(movie_title)

    def load_reel(self, title):
        data = resource_string(__name__, os.path.join('data', title + '.json'))
        self.reel = json.loads(data.decode('utf-8'))

    def __iter__(self):
        for frame in self.reel:
            yield frame


class Movie(object):

    def __init__(self):
        raise NotImplementedError("Movie class is not meant to be used directly")

    def __iter__(self):
        for frame in self.reel:
            yield frame


    def start_movie(self):
        self.reel = TelnetReel(self.host, self.frame_break)
        try:
            for frame in self:
                print(frame)
                time.sleep(self.frame_rate)
        except Exception as e:
            print("\nTelnet application has failed with error :"
                  "\n{!s} : {!s}.\nTrying local cache.".format(type(e), e))
            time.sleep(10)
            self.reel = JsonReel(self.movie_title, self.frame_break)
            for frame in self:
                print(frame)
                time.sleep(self.frame_rate)


class StarWars(Movie):

    host = 'Towel.blinkenlights.nl'
    movie_title = 'a_new_hope'
    frame_break = b'\x1b[H'

    def __init__(self, frame_rate=0.5):
        self.frame_rate = frame_rate


if __name__ == '__main__':
    pass