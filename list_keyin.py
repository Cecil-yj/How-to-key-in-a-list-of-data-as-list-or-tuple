null_lst = []      			# 定义一个空列表
times = 0       			# 对次数赋初值

set_times = int(input("请输入循环的次数："))

while times < set_times:
	null_lst_data = input("请输入需要保存的数据：")   		# 对列表赋数据
	null_lst.append(null_lst_data)            		 # 将数据添加到列表中
	times += 1    		   # 次数自增
lst_tuple = tuple(null_lst)        # 列表转换为元组
print(lst_tuple)   	           # 输出列表
