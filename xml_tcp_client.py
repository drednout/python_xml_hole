#!/usr/bin/env python
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
import sys

from twisted.internet import task
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver

BILLION_LAUGHS = None

class EchoClient(LineReceiver):
    delimiter = '\0'

    def connectionMade(self):
        self.sendLine(BILLION_LAUGHS)


    def lineReceived(self, line):
        print("receive:", line)
        self.transport.loseConnection()



class EchoClientFactory(ClientFactory):
    protocol = EchoClient

    def __init__(self):
        self.done = Deferred()


    def clientConnectionFailed(self, connector, reason):
        print('connection failed:', reason.getErrorMessage())
        self.done.errback(reason)


    def clientConnectionLost(self, connector, reason):
        print('connection lost:', reason.getErrorMessage())
        self.done.callback(None)



def main(reactor):
    global BILLION_LAUGHS
    BILLION_LAUGHS = open(sys.argv[1]).read()
    factory = EchoClientFactory()
    reactor.connectTCP('localhost', 8000, factory)
    return factory.done



if __name__ == '__main__':
    task.react(main)
