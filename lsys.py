import random

class Lsys:
	def widenNetworks(self, lhch):   # Rule 1
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == 'N':
			if rnum < 10:
				rhstr = '[N][N]'
			elif rnum < 70:
				rhstr = '[N][N][N]'
			else:
				rhstr = '[N][N][N][N]'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr

	def populateBaseNetwork(self, lhch):   # Rule 2
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == 'N':
			if rnum < 30:
				rhstr = '###'
			elif rnum < 80:
				rhstr = '####'
			else:
				rhstr = '#####'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr

	def deepenNetworks(self, lhch):   # Rule 3
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == '#':
			if rnum < 60:
				rhstr = '#'
			elif rnum < 65:
				rhstr = '#<#>'
			elif rnum < 70:
				rhstr = '#<##>'
			elif rnum < 85:
				rhstr = '#<###>'
			else:
				rhstr = '#<#####>'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr

	def stringifyNetworks(self, lhch):   # Rule 4
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == '#':
			if rnum < 80:
				rhstr = '#'
			elif rnum < 90:
				rhstr = '#<#>'
			else:
				rhstr = '#<#<#>>'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr

	def createEndpoints(self, lhch):   # Rule 5
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == '#':
			if rnum < 30:
				rhstr = 'E'
			else:
				rhstr = '#'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr

	def capEndpoints(self, lhch):   # Rule 6
		rhstr = ""
		if lhch == '#':
			rhstr = 'E'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr

	def vulnerablizeEndpoints(self, lhch):   # Rule 7
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == 'E':
			if rnum < 60:
				rhstr = 'E'
			elif rnum < 70:
				rhstr = 'E{V}'
			elif rnum < 80:
				rhstr = 'E{VV}'
			elif rnum < 90:
				rhstr = 'E{VVV}'
			else:
				rhstr = 'E{VVVVV}'
		else:
			rhstr = lhch
		#print rhstr
		return rhstr

	def finalizeVulnerabilities(self, lhch):   # Rule 8
		rnum = str(random.randint(0, 100))
		# add in stuff to make sure you don't get the same vulnerability twice.
		rhstr = ""
		if lhch == 'V':
			rhstr = rnum + ","
		else:
			rhstr = lhch
		#print rhstr
		return rhstr

        def processString1(self, oldStr):#, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.widenNetworks(ch)
                #self.axiom = newstr
		#print newstr
		return newstr

	def processString2(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.populateBaseNetwork(ch)
		#print newstr
		return newstr

	def processString3(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.deepenNetworks(ch)
		#print newstr
		return newstr

	def processString4(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.stringifyNetworks(ch)
		#print newstr
		return newstr

	def processString5(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.createEndpoints(ch)
		#print newstr
		return newstr

	def processString6(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.capEndpoints(ch)
		#print newstr
		return newstr

	def processString7(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.vulnerablizeEndpoints(ch)
		#print newstr
		return newstr

	def processString8(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.finalizeVulnerabilities(ch)
		#print newstr
		return newstr


	def __init__(self,numIters,axiom):
                self.numIters = numIters
                self.axiom = axiom
                #self.networkString = ""

        def buildString(self):
		startString = self.axiom
		endString = ""
                #processString1()

		endString = endString + self.processString1(startString)
		startString = endString
		endString = ""

		endString = endString + self.processString2(startString)
		startString = endString
		endString = ""

		for i in range(self.numIters):
			endString = endString + self.processString3(startString)
			startString = endString
			endString = ""

			endString = endString + self.processString4(startString)
			startString = endString
			endString = ""

			endString = endString + self.processString5(startString)
			startString = endString
			endString = ""

		endString = endString + self.processString6(startString)
		startString = endString
		endString = ""

		endString = endString + self.processString7(startString)
		startString = endString
		endString = ""

		endString = endString + self.processString8(startString)
		startString = endString
		endString = ""

                self.axiom = startString
               # startString = startString
		#return startString
		#print "done now"
