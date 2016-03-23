# Sample file to display lldp neighbors details

# Import Interface class
from .nxcli import NXCLI
import traceback

def available_interface():
        """
        Display lldp neighbors details.
        """
        try:
                resp = NXCLI('show lldp neighbors')
                return True
        except Exception as e:
                return False

if __name__=="__main__":
        try:
                available_interface()
        except Exception,e:
                traceback.print_exc()
