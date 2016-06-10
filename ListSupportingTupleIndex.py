# -* - coding: UTF-8 -* -
#!/usr/bin/python
# Tested only in python 3.x, not tested in python 2.x

# class ListSupportingTupleIndex(list):
# 	pass

'''
模仿 numpy.array

>>> m
array([[1, 2],
       [3, 4]])
>>> m[0,0]
1
#这是python自动裹tuple造成的语法糖吧...
>>> m[(0,0)]
1
#这才是真相吧... 试一试
>>> m[[0,0]]
array([[1, 2],
       [1, 2]])
#mma之风... 暂缓支持

>>> m[0:1:1]
array([[1, 2]])
>>> m[0:1:1,0:1:1]
array([[1]])
# slice吊吊的


http://stackoverflow.com/questions/1957780/how-to-override-operator
__getitem__(arg)
__setitem__(arg)
__delitem__(arg) #?
if isinstance(arg, slice)
s=slice(1,9,2)
s.start s.stop s.step 
s.indice(int) #?


'''
class ListSupportingTupleIndex(list):
	def __getitem__(self, indices):
		if isinstance(indices,int):
			return super().__getitem__(indices)
		elif isinstance(indices,tuple):
			this=self # Using 'self' is just OK!! (may be some bad impact)
			for index in indices:
				this=this[index]
			return this


if __name__ == '__main__':
	m=ListSupportingTupleIndex([[1,2],[3,4]])
	print(m[0,0])

