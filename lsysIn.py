
#import stuff
import random, os, errno

currentNetwork = 'a'
charList = ""
networkList = []
numNetworks = 0
numHosts = 0

# generate home dir
try:
  os.makedirs('home')
except OSError as e:
  if e.errno != errno.EEXIST:
    raise

# define code to generate full subnet block
def genNetwork():
	global numNetworks
	numNetworks += 1
	currentNetwork = "network" + str(numNetworks)
	networkList.append(currentNetwork)
	return currentNetwork

# generate other networks
def genEnterprise(charList):
	for x in charList:
		if x == '[': # [ , generate new network
			network = genNetwork()
			relevantNetwork = network
			print "There was a [! Spawn a network!"
		elif x == '<': # < , generate new stubNetwork
			network2 = genNetwork()
			relevantNetwork = network2
			print "There was a <! Spawn a network!"
		elif x == '$': # $ , generate new serialNetwork
			network3 = genNetwork()
			relevantNetwork = network3
			print "There was a $! Spawn a network!"
		elif x == '#': # # , generate new host
			# generate folder for docker
			global numHosts
			numHosts += 1
			machineId = relevantNetwork + str(numHosts)
			try:
			  os.makedirs("home\\" + machineId)
			except OSError as e:
			  if e.errno != errno.EEXIST:
				raise
			# put stuff in the file here
			f = open('home\\' + machineId + '\\Dockerfile', 'a')
			f.write("FROM alpine\nCMD ['top']")
			f.close()
			
			f = open('home\\docker-compose.yml', 'a')
			f.write('''  host%s%s:
			build: .\\%s
			image: %s
			networks:
			  - %s\n''' % ("host", machineId, machineId, machineId, relevantNetwork))
			f.close()
		else: # skip bullshit
			print "nothing"

# test stuff
var = "[#<#><#>$#<#>$#<#$#<#>>][#<#$#>$#$#<#$#>$#<#$#<#>>][#<#><#>]"
genEnterprise(var)
	
# print network info to file
f = open('home\\docker-compose.yml', 'a')
f.write("\n################ NETWORKING ################\n")
f.write('networks:\n')
for x in networkList:
  f.write('''
  %s:
    driver: bridge
''' % x)
f.close()