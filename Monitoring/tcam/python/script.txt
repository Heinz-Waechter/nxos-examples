from .nxcli import NXCLI
import re


def main():
        cli = NXCLI('show hardware access-list tcam region', do_print=False)
        print "\nShow hardware access-list tcam region"
        print "======================================="
        names = []
        sizes = []
        out = cli.raw_output.split('\n')
        for line in out:
            tcamLine = re.search(r'TCAM Region Sizes:(\s+)(.*)', line)
            if tcamLine:
                total_tcam_region = tcamLine.group(2)
                print 'TCAM Region Sizes: ', total_tcam_region

            tcamSize = re.search(r'(\s+)(.*)(\s+)size(\s+)=(\s+)(.*)', line)
            if tcamSize:
                names.append(tcamSize.group(2))
                sizes.append(tcamSize.group(6))

        template = "{0:40} {1:10}"
        print template.format("Name", "Size")
        print template.format("=======", "=========")
        for name, size in zip(names, sizes):
            print template.format(name, size)

        print "\nShow hardware access-list resource utilization"
        print "======================================="
        cli = NXCLI('show hardware access-list resource utilization', do_print=True)

        print "\nShow show system internal access-list global"
        print "======================================="
        cli = NXCLI('show system internal access-list global', do_print=True)


if __name__ == '__main__':
	main()
