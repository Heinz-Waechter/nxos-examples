#Sample file to display the switch hardware buffer info

from .nxcli import NXCLI
import traceback

def show_hardware_buffer():
        """
        Show the switch hardware buffer info
        """
        try:
                interface = NXCLI('show hardware internal buffer info pkt-stats detail')
                return True
        except:
                return False

if __name__=="__main__":

        try:
                show_hardware_buffer()
        except Exception,e:
                traceback.print_exc()
