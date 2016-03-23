#Sample file to configure Interface
#Import Interface class
from .interface import  Interface
from .nxcli import NXCLI
import traceback

#Fillup the Interface details to be configured
interfaceName="Ethernet1/6"
interfaceIpaddress="192.168.17.12/24"
interfaceDescription="Interface6"
interfaceState="no shut"

def is_interface_available(interfaceName):
        """
        Checks if interface is available or not.
        return True if interface is available, else return False
        """

        try:
                interface = NXCLI('show run interface %s' %interfaceName)
                return True
        except:
                return False

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """

        NXCLI._run_cfg(cmd)

def convert_to_routed_interface(interfaceName):
        """
        Convert interface mode from access to routed
        """

        cmd = "interface %s ; no switchport" %interfaceName
        configure_terminal(cmd)

if __name__=="__main__":

        try:
                if not is_interface_available(interfaceName):
                        raise Exception("Interface not available. \nPlease give different interface. To list available interfaces, just go to switch-prompt and type : \nshow int br")

                switch=Interface(interfaceName)

                print "Before Interface Configuration"
                configurationResults=switch.config()
                print configurationResults

                convert_to_routed_interface(interfaceName)

                if interfaceIpaddress:
                        #set Ip address
                        ipaddress=switch.set_ipaddress(interfaceIpaddress)

                        #set Description
                        if interfaceDescription:
                                description=switch.set_description(interfaceDescription)

                        #set mode and state
                        switch.set_state(interfaceState)

                print "After interface  Configuration"
                configurationResults=switch.config()
                print configurationResults


        except Exception,e:
                traceback.print_exc()
