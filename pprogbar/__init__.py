__version__='0.0.1'

class Progger:
	def __init__(self,x,y,min,max,color):
		"""
			Params:
				- x
					image width
				- y
					image height
				- min
					progress fill
				- max
					max progress fill
				- color
					color?
		"""
		self.x = x
		self.y = y
		self.min = min
		self.max = max
		self.color = color

	def create(self,filename):
		"""create a progress bar image"""
		from PIL import Image
		bg=Image.new('RGB',size=(self.x,self.y),color=(60,60,60))
		fl=Image.new('RGB',size=(round((self.min/self.max) * self.x),self.y),color=self.color)
		bg.paste(fl)
		bg.save(filename)
		return filename