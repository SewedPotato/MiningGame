# wattodo

sav = [] # savecode string

class Save:
	def __init__(self):
		# how
		pass
	def Save(self,givemedata,givemoredata):
		global sav
		self.gmd = givemedata
		self.gmmd = givemoredata
		sav.append(gmd)
		sav.append("->")
		sav.append(gmmd)
		compiled = encode(sav)
		print(compiled)
		
