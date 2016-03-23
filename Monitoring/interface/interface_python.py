#Sample file to Show Interface details
#Import Interface class
from .interface import  Interface
from .nxcli import NXCLI
import traceback

interfaceName = "Ethernet1/6"

def available_interface(interfaceName):
        """
        Display interface details.
        """
        interface = NXCLI('show interface %s' % interfaceName)


if __name__=="__main__":
        try:
                available_interface(interfaceName)
        except Exception,e:
                traceback.print_exc()
