#   boardThread.py
#
#   Some tasks must be execute periodically,
#   to blink a led for example. Or sometimes we
#   have to execute instructions successively.
#
#   boardThread compile instructions and sending
#   them to the board in a single arrayByte
#   that's way the instructions'll be execute
#   successively.
#
#   If we set a period (milliseconds), the board
#   will initialize a thread, and will execute
#   the instructions periodically.
#
#   If the period is 0, the board will execute
#   the instructions only once time.
#
#   Created by Lenselle Nicolas, January, 2016.
#   lenselle.nicolas@gmail.com

from .variable import _VARIABLES, _FUNCTIONS, _INV_FUNCTIONS, DEBUG, fct
from .exode import ExodeSpeaker

class boardThread :

    def __init__(self, board):

        self._board = board
        self._period = -1
        self._instructions = []

        # the thread's id on the board
        self._ID = -1

        self.on = False

    def setID(self, id):
        self._ID = id

    def add(self, name, *args):
        self._instructions.append([name, args])

    def start(self, period=0):

        self._period = period

        # we use a fake Speaker to get the byteCode
        fakeSpeaker = ExodeSpeaker(None)
        fakeSpeaker.mute = True

        # byteCluster holding the byteCode
        byteCluster = bytearray()
        for inst in self._instructions:
            name = inst[0]
            args = inst[1]
            # a way to get the byteCode, this code is eqv to
            # byteCluster += fakeSpeaker.name(*args)
            byteCluster += getattr(fakeSpeaker, name)(*args)


        # if the period is 0, we just execute Thread once time
        if self._period == 0:
            byteCluster = bytearray([fct('executeThread'),len(byteCluster)]) + byteCluster

        # else we init a periodic thread
        else:
            self.on = True
            key = self._board.getKey()
            bytePeriod = bytearray(self._period.to_bytes(4,'little'))
            byteCluster = bytearray([fct('initThread'), key]) + bytePeriod + bytearray([len(byteCluster)]) + byteCluster
            self._board.addListener(key=key, updateFunction=self.setID)

        self._board.speak(byteCluster)

    def stop(self):
        if self.on == True and self._ID != -1:
            self.period = -1
            self.on = False
            self._board.speak(bytearray([fct('deleteThread')])+self._ID.to_bytes(4,'little'))
