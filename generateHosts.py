import os, errno, random

# class to generate hosts
class GenerateHosts(object):
  
  

  def __init__(self, networkName, hostname):
    
    machineId = networkName + str(hostname)
    
    # generate folder for docker
    try:
      os.makedirs("home/" + machineId)
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise
    
    # put stuff in the file here
    f = open('home/' + machineId + '/Dockerfile', 'a')
    f.write("FROM alpine\nCMD ['top']")
    f.close()
    
    f = open('home/docker-compose.yml', 'a')
    f.write('''  host%s%s:
    build: ./%s
    image: %s
    networks:
      - %s\n''' % (networkName, hostname, machineId, machineId, networkName))
    f.close()
    
    # print ips to console (debugging)
    #print machineId