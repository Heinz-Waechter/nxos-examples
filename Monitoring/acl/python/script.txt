from .acl import *
from .nxcli import NXCLI
import re

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """
        NXCLI._run_cfg(cmd)

def apply_acl(name):
        """
        Apply ACL 
        """
        cmd  = "line vty ; ip access-class %s out" % acl.name
        configure_terminal(cmd)

def config_timerange(name, type=None, s_day=None, e_day=None, s_time=None, 
		     e_time=None,a_type=None, a_date=None, a_month=None, 
		     a_year=None):
        """
        Configure time range
        """
        if type == 'periodic':
                cmd = "time-range %s ; periodic %s %s to %s %s"% (name, s_day,
						        s_time, e_day, e_time) 
        elif type == 'absolute':
                cmd = "time-range %s ; absolute %s %s %s %s %s"% (name,
				a_type, s_time, a_date, a_month, a_year)
        else:
                cmd = "time-range %s"% name
        configure_terminal(cmd)

def main():
        """
        Configure time based ACL
        """
        # Configuring time-range
        config_timerange('sample', type='periodic', s_day='Monday', 
			 e_day='Thursday', s_time='00:00:00', e_time='0')
        config_timerange('sample', type='absolute', a_type='start',
		         s_time='00:00:00', a_date='31', a_month='Jan', 
			 a_year='2016')

        # Configuring access-list with time-range
        acl = IPv4ACL('my_acl')
        acl.permit('tcp', 'any', 'any', time_range='sample')
        
        # Applying the ACL to an interface
        apply_acl(acl.name)

        cli = NXCLI('show ip access-lists my_acl', do_print=False)
        acl_dict = {}
        acl_lines = cli.raw_output.split('\n\t')
        for line in acl_lines:
            match_acl_name = re.search(r'IP access list (.*)', line)
            if match_acl_name:
                aclName = match_acl_name.group(1) 
		acl_dict[aclName] = {}
            else:
                match_acl_line = re.search(r'(\d+) permit (\w+) (\w+) (\w+) time-range (\w+)', line)
                if match_acl_line:
                        seqNo = match_acl_line.group(1)
			acl_dict[aclName][seqNo] = {}
                        acl_dict[aclName][seqNo]['protocol'] = match_acl_line.group(2) 
                        acl_dict[aclName][seqNo]['src'] = match_acl_line.group(3) 
                        acl_dict[aclName][seqNo]['dest'] = match_acl_line.group(4) 
                        acl_dict[aclName][seqNo]['timeRangeName'] = match_acl_line.group(5) 
                else:
                        print 'No Acl details found'
        print acl_dict

if __name__=="__main__":
	main()
