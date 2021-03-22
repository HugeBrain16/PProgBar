__version__='0.0.2'

class Progger:
	def __init__(self,x,y,min,max):
		self.x = x
		self.y = y
		self.min = min
		self.max = max

	def create(self,filename,color):
		"""create a progress bar image"""
		from PIL import Image
		bg=Image.new('RGB',size=(self.x,self.y),color=(60,60,60))
		fl=Image.new('RGB',size=(round((self.min/self.max) * self.x),self.y),color=color)
		bg.paste(fl)
		bg.save(filename)
		return filename