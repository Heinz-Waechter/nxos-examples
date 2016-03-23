from .nxcli import NXCLI
import time
import re

conName = 'con1'
ipAdd = '172.31.217.189'
userName = 'root'
password = 'C!sc0123'

class ShowVmTracker(NXCLI):
    def __init__ (self, cmd):
        super(ShowVmTracker, self).__init__(cmd, do_print=True)

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """
        NXCLI._run_cfg(cmd)

def main():
        """
        Configure checkpoint
        """
        # Enable the feature  
        configure_terminal('feature vmtracker')

        # Config VM Tracker Connection
        configure_terminal('vmtracker connection %s ; remote ip address %s port 80 vrf management ; username %s password %s ; connect ' % (conName, ipAdd, userName, password))
        
        time.sleep(20)
        vmStatus = {}
        
        cli = ShowVmTracker('show vmtracker status')
        cliStatusOutput = cli.raw_output
        out = cliStatusOutput.split('\n\t')
        for line in out:
            vmStatusLine = re.search(r'(\w+)(\s+)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(\s+)(\w+)', line)
            if vmStatusLine:
                connName = vmStatusLine.group(1)
                vmStatus[connName] = {}
                vmStatus[connName]['vcenterip'] = vmStatusLine.group(3)
                vmStatus[connName]['status'] = vmStatusLine.group(5)
        print vmStatus

        vmInfo = {}
        cli = ShowVmTracker('show vmtracker info detail')
        cliInfoOutput = cli.raw_output
        out = cliInfoOutput.split('\n')
        i = 1
        for line in out:
            vmInfoLine = re.search(r'([A-Za-z/0-9]+)(\s+)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(\s+)(\w+)(\s+)([A-Za-z0-9-.]+)(\s+)(\w+)(\s+)([A-Za-z0-9-.]+)(\s+)(\w+)', line)
            if vmInfoLine:
                vmInfo[i] = {}
                vmInfo[i]['interface'] = vmInfoLine.group(1)
                vmInfo[i]['host'] = vmInfoLine.group(3)
                vmInfo[i]['vmnic'] = vmInfoLine.group(5)
                vmInfo[i]['vm'] = vmInfoLine.group(7)
                vmInfo[i]['state'] = vmInfoLine.group(9)
                vmInfo[i]['portgroup'] = vmInfoLine.group(11)
                vmInfo[i]['vlan'] = vmInfoLine.group(13)
                i += 1
        print vmInfo

        # Unconfigure the changes done
        configure_terminal('no feature vmtracker')


if __name__=="__main__":
        main()

