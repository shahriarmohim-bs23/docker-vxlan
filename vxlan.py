import docker
import subprocess
from subprocess import PIPE
#import ovspy.client

def run_command(command):
    popen = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return popen
def main():
    client = docker.from_env()
    #sudo ovs-vsctl set-manager ptcp:5678
    dockername="docker1"
    #ubuntu-docker = "ubuntu-docker"
    #ovs = ovspy.client.OvsClient(5678)
    #client.images.build(path="./", tag={ubuntu-docker})
    tag="ubuntu-docker"
    image, build_log  = client.images.build(path="./", dockerfile='Dockerfile', tag=tag, rm=True)
    print(image)
    client.containers.run("ubuntu-docker", name={dockername}, network_mode=None,detach=True)
    BR="br0"
    #subprocess.Popen(['/path/to/ovs-vsctl', 'add-br', BR], stdin=None, stderr=None)
    #ovs.add_bridge(BR)
    #sudo ovs-vsctl add-br ovs-br0
    command = ["sudo","ovs-vsctl","add-br",BR]
    run_command(command)
    print(command)
    #sudo ovs-vsctl add-port ovs-br0 veth0 -- set interface veth0 type=internal
    PR = "veth0"
    command = ["sudo","ovs-vsctl","add-port",BR,PR,"--set","interface",PR,"type=internal"]
    run_command(command)
    print(command)
    #sudo ip address add 192.168.1.1/24 dev veth0 
    IP = "192.168.1.1/24"
    command = ["sudo","ip","address","add",IP,"dev",PR]
    run_command(command)
    print(command)
    #sudo ip link set dev veth0 up mtu 1450
    command = ["sudo","ip","link","set","dev",PR,"up","mtu","1450"]
    run_command(command)
    print(command)
    #sudo ovs-docker add-port ovs-br0 eth0 docker1 --ipaddress=192.168.1.11/24 --gateway=192.168.1.1
    ETH="eth0"
    command = ["sudo","ovs-docker","add-port",BR,ETH,dockername,"--ipaddress=192.168.1.11/24"," --gateway=192.168.1.1"]
    run_command(command)
    print(command)
    #sudo ovs-vsctl add-port ovs-br0 vxlan0 -- set interface vxlan0 type=vxlan options:remote_ip=10.0.1.169 options:key=1000
    VXLAN="vxlan0"
    VNI="100"
    command=["sudo","ovs-vsctl","add-port",BR,VXLAN,"--set","interface",VXLAN,"type=vxlan","options:remote_ip=10.0.1.43","options:key=1000"]
    run_command(command)
    print(command)








if __name__ == "__main__":
    main()