# Entropy Based DDos Attack Detection in a Software Defined Network
    
    detection.py - Has the actual code for entropy calculation and DDoS determination
    l2_learning_edited.py - l2 learning mode of POX controller with hooks into the entropy-based detection code
    launchAttack.py - Script which generates attack traffic
    launchTraffic.py - Script which generates normal traffic


python ./pox.py openflow.of_01 --port=6633 forwarding.l2_learning_edited

+

sudo mn --switch=ovsk --topo=tree,depth=2,fanout=7 --controller=remote,ip=127.0.0.1,port=6633

mininet> xterm h1 h2 h3

python launchTraffic.py -s 2 -e 49
# Here, -s and -e specify the starting and ending octets of IPs starting with 10.0.0.x who we have to send packets to

python launchAttack.py 10.0.0.10
# Here, the only argument is the IP address of the host in the network we want to attack.


