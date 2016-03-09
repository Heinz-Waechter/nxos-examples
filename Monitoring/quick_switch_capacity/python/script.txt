from .nxcli import NXCLI
import re


def main():
        """
        Monitor port-channel, MAC, Tcam and SVI details
        """
        cli = NXCLI('show port-channel usage', do_print=False)
	print "\nShow port-channel usage"
	print "========================="
        pc_out = cli.raw_output.split('\n\t')
        for line in pc_out:
            used_pc = re.search(r'Used(\s+):(\s+)(.*)', line)
            if used_pc:
                usedPC = used_pc.group(3).split(',')
                print 'Used port channel group:' , usedPC
            unused_pc = re.search(r'Unused:(\s+)(.*)', line)
            if unused_pc:
                unUsedPC = unused_pc.group(2).split(',')
                print 'Unused port channel group:' , unUsedPC
       
 
        cli = NXCLI('show hardware access-list tcam region', do_print=False)
	print "\nShow hardware access-list tcam region"
	print "======================================="
        names = []
        sizes = []
        out = cli.raw_output.split('\n')
        for line in out:
            t_reg = re.search(r'TCAM Region Sizes:(\s+)(.*)', line)
            if t_reg:
                total_tcam_region = t_reg.group(2)
                print 'TCAM Region Sizes: ', total_tcam_region

            t_names = re.search(r'(\s+)(.*)(\s+)size(\s+)=(\s+)(.*)', line)
            if t_names:
                names.append(t_names.group(2))
                sizes.append(t_names.group(6))
        
        template = "{0:40} {1:10}"
        print template.format("Name", "Size")
        print template.format("=======", "=========")
        for name, size in zip(names, sizes):
            print template.format(name, size)
        
        cli = NXCLI('show mac address-table count', do_print=False)
	print "\nShow mac address-table count"
	print "================================="
	out = cli.raw_output.split('\n')
	mac_dict = {} 
	for line in out:
            mac = re.search(r'(.*):(\s+)(.*)', line)
            if mac:
		mac_address = mac.group(1)
		mac_dict[mac_address] = mac.group(3)

	print mac_dict

if __name__=="__main__":
        main()

