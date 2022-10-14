import docker
def main():
    client = docker.from_env()
    #sudo ovs-vsctl set-manager ptcp:5678
    #sudo chmod 666 /var/run/docker.sock

    dockername="docker1"
    #ubuntu-docker = "ubuntu-docker"
    #ovs = ovspy.client.OvsClient(5678)
    #client.images.build(path="./", tag={ubuntu-docker})
    tag="ubuntu-docker"
    image, build_log  = client.images.build(path="./", dockerfile='Dockerfile', tag=tag, rm=True)
    print(image)
    client.containers.run("ubuntu-docker", name={dockername}, network_mode=None,detach=True)
if __name__ == "__main__":
    main()