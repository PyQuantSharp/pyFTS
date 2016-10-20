from pyFTS import *
from functools import reduce
import numpy as np


class FLRGTreeNode:
	
	def __init__(self,value):
		self.isRoot = False
		self.children = []
		self.value = value
		
	def appendChild(self,child):
		self.children.append(child)
	
	def getChildren(self):
		for child in self.children:
			yield child
		
	def getPaths(self):
		if len(self.children) > 0:
			for child in self.children:
				tmp = [self.value]
				tmp.extend(child.getPaths())
				yield tmp
		else:
			yield self.value
			
	def getStr(self,k):
		if self.isRoot:
			tmp = str(self.value)
		else:
			tmp = "\\" + ("-" * k) + str(self.value)
		for child in self.getChildren():
			tmp = tmp + "\n" + child.getStr(k + 1)
		return tmp
		
	def __str__(self):
		return self.getStr(0)

class FLRGTree:
	def __init__(self):
		self.root = FLRGTreeNode(None)

def flat(dados):
	for inst in dados:
		if isinstance(inst, (list, tuple)):
			x = flat(inst)
			for k in x:
				yield k
		else:
			yield inst
