class DynamicArray:
	def __init__(self, val):
		if isinstance(val, int):
			self._n = 0
			self._capacity = val
			self._A = self.makearray(self._capacity)

		else:
			self._n = 0
			self._capacity = len(val)
			self._A = 2*val

	def append(self, ele):
		if self._n == self._capacity:
			self.resize(2*self._capacity)
			self._A[self._n] = ele
			self._n += 1

	def insert(self, index, ele):
		if not (index <= self._n):
			raise IndexError("Index out of Range")
			
		if self._n == self._capacity:
			self.resize(2*self._capacity)
