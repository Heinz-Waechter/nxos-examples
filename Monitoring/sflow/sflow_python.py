from .nxcli import NXCLI
import re

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """
        NXCLI._run_cfg(cmd)

def main():

        # Make some configuration changes
        NXCLI._run_cfg('feature sflow')

        # Show the difference between running-config and checkpoint
        cli = NXCLI('show sflow', do_print=True)
        print "\nShow sflow "
        print "==============="
        sflow = {}
        lines = cli.raw_output.split('\n')
        for line in lines:
            sampRate = re.search(r'sflow sampling-rate :\s+(.*)', line)
            if sampRate:
                sflow['sampling rate'] = sampRate.group(1)
            sampMaxSize = re.search(r'sflow max-sampled-size :\s+(.*)', line)
            if sampMaxSize:
                sflow['sampling max size'] = sampMaxSize.group(1) 
            pollIntrwl = re.search(r'sflow counter-poll-interval :\s+(.*)', line)
            if pollIntrwl:
                sflow['poll interval'] = pollIntrwl.group(1)     
            dataSize = re.search(r'sflow max-datagram-size :\s+(.*)', line)
            if dataSize:
                sflow['datagram max size'] = dataSize.group(1)   
            collIp = re.search(r'sflow collector-ip :\s+(.*)\s+,vrf :\s+(.*)', line)
            if collIp:
                sflow['collector ip'] = collIp.group(1)          
                sflow['vrf'] = collIp.group(2)              
            collPort = re.search(r'sflow collector-port :\s+(.*)', line)
            if collPort:
                sflow['collector port'] = collPort.group(1)      
            agentIp = re.search(r'sflow agent-ip :\s+(.*)', line)
        print sflow

        cli = NXCLI('show sflow statistics', do_print=True)
        print "\nShow sflow stats"
        print "==============="
        sflowStats = {}
        lines = cli.raw_output.split('\n')
        for line in lines:
            totPkts = re.search(r'Total Packets\s+:\s+(.*)', line)
            if totPkts:
                sflowStats['total packets'] = totPkts.group(1)
            totSamples = re.search(r'Total Samples\s+:\s+(.*)', line)
            if totSamples:
                sflowStats['total samples'] = totSamples.group(1)
            procSamples = re.search(r'Processed Samples\s+:\s+(.*)', line)
            if procSamples:
                sflowStats['processed samples'] = procSamples.group(1)
            drpSamples = re.search(r'Dropped Samples\s+:\s+(.*)', line)
            if drpSamples:
                sflowStats['dropped samples'] = drpSamples.group(1)
            sentData = re.search(r'Sent Datagrams\s+:\s+(.*)', line)
            if sentData:
                sflowStats['sent datagrams'] = sentData.group(1)
            dropData = re.search(r'Dropped Datagrams\s+:\s+(.*)', line)
            if dropData:
                sflowStats['dropped datagrams'] = dropData.group(1)
        print sflowStats
            
        NXCLI._run_cfg('no feature sflow')

if __name__=="__main__":
        main()

