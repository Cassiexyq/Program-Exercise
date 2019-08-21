# -*- coding: utf-8 -*-

# @Author: xyq

# 到十进制： int('',16)
# 到八进值  oct
# 十进制 到十六  hex()
# 八/二进制 到十六  先转十进制再转十六
# 十进制 到二进制  bin
# 八/十六进值 到二进制 先转十进制再到二进制

import sys

for line in sys.stdin:
    n = int(line, 16) # 转二进制
    # n = hex(int(line)) # 转十六
    print(n)

