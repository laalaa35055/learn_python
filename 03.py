dict = {
    "title": "book no name",
    "writer": "hello",
    "age": 10,
    "buy": False
}

# 查詢字典 title 和 age 
print(dict["title"])
print(dict["age"])

dict["website"] = "tibame"      # 新稱網站 = tibame
print(dict["website"])

dict["age"] = 100               # 改變字典裡的 age 為 100
print(dict["age"])

del dict["website"]             #刪除字典裡的 website
print(dict)