import random, generateHosts

# class to generate networks
class GenerateNetworks:

  __networkString = 'a'
  __numberOfHosts = 0
  __networkName = 'a'
  
  def __init__(self, numberOfHosts, numberOfNetworks):
    # define network name
    self.__networkName = "network" + str(numberOfNetworks)
    
    # generate hosts for this network
    while numberOfHosts > 0:
      self.__generatedHost = generateHosts.GenerateHosts(self.__networkName, numberOfHosts)
      numberOfHosts -= 1

  # return network string
  def getNetworkName(self):
    return self.__networkName