# 打印出字串，帶return的函數
def say_hello(msg:str = ""):
    return f"Hello, { msg }!"

say = say_hello("World !!")  # 獲取函數返回值
print(say) 