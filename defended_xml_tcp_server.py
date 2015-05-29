from defusedxml.ElementTree import parse


from twisted.internet import reactor, protocol
from twisted.protocols import basic


class XmlEcho(basic.LineReceiver):
    """This is just about the simplest possible protocol"""
    delimiter = '\0' 
    
    def lineReceived(self, line):
        "As soon as any data is received, write it back."
        data_as_xml = parse(line)
        print("DEBUG: line is {0}".format(line))
        self.sendLine(line)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = XmlEcho
    reactor.listenTCP(8000, factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
