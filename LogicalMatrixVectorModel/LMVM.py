from datadict import diseases
import numpy as np

# Standard schema for LMVM. It must be followed
mydict = {
	'a': ['toyota', 'bmw', 'audi', 'tata'],
	'b': ['bmw', 'mercedes', 'porshe', 'honda'],
	'c': ['tesla', 'porsche', 'audi', 'lucid'],
	'd': ['honda', 'hyundai', 'mahindra', 'audi'],
	'e': ['jeep', 'tata', 'ford', 'gm', 'toyota']
}


class LMVM:
	""" LMVM stands for Logical Matrix Model it is used
	to create matrix from given dictionary and solve a 
	percentvector or frequency vector. In order to use 
	this class you need to initialize it with dictionary
	like LMVM(mydict)"""
	def __init__(self, mydict):
		try: # check if import is wrong then raise error
			import numpy as np
			np.set_printoptions(threshold=np.inf)
			self.np = __import__('numpy')
		except ImportError as err:
			print(err)
		self.mydict = mydict
		self.simple_arr = None
		self.percent_arr = None

	def __dictToList(self): # convert dict to list return items and values
		objects = list(self.mydict.keys())
		features = list(self.mydict.values())
		return objects, features

	def __Union(self): #Union of all features
		objs, feats = self.__dictToList()
		mylist = [item for sublist in feats for item in sublist]
		l = list(set(mylist))
		l.sort()
		return l

	def toMatrix(self):
		"""Preparation of matrix of n by m elements"""
		objects, feats = self.__dictToList()
		union_feats = self.__Union()
		m = self.np.zeros((len(objects), len(union_feats)), 
								dtype = self.np.uint8)
		for i in range(len(feats)):
			for j in range(len(feats[i])):
				if feats[i][j] in union_feats:
					indics = union_feats.index(feats[i][j])
					m[i][indics] = 1
		return m

	def solve(self, inp, type = None):
		"""it will apply input vector to matrix and return
		percent vector or frequency vector. it takes N size
		.obj_feat_counts will return frequency vector of 
		input vector as parameter. simple_arr will return
		occurence vector  and percent_arr will return percent
		vector """

		objs, feats = self.__dictToList()
		obj_feat_counts = self.np.transpose([len(i) for i in feats]) 
		m = self.toMatrix()
		inp = self.np.transpose(inp)
		rows, cols = m.shape
		irows = len(inp)
		if cols != irows:
			raise Exception('Size of input vector must match Matrix rows')
		self.simple_arr = m@inp
		self.percent_arr = np.round_(np.multiply(100/obj_feat_counts, 
										self.simple_arr), decimals = 0)
		if type == 'percent':
			return self.percent_arr
		else:
			return self.simple_arr


	def whichObject(self, max_value):
		#whichObject takes max value and return name of the object
		objs, feats = self.__dictToList()
		obj_feat_counts = self.np.transpose([len(i) for i in feats])
		indics = [i for i, v in enumerate(obj_feat_counts) if i == max_value]
		obj_name = [objs[i] for i in indics]
		if len(obj_name) == 1:
			return obj_name[0]
		else:
			return obj_name

	def print(self):
		i, v = self.__dictToList()
		print('Items:', i)
		print()
		print(self.__Union())
		print()
		print(self.toMatrix())


# Calling LMVM Class and passing the dictionay
m = LMVM(diseases)

#checking the prepared matrix shape
r, c = m.toMatrix().shape

#generating a random input for checking LMVM
a = np.random.randint(2, size = c)

# solving matrix vector product
print(m.solve(a)) #, type = 'percent'

#
maxx = max(m.solve(a))
print(maxx)
maxd = m.whichObject(maxx)
print(maxd)
m.print()


