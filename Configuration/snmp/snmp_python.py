# Sample file to configure snmp community

from .nxcli import NXCLI
import traceback

def config_snmp_community():
        """
        Configure the snmp community
        """
        try:
            cmd = 'snmp-server community test group network-operator ; snmp-server community test use-acl aclname'
            NXCLI._run_cfg(cmd)
            return True
        except:
            return False


if __name__=="__main__":

        try:
            config_snmp_community()
        except Exception,e:
            traceback.print_exc()
