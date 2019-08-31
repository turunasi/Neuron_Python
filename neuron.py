import numpy as np
import modules as m

def main():

	memories = np.array([])

	print("\nThis program is simple memorization model")
	n = int(input("Define the number of neurons:"))
	brain = m.matrix_init(n)
	
	while True:
		print("\n+----------------------------------------------+")
		print("|1: Make the state of neurons into the memory  |")
		print("|2: Let the brain memorize the memory          |")
		print("|3: Let the brain remember the memory          |")
		print("|4: Check the state of the brain               |")
		print("|5: Check the memories                         |")
		print("|6: Initialize the brain                       |")
		print("|7: Initialize the memories                    |")
		print("|other: quit this program                      |")
		print("+----------------------------------------------+\n")
		cmd = int(input("Please input command:"))
	
		if cmd == 1:
			neuron = np.zeros(n,dtype=np.int)
			print("\nInput state of each neuron by a integer 1 or -1")
			print("1:active -1:inactive")
			for i in range(n):
				neuron[i] = int(input("State of neuron[%d] :" %i))
			memories = np.append(memories,m.memory(neuron))
			print("\nAdd new memory[{}] into memories".format(len(memories)-1))
		
		elif cmd == 2:
			if empty_memories(memories):continue
			word = ""
			while (word in "NO No N no n"):
				print("Your created memory is...")
				for i in range(len(memories)):
					print("\nneuron[%d](count:%d) :\n" %(i,memories[i].count),memories[i].neuron)
				selected = int(input("Select memory to memorize:"))
				print("Selected memory is...\n",memories[selected].neuron)
				word = input("Let brain memorize this memory (Y/n):")
			count = int(input("How many times do you want to memorize?:"))
			brain += count*memories[selected].matrix
			memories[selected].count += count
			print("\nThe state of brain is...\n",brain)
		
		elif cmd == 3:
			if empty_memories(memories):continue
			print("Your created memory is...")
			for i in range(len(memories)):
				print("\nneuron[%d](count:%d) :\n" %(i,memories[i].count),memories[i].neuron)
			print("Input state of each neuron by a integer 1 or -1 or 0")
			print("1:active -1:inactive 0:unknown")
			for i in range(n):
				neuron[i] = int(input("state of neuron[%d] :" %i))
			answer = np.dot(brain,neuron)
			print("The answer is\n",answer)
		
		elif cmd == 4:print("\nThe brain is...\n",brain)
		
		elif cmd == 5:
			if empty_memories(memories):continue
			for i in range(len(memories)):
				print("memory[%d](count:%d):" %(i,memories[i].count),"\n",memories[i].neuron,"\n",memories[i].matrix)
		
		elif cmd == 6:
			if empty_memories(memories):continue
			if (input("Is It OK?(Y/n):") in ("NO No N no n")):continue
			brain = m.matrix_init(n)
			for i in range(len(memories)):memories[i].count = 0
			print("\nInitialize the brain\n")
		
		elif cmd == 7:
			if (input("Is It OK?(Y/n):") in ("NO No N no n")):continue
			memories = np.array([])
			print("\nInitialize the memories\n")
		
		else:
			print("bye!")
			break

def empty_memories (memories):
	if len(memories) != 0:return False
	print("No memory !!")
	return True

if __name__ == '__main__':
	main()
