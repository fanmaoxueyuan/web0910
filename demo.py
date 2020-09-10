# 将abcde 使用base64 加密

import base64
a = "abcdefg"
# 字符串转换字节类型
b = a.encode()

print(type(b),b)
# 加密
print( base64.b64encode(b))
bencode = base64.b64encode(b)

# 解密
ecode = base64.b64decode(bencode)
print(ecode,type(ecode))
# 字节转换为字符串
de = ecode.decode()
print(de,type(de))