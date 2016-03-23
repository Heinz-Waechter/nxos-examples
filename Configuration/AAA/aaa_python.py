#Sample file to configure AAA authentication login ascii and error-enable

from .nxcli import NXCLI
import traceback

def show_config_info():
        """
        Show the running aaa configuration
        """

        try:
                interface = NXCLI('show run aaa')
                return True
        except:
                return False

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """

        NXCLI._run_cfg(cmd)

def enable_aaa_ascii_error():
        """
        Configure the default aaa authentication login features
        """

        cmd = "aaa authentication login ascii-authentication ; aaa authentication login error-enable"
        configure_terminal(cmd)

if __name__=="__main__":

        try:
                enable_aaa_ascii_error()
                show_config_info()
        except Exception,e:
                traceback.print_exc()
