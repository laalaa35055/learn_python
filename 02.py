list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 宣告清單 List
print(list)                         
list.append(10)                     # 新增資料至清單中
print(list)
first = list[0]                     # 查詢清單資料
print(first)
print(list[3])                      # 查詢第二筆資料
list[1] = 100                       # 更改第二筆資料
print(list)
del list[4]                         # 刪除第 5 筆資料
print(list)