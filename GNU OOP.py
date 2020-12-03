class Matrix:

	def __init__(self, row = 0, col = 0):
		mtrx_list = []
		num = 1
		for _ in range(row):
			tmp = []
			for _ in range(col):
				tmp.append(num)
				num += 1
			mtrx_list.append(tmp)

		self.data = mtrx_list
		self.row = len(self.data)
		self.col = len(self.data[0]) if row != 0 else 0 # 데이터가 한개도 없으면 0
	
	def __str__(self): # return str
		return_str = ""
		length = len(self.data)

		if length == 0: # 예외처리
			return "[[]]"

		for i in range(length - 1): # 의미없는 엔터 없애기 위해 한 줄 제외
			return_str += (str(self.data[i]) + '\n')
		return_str += str(self.data[length - 1]) # 마지막 행 출력(end = '')

		return return_str

	def __mul__(self, num): # return multiplied object, 원본훼손 X

		'''일회용 Matrix 만들기'''
		row = len(self.data) # 원본의 행의 개수
		col = len(self.data[0]) if row != 0 else 0 # 원본의 열의 개수
		Mtrx = Matrix(row, col)
		'''일회용 Matrix 만들기 끝'''

		multiplied = [] # 숫자 곱한 행렬
		for i in self.data:
			tmp = []
			for j in i:
				tmp.append(j * num)
			multiplied.append(tmp)

		'''일회용 Matrix의 data 수정'''
		Mtrx.data = multiplied

		'''Return 일회용 Matrix'''
		return Mtrx 

	def getTranspose(self): # return transposed object, 원본훼손 X
		if len(self.data) == 0: # 예외처리
			return Matrix(0, 0)

		'''일회용 Matrix 만들기'''
		row = len(self.data)
		col = len(self.data[0]) if row != 0 else 0
		Mtrx = Matrix(row, col)
		'''일회용 Matrix 만들기 끝'''

		transposed = [] # 
		for idx in range(len(self.data[0])): # len(self.data[0]) == 열의 크기
			tmp = []
			for i in self.data:
				tmp.append(i[idx])
			transposed.append(tmp)

		'''일회용 Matrix의 data 수정'''
		Mtrx.data = transposed

		'''Return 일회용 Matrix'''
		return Mtrx

	def doTranspose(self): # return None, 원본훼손 O
		if len(self.data) == 0: # 예외처리
			return Matrix(0, 0)

		transposed = []
		for idx in range(len(self.data[0])): # len(self.data[0]) == 열의 크기
			tmp = []
			for i in self.data:
				tmp.append(i[idx])
			transposed.append(tmp)
		
		'''원본 data 수정'''
		self.data = transposed

	def getElement(self, x, y): # return int, 원본훼손 X
		if len(self.data) == 0 or len(self.data) < x or len(self.data[0]) < y: # 예외처리
			return None

		return self.data[x - 1][y - 1]

	def setElement(self, x, y, new_value): # return None, 원본훼손 O
		if len(self.data) == 0 or len(self.data) < x or len(self.data[0]) < y: # 예외처리
			return None
		
		'''원본 data 수정'''
		self.data[x - 1][y - 1] = new_value

def main():
	m1 = Matrix(2, 3)
	print("--------------m1---------------")
	print(m1)
	print("---------getElement------------")
	print(m1.getElement(2, 2))
	print("---------setElement------------")
	m1.setElement(2, 2, -10)
	print(m1)
	print("------------m1 * 3-------------")
	print(m1 * 3)
	print("--------------m1---------------")
	print(m1)
	print("---------getTranspose----------")
	print(m1.getTranspose())
	print("--------------m1---------------")
	print(m1)
	print("----------doTranspose----------")
	print(m1.doTranspose())
	print("--------------m1---------------")
	print(m1)
	print("-------------------------------")

	print("===============================")
	print("===============================")

	m2 = Matrix() # 빈 행렬일 때 예외 확인 용
	print("--------------m2---------------")
	print(m2)
	print("---------getElement------------")
	print(m2.getElement(2, 2))
	print("---------setElement------------")
	m2.setElement(2, 2, -10)
	print(m2)
	print("------------m2 * 3-------------")
	print(m2 * 3)
	print("--------------m2---------------")
	print(m2)
	print("---------getTranspose----------")
	print(m2.getTranspose())
	print("--------------m2---------------")
	print(m2)
	print("----------doTranspose----------")
	print(m2.doTranspose())
	print("--------------m2---------------")
	print(m2)
	print("-------------------------------")

main()