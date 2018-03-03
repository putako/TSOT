#import stuff
import os, errno, lsys

# generate home dir
try:
  os.makedirs('home')
except OSError as e:
  if e.errno != errno.EEXIST:
    raise

# Generate information about networks from charList
def dockerWriter(charList):
	# Declare necessary variables
	networkID = []
	networkPrint = []
	netNum = 0
	machNum = 0

	# Open files
	f = open('home/docker-compose.yml', 'a')

	# Write static header
	f.write('version: "3"\n')

	# Don't look down....
	for index, x in enumerate(charList):
		if x == '[': # IF we see a [ at x index, do rule
			networkID.append(netNum)
			networkPrint.append(netNum)
			netNum += 1
			print(networkID)
		elif x == '<': # IF we see a < at x index, do rule
			networkID.append(netNum)
			networkPrint.append(netNum)
			netNum += 1
			print(networkID)
		elif x == ']':
			networkID = networkID[:-1]
			print(networkID)
		elif x == '>':
			networkID = networkID[:-1]
			print(networkID)
		elif x == 'E':
			#### DOCKER SPECIFIC FILE STUFF ####
			# generate folder for docker


			if charList[index - 1] == '<':
				machineName = "device_" + str(machNum)
			else:
				machineName = "machine_" + str(machNum)

			try:
			  os.makedirs("home/" + machineName)
			except OSError as e:
			  if e.errno != errno.EEXIST:
				raise

			# put stuff in the file here
			e = open('home/' + machineName + '/Dockerfile', 'a')
			e.write("FROM alpine\nCMD ['top']")
			e.close()

			# iterate machNum
			machNum += 1

			#### DOCKER COMPOSE FILE STUFF ####
			f.write('  host%s:\n' % machineName)
			f.write('    build: ./%s\n' % machineName)
			f.write('    image: %s\n' % machineName)
                        f.write('    ports:\n')
                        f.write('     - "2222:22"\n')
			f.write('    networks:\n')
			f.write('      - %s\n' % ("network" + str(networkID[-1])))
			if charList[index - 1] == '<':
				f.write('      - %s\n' % ("network" + str(networkID[-2])))
		else:
			pass

	# Write networking info
	f.write("\n################ NETWORKING ################\n")
	f.write("networks:\n\n")

	for x in networkPrint:
		f.write("  network%s:\n" % x)
		f.write("    driver: bridge\n\n")

	# Close files
	f.close()

charList = lsys.Lsys(1, "N")
charList.buildString()
#charList = "[EE<E<E><E>>][E<EE><EE<E><E>>]"
dockerWriter(charList.axiom)
