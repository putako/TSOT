# import bullshit
import random, os, errno, generateNetworks

# Global variables
numberOfHosts = 15
numberOfHostsTracker = numberOfHosts
networkNames = []
numberOfNetworks = 0

# Build folder for docker files
try:
  os.makedirs('home')
except OSError as e:
  if e.errno != errno.EEXIST:
    raise

# docker-compose network information
f = open('home/docker-compose.yml', 'a')
f.write('version: "3"\nservices:\n')
f.close()

# generate all networks
while numberOfHosts > 0:
  hostsOnThisNetwork = random.randint(1, (numberOfHostsTracker / 3) + 1)
  network = generateNetworks.GenerateNetworks(hostsOnThisNetwork, numberOfNetworks)
  numberOfHosts -= hostsOnThisNetwork
  
  numberOfNetworks += 1

  networkNames.append(network.getNetworkName())
  
print(networkNames)

f = open('home/docker-compose.yml', 'a')
f.write("\n################ NETWORKING ################\n")
f.write('networks:\n')

# write networking information
for x in networkNames:
  f.write('''
  %s:
    driver: bridge
''' % x)

f.close()


"""
# Global variables
numberOfHosts = 15
numberOfHostsTracker = numberOfHosts
networkStrings = []

# Build folder for docker files
try:
  os.makedirs('home')
except OSError as e:
  if e.errno != errno.EEXIST:
    raise
  
# generate all networks
while numberOfHosts > 0:
  hostsOnThisNetwork = random.randint(1, (numberOfHostsTracker / 3) + 1)
  network1 = generateNetworks.GenerateNetworks(hostsOnThisNetwork)
  numberOfHosts -= hostsOnThisNetwork

  networkStrings.append(network1.getNetworkString())
  
print(networkStrings)  

# docker-compose network information
f = open('home/docker-compose.yml', 'a')
f.write("\n")

# god will punish me for my sins
for x in networkStrings:
  f.write(x + "\n")
f.close()
  
# connect networks
"""