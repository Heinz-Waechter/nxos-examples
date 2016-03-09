from .nxcli import NXCLI

checkpointName = 'sample'

class ShowRollbackDiff(NXCLI):
    def __init__ (self, name):
        super(ShowRollbackDiff, self).__init__('show diff rollback-patch checkpoint %s running-config' % name)

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """
        NXCLI._run_cfg(cmd)

def main():
        """
        Configure checkpoint
        """
        NXCLI._run_cfg('checkpoint %s' % checkpointName)

        # Make some configuration changes
        configure_terminal('feature vmtracker')

        checkpoint = ShowRollbackDiff(checkpointName)

        # Show the difference between running-config and checkpoint
        configure_terminal('show diff rollback-patch checkpoint %s running-config' %checkpointName)

        # Unconfiguring checkpoint
        configure_terminal('no checkpoint %s' %checkpointName)

        # Unconfigure the changes done
        configure_terminal('no feature vmtracker')

if __name__=="__main__":
        main()

