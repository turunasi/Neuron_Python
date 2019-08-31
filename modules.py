import numpy as np

class memory:

	def __init__ (self,neuron):
		self.neuron = neuron
		self.matrix = matrix_from_neuron(neuron)
		self.count = 0
		print("\nThe input states of neurons:\n",self.neuron)
		print("\nMatrix calculated from the neuron:\n",self.matrix)

def matrix_init (n):
	return np.zeros((n,n),dtype=np.int)

def matrix_from_neuron (neuron):
	n = len(neuron)
	m = matrix_init(n)
	for i in range(n):
		for j in range(n):
			if i == j: continue
			m[i][j] = hebb(neuron[i],neuron[j])
	return m

def hebb (a,b):
	if a == 1 and b == 1: return 1
	return -1
