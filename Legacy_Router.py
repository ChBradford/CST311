#Christopher Bradford
#Idama Okumagba
#Programming assignment 3
from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
def myNetwork():
        net = Mininet( topo=None,
                       build=False,
                       ipBase='10.0.0.0/8')
        info( '*** Adding controller\n' )
        info( '*** Add switches\n')
        r1 = net.addHost('r1', cls=Node, ip='155.007.1.1/8')#This is what both hosts will be connecting to. (155.007.1.1)
        r1.cmd('sysctl -w net.ipv4.ip_forward=1')

        info( '*** Add hosts\n')  # setting up the hosts to the network by their IP address
        h1 = net.addHost('h1', cls=Host, ip='155.007.1.100/8', defaultRoute='via 155.007.1.1')
        h2 = net.addHost('h2', cls=Host, ip='10.16.0.100/8', defaultRoute='via 10.16.0.1')

        info( '*** Add links\n') #links to the network with parameters set to the IP addresses previously added
        net.addLink(h1, r1, intfName2='r1-eth1', params2={ 'ip' : '155.007.1.1/8' })
        net.addLink(h2, r1, intfName2='r2-eth1', params2={ 'ip' : '10.16.0.1/8'})

        info( '*** Starting network\n') #build the network
        net.build()
        CLI(net)
        net.stop()
if __name__ == '__main__': #Run the network and set log for the connection~
   setLogLevel( 'info' )
   myNetwork()
