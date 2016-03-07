from .ospf import OSPFSession
from .nxcli import NXCLI
import traceback

instance = '49'
interface_name = 'eth1/6'
area = '20'
distance = 41
ospf_cost = 45
hello_interval = 61
dead_interval = 55
priority = 51

def start_ospf_session():
        '''
        starts ospf session.
        Do show run ospf on switch to see the changes.
        '''

        ospf_session = OSPFSession(instance)
        ospf_interface = OSPFSession.OSPFInterface(interface_name, area)

        ospf_session.start()
        return (ospf_session, ospf_interface)


def shutdown_ospf_session(ospf_session):
        ospf_session.shutdown()


def start_ospf_if_down(ospf_session):
        if ospf_session.is_shutdown():
                start_ospf_session()


def configure_distance(ospf_session):
        ospf_session.cfg_distance(distance)


def add_interface_to_ospf(ospf_interface):
        ospf_interface.add()


def configure_ospf_cost(ospf_interface):
        ospf_interface.cfg_ospf_cost(ospf_cost)


def configure_ospf_hello_interval(ospf_interface):
        ospf_interface.cfg_hello_interval(hello_interval)


def configure_dead_interval(ospf_interface):
        ospf_interface.cfg_dead_interval(dead_interval)


def configure_priority(ospf_interface):
        ospf_interface.cfg_ospf_priority(priority)


def interface_shutdown(ospf_interface):
        ospf_interface.shutdown()


def is_interface_available(interface_name):
        """
        Checks if interface is available or not.
        return True if interface ia available, else returns False
        """

        try:
                interface = NXCLI('show run interface %s' %interface_name)
                return True
        except:
                return False

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """

        NXCLI._run_cfg(cmd)


def convert_to_routed_interface(interface_name):
        """
        Convert interface mode from access to routed
        """

        cmd = "interface %s ; no switchport" %interface_name
        configure_terminal(cmd)


def enable_feature_ospf():
        """
        Enable feature on switch
        """

        cmd = "feature ospf"
        configure_terminal(cmd)


def configure_switch_for_ospf():
        if not is_interface_available(interface_name):
                raise Exception("Interface not available. \nPlease give different interface. To list available interfaces, just go to switch-prompt and type : \nshow int br")

        convert_to_routed_interface(interface_name)

        enable_feature_ospf()

        return start_ospf_session()


def configure_ospf():
        '''
        Use above mention functions as per requirement.
        Sample configuration is shown below.
        To check the result of any fucntion after using it here, do a
        show run ospf on switch.
        '''
        try:
                #Switch is configured for OSPF. This is basic operation and should not be omitted.
                ospf_session, ospf_interface = configure_switch_for_ospf()

                #All of the functions below are independent of each other.
                configure_distance(ospf_session)
                add_interface_to_ospf(ospf_interface)
                configure_ospf_cost(ospf_interface)
                configure_ospf_hello_interval(ospf_interface)
                configure_dead_interval(ospf_interface)
                configure_priority(ospf_interface)

                print "After ospf configuration:"
                NXCLI('show run ospf')

        except Exception, e:
                traceback.print_exc()


if __name__ == '__main__':
        configure_ospf()
