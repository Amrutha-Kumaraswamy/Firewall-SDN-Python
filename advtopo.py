
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost1 = self.addHost( 'h3',ip="10.0.1.2",defaultRoute="via 10.0.1.1" )
        rightHost1 = self.addHost( 'h5',ip="10.0.2.2",defaultRoute="via 10.0.2.1" )
        leftHost2 = self.addHost( 'h4',ip="10.0.1.3",defaultRoute="via 10.0.1.1" )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )

        # Add links
        self.addLink( leftHost1, switch1 )
        self.addLink( rightHost1, switch2 )
        self.addLink( leftHost2, switch1 )
        self.addLink( switch1, switch2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }