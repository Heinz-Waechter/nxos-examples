from .nxcli import NXCLI
import re

def main():
        """
        Monitor SSH & Telnet details
        """
        cli = NXCLI('show users', do_print=True)
        print "\nShow users"
        print "==============="
        pids = {}
        lines = cli.raw_output.split('\n')
        for line in lines:
            user_line = re.search(r'([a-zA-Z0-9]+)(\s+)([a-zA-Z0-9/]+)(\s+)([0-9-]+)(\s+)([0-9:]+)(\s+)([0-9:.]+)(\s+)([0-9]+)(\s+)(.*)', line)
            if user_line:
                pid = user_line.group(11)
                pids[pid] = {}
                pids[pid]['name'] = user_line.group(1)
                pids[pid]['line'] = user_line.group(3)
                pids[pid]['time'] = user_line.group(5) + user_line.group(7)
                pids[pid]['idle'] = user_line.group(9)
                pids[pid]['comment'] = user_line.group(13)

        template = '{0:10} {1:10} {2:20} {3:10} {4:10} {5:20}'
        print template.format("NAME", "LINE", "TIME", "IDLE", "PID", "COMMENT")
        print template.format("=========", "=========", "=========", "=========", "=========", "=========")
        for pid in pids:
            print template.format(pids[pid]['name'], pids[pid]['line'], pids[pid]['time'], pids[pid]['idle'], pid, pids[pid]['comment'])


if __name__=="__main__":
        main()


