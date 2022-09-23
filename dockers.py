import docker
import requests

def main():

  # Connect to the default unix socket (/var/run/docker.sock)
  client = docker.from_env()

  #Pull the nginx:alpine image
  client.images.pull('nginx:alpine')

  #Define some test parameters, our first HTTP port and the number of containers
  portstart = 10000
  count = 1000

  #Create and start 'count' number of containers. Map container port 80 to an external port.
  for a in range(1,count+1):
    container = client.containers.create('nginx:alpine',ports={'80/tcp':portstart+a})
    container.start()
    print('Created container number {} name: {}'.format(a,container.name))

  #Get a list of all the running containers (best you don't run this script on a system which has existing containers running)
  #Iterate through the list, pick out the remote port, and perform a GET request to it to check nginx is online. If the status code is 200, we must be successful!
  container_list = client.containers.list()
  count = 0
  for container in container_list:
    port = container.attrs['HostConfig']['PortBindings']['80/tcp'][0]['HostPort']
    r = requests.get('http://127.0.0.1:{}'.format(port))
    if(r.status_code == 200):  
      print('Container {} is alive and working on port {}!'.format(container.name,port))
      count += 1
    else:
      print('Container {} is dead :( Code: {}'.format(container.name,r.status_code))

  print('Summary: Online Containers: {} Offline Containers: {}'.format(count,len(container_list)-count))
  print('Removing containers...')
 
  #Let's clean up and put our toys back in the toybox.
  for container in container_list:
    container.stop()
    container.remove()

if __name__ == "__main__":
    main()