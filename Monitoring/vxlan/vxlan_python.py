from .nxcli import NXCLI
import re

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """
        NXCLI._run_cfg(cmd)

def main():
        """
        Monitor nve vni interfaces 
        """

        # Enable the feature
        configure_terminal('feature nv overlay')

        cli = NXCLI('show nve vni', do_print=True)
	print "\nShow nve vni "
	print "==============="
	vni = {}
        lines = cli.raw_output.split('\n')
        for line in lines:
            vni_line = re.search(r'(nve1)(\s+)([0-9]+)(\s+)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9])(\s+)([a-zA-Z]+)(\s+)([a-zA-Z]+)(\s+)([a-zA-Z0-9]+)(\s+)\[([0-9]+)\]', line)
            if vni_line:
                vni_id = vni_line.group(3)
		vni[vni_id] = {}
		vni[vni_id]['interface'] = vni_line.group(1)
		vni[vni_id]['mcast_grp'] = vni_line.group(5)
		vni[vni_id]['state'] = vni_line.group(7)
		vni[vni_id]['mode'] = vni_line.group(9)
		vni[vni_id]['type'] = vni_line.group(11)
		vni[vni_id]['vrf'] = vni_line.group(13)
        print vni
       
 
        cli = NXCLI('show nve interface', do_print=True)
	print "\nShow nve interface"
	print "========================="
        nveIntf = {}
        lines = cli.raw_output.split('\n')
        for line in lines:
            intf_line1 = re.search(r'Interface: (nve1), State: ([a-zA-Z]+), encapsulation: ([A-Z]+)', line)
            if intf_line1:
                nveIntf['interface'] = intf_line1.group(1)
                nveIntf['state'] = intf_line1.group(2)
                nveIntf['encapsulation'] = intf_line1.group(3)
	    intf_line2 = re.search(r' Source-Interface: (.*) \(primary: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}), secondary: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\)', line)
	    if intf_line2:
		nveIntf['Source-Interface'] = intf_line2.group(1)
		nveIntf['primary'] = intf_line2.group(2)
		nveIntf['secondary'] = intf_line2.group(3)
	print nveIntf

        # Disable the feature
        configure_terminal('no feature nv overlay')

if __name__=="__main__":
        main()

