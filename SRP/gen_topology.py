from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   controller=None)

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    r1 = net.addHost('r1', cls=Node)
    r2 = net.addHost('r2', cls=Node)

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, defaultRoute=None)
   

    info( '*** Add links\n')
    net.addLink(h1, r1, cls=TCLink)
    net.addLink(h2, r1, cls=TCLink)
    net.addLink(r1, r2, cls=TCLink)
    net.addLink(h2, r2, cls=TCLink)

    info( '*** Starting network\n')
    net.build()

    info( '*** Starting controllers\n')
    #for controller in net.controllers:
    #    controller.start()

    info( '*** Starting switches\n')

    info( '*** Post configure switches and hosts\n')
    h1.cmd('ifconfig h1-eth0 inet6 add 1000::2/64')

    h2.cmd('ifconfig h2-eth0 inet6 add 2000::2/64')
    h2.cmd('ifconfig h2-eth1 inet6 add 3000::2/64')

    r1.cmd('ifconfig r1-eth0 inet6 add 1000::1/64')
    r1.cmd('ifconfig r1-eth1 inet6 add 2000::1/64')
    r1.cmd('ifconfig r1-eth2 inet6 add 4000::1/64')

    r2.cmd('ifconfig r2-eth0 inet6 add 4000::2/64')
    r2.cmd('ifconfig r2-eth1 inet6 add 3000::1/64')

    # config route
    h1.cmd('route -A inet6 add default gw 1000::1 dev h1-eth0')
    h2.cmd('route -A inet6 add default gw 2000::1 dev h2-eth0')

    r1.cmd('route -A inet6 add 2000::2/64 gw 2000::2 dev r1-eth1')  # to h2
    r1.cmd('route -A inet6 add 1000::2/64 gw 1000::2 dev r1-eth0')  # to h1
    

    r2.cmd('route -A inet6 add 3000::2/64 gw 3000::2 dev r2-eth1')  # to h2
    r2.cmd('route -A inet6 add 1000::2/64 gw 4000::1 dev r2-eth0')  # to h1

    # open srv6 
    r1.cmd('sysctl -w net.ipv6.conf.all.seg6_enabled=1')
    #r1.cmd('sysctl -w net.ipv6.conf.lo.seg6_enabled=1')
    r1.cmd('sysctl -w net.ipv6.conf.r1-eth0.seg6_enabled=1')
    r1.cmd('sysctl -w net.ipv6.conf.r1-eth1.seg6_enabled=1')
    r1.cmd('sysctl -w net.ipv6.conf.r1-eth2.seg6_enabled=1')

    r2.cmd('sysctl -w net.ipv6.conf.all.seg6_enabled=1')
    #r2.cmd('sysctl -w net.ipv6.conf.lo.seg6_enabled=1')
    r2.cmd('sysctl -w net.ipv6.conf.r2-eth0.seg6_enabled=1')
    r2.cmd('sysctl -w net.ipv6.conf.r2-eth1.seg6_enabled=1')

    # open route
    r1.cmd('sysctl net.ipv6.conf.all.forwarding=1')
    r2.cmd('sysctl net.ipv6.conf.all.forwarding=1')
    
    # config srv6 encapsulation
    r1.cmd('ip -6 route add 3000::2/128 encap seg6 mode encap segs 4000::2 dev r1-eth2')
    # r2.cmd('ip -6 route add 3000::2/128 encap seg6local action End 3000::2 dev r2-eth0')
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()