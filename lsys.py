import random

class Lsys:
	def baseNetwork(self, lhch):
		rhstr = ""
		if lhch == 'N':
			rhstr = '[N]'
			
		return rhstr
		
	def populateBaseNetwork(self, lhch):
		rnum = random.randint(0, 100)
		rhstr = ""        
		if lhch == 'N':
			if rnum < 60:
				rhstr = '###'
			elif rnum < 80:
				rhstr = '####'
			else:
				rhstr = '#####'
		else:
			rhstr = lhch
		return rhstr
		
	def hairifyNetwork(self, lhch):
		rnum = random.randint(0, 100)
		rhstr = ""        
		if lhch == '#':
			if rnum < 70:
				rhstr = '#'
			elif rnum < 80:
				rhstr = '#<#<#<#>>>'
			elif rnum < 90:
				rhstr = '#<#<#<#<#>>>>'
			else:
				rhstr = '#<#<#<#<#<#>>>>>'
		else:
			rhstr = lhch
		return rhstr
		
	def chubbifyNetwork(self, lhch):
		rnum = random.randint(0, 100)
		rhstr = ""        
		if lhch == '#':
			if rnum < 70:
				rhstr = '#'
			elif rnum < 80:
				rhstr = '#<###>'
			elif rnum < 90:
				rhstr = '#<####>'
			else:
				rhstr = '#<#####>'
		else:
			rhstr = lhch
		return rhstr
		
	def splitifyNetwork(self, lhch):
		rnum = random.randint(0, 100)
		rhstr = ""        
		if lhch == '#':
			if rnum < 70:
				rhstr = '#'
			elif rnum < 90:
				rhstr = '#<#><#>'
			else:
				rhstr = '#<#><#><#>'
		else:
			rhstr = lhch
		return rhstr
		
	def stuffEnds(self, lhch):
		rhstr = ""
		if lhch == '#':
			rhstr = 'E'
		else:
			rhstr = lhch
		return rhstr
		
	def chanceToStuffEnds(self, lhch):
		rnum = random.randint(0, 100)
		rhstr = ""
		if lhch == '#':
			if rnum < 90:
				rhstr = 'E'
			else:
				rhstr = '#'
		else:
			rhstr = lhch
		return rhstr

	def processBaseNetwork(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.baseNetwork(ch)
		return newstr
		
	def processPopulateBaseNetwork(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.populateBaseNetwork(ch)
		return newstr
		
	def processHairifyNetwork(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.hairifyNetwork(ch)
		return newstr
		
	def processChubbifyNetwork(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.chubbifyNetwork(ch)
		return newstr
		
	def processStuffEnds(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.stuffEnds(ch)
		return newstr
		
	def processChanceToStuffEnds(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.chanceToStuffEnds(ch)
		return newstr
		
	def processSplitifyNetwork(self, oldStr):
		newstr = ""
		for ch in oldStr:
			newstr = newstr + self.splitifyNetwork(ch)
		return newstr

	def __init__(self,numIters,axiom):
                self.numIters = numIters
                self.axiom = axiom

	def buildString(self):
		startString = self.axiom
		endString = ""

		# Stuff before iterables go here
		endString = endString + self.processBaseNetwork(startString)
		startString = endString
		endString = ""
		
		endString = endString + self.processPopulateBaseNetwork(startString)
		startString = endString
		endString = ""

		# Iterables go here
		for i in range(self.numIters):
			endString = endString + self.processHairifyNetwork(startString)
			startString = endString
			endString = ""
			
			endString = endString + self.processChubbifyNetwork(startString)
			startString = endString
			endString = ""
			
			endString = endString + self.processSplitifyNetwork(startString)
			startString = endString
			endString = ""
			
			#endString = endString + self.processChanceToStuffEnds(startString)
			#startString = endString
			#endString = ""
		
		# Stuff after iterables go here
		endString = endString + self.processStuffEnds(startString)
		startString = endString
		endString = ""
		
		print(startString)

		self.axiom = startString
