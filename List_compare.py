class intersection():
	
	def inter(self, lst1, lst2):
		inter_lst = []
		for i in lst1:
			if i in lst2 and i not in inter_lst:
				inter_lst.append(i)
		print"::Intersection: ",inter_lst	

class_obj = intersection()
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
class_obj.inter(a, b)
