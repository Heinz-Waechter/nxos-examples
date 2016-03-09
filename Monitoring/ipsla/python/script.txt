from .nxcli import NXCLI
import re

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """
        NXCLI._run_cfg(cmd)

def main():
        # Make IP SLA configurations
        NXCLI._run_cfg('feature sla sender')
        NXCLI._run_cfg('ip sla 6 ; icmp-echo 172.31.216.130')
        NXCLI._run_cfg('ip sla schedule 6 life forever start-time now')

        # Show the difference between running-config and checkpoint
        print "\nShow IP SLA application "
        print "==============="
        cli = NXCLI('show ip sla application', do_print=True)
        ipslaAppln = {}
        lines = cli.raw_output.split('\n')
        for line in lines:
            confEntries = re.search(r'Number of Entries configured\s+:\s+(.*)', line)
            if confEntries:
                ipslaAppln['Configured entries'] = confEntries.group(1)
            actEntries = re.search(r'Number of active Entries\s+:\s+(.*)', line)
            if actEntries:
                ipslaAppln['Active entries'] = actEntries.group(1) 
        print ipslaAppln

        print "\nShow IP SLA configuration"
        print "==============="
        cli = NXCLI('show ip sla configuration', do_print=True)
        ipslaConf = {}
        lines = cli.raw_output.split('\n')
        for line in lines:
	    entryNo = re.search(r'Entry number:\s+(.*)', line)
	    if entryNo:
		ipslaConf['Entry number'] = entryNo.group(1)
	    typeOfOp = re.search(r'Type of operation to perform:\s+(.*)', line)
	    if typeOfOp:
		ipslaConf['Type of operation'] = typeOfOp.group(1)
	    addr = re.search(r'Target address\/Source address:\s+(.*)\/(.*)', line)
	    if addr:
		ipslaConf['target addr'] = addr.group(1)
		ipslaConf['source addr'] = addr.group(2)
	    opFreq = re.search(r'Operation frequency \(seconds\):\s+([0-9]+)', line)
	    if opFreq:
		ipslaConf['operation frequency'] = opFreq.group(1)
	print ipslaConf

        print "\nShow IP SLA statistics"
        print "==============="
        cli = NXCLI('show ip sla statistics', do_print=True)
        ipslaStats = {}
        lines = cli.raw_output.split('\n')
        for line in lines:
	     opId = re.search(r'IPSLA operation id:\s+(.*)', line)
	     if opId:
		ipslaStats['operation id'] = opId.group(1)
	     noOfSuc = re.search(r'Number of successes:\s+(.*)', line)
	     if noOfSuc:
		ipslaStats['number of successes'] = noOfSuc.group(1)
	     noOfFail = re.search(r'Number of failures:\s+(.*)', line)
	     if noOfFail:
		ipslaStats['number of failures'] = noOfFail.group(1)
	     opTime = re.search(r'Operation time to live:\s+(.*)', line)
	     if opTime:
		ipslaStats['operation ttl'] = opTime.group(1)
	print ipslaStats

        NXCLI._run_cfg('no feature sla sender')

if __name__=="__main__":
        main()
