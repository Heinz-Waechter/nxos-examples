from .tacacs import *

tacacsServerIp="10.10.2.1" #TACACS+ server's DNS name or its IP address
port="" #TACACS+ server port
key="" #Global TACACS+ server shared secret
timeout="" #TACACS+ server timeout period in seconds
deleteIp="" #server Ip for removing

#used to remove server configuration
def deleteServer(tacacs,server):


        tacacs.add_server(server,no="True")
        print "Successfuly deleted configuration of server ",server


def enable_feature_tacacs():
        cmd = 'feature tacacs'
        configure_terminal(cmd)

def configure_terminal(cmd):
        """
        Configure terminal based on the commands given
        """

        NXCLI._run_cfg(cmd)


if __name__=="__main__":

        enable_feature_tacacs()
        #show TACACS Server
        showTacacs=ShTacasServer()
        print "Before TACACS+ Configuration"
        if showTacacs.servers():
                print showTacacs.servers()
        else:
                print "no server configured"

        tacacs=Tacacs()

        if deleteIp !="" and tacacs._is_server_configured(deleteIp):
                #delete server Ip
                deleteServer(tacacs,deleteIp)

        if tacacsServerIp:

                #add th TACACS+ server
                tacacs.add_server(tacacsServerIp)
                #tacacs.src_interface("Ethernet1/2")
                #tacacs.commit()
                #tacacs.add_group("ciscogroup1",tacacsServerIp)


        showTacacs=ShTacasServer()
        print "After TACACS+ Configuration:",showTacacs.servers()
