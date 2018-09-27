class Node:
	def __init__(self, inbound_nodes=[]):
		# Node(s) from which the current node receives
		# input
		self.inbound_nodes = inbound_nodes
		# current node is the outbound node to all the
		# inbound nodes
		for node in self.inbound_nodes:
			node.outbound_nodes.append(self)
		self.outbound_nodes = []
		# every node will have a value which it its output
		self.value = None

	def forward(self):
		"""
		Forward propagation.
		Compute the output value based on `inbound_nodes` and
		store the result in self.value
		"""
		raise NotImplemented


class Input(Node):
	def __init__(self):
		Node.__init__(self)

	# for input node set the value explicitly
	def forward(self, value=None):
		if value is not None:
			self.value = value


class Add(Node):
	def __init__(self, *args):
		Node.__init__(self, [*args])

	def forward(self):
		self.value = 0
		for node in self.inbound_nodes:
			self.value += node.value


class Mul(Node):
	def __init__(self, *args):
		Node.__init__(self, [*args])

	def forward(self):
		self.value = 1
		for node in self.inbound_nodes:
			self.value *= node.value






















