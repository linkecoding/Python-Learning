# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil

print("CPU信息".center(50, '-'))
# 获取CPU信息
# CPU逻辑数量
print(psutil.cpu_count())
# CPU物理核心
print(psutil.cpu_count(logical=False))
# 统计CPU的用户/系统/空闲时间
print(psutil.cpu_times())

# CPU使用率,每秒刷新一次,共10次
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))

# 获取内存信息
print("内存信息".center(50, '-'))
# 获取物理内存
print(psutil.virtual_memory())
# 获取交换内存
print(psutil.swap_memory())


# 获取磁盘信息
print("磁盘使用情况".center(50, '-'))
# 磁盘分区情况
print(psutil.disk_partitions())
# 磁盘使用情况
print(psutil.disk_usage('/'))
# 磁盘IO
print(psutil.disk_io_counters())

# 获取网络信息
print("网络信息".center(50, '-'))
# 获取网络读写字节和/包的个数
print(psutil.net_io_counters())
# 获取网络接口信息
print(psutil.net_if_addrs())
# 获取网络接口状态
print(psutil.net_if_stats())
# 当前网络连接信息
print(psutil.net_connections())

print("进程信息".center(50, '-'))
# 所有进程ID
print(psutil.pids())
p = psutil.Process(1809)
print(p.name())
print(p.exe())
print(p.cwd())
print(p.cmdline())
print(p.ppid())
print(p.parent())
print(p.children())
print(p.status())
print(p.username())
print(p.create_time())
print(p.terminal())
print(p.cpu_times())
print(p.memory_info())
print(p.open_files())
print(p.connections())
print(p.num_threads())
print(p.threads())
print(p.environ())

# 模拟ps的效果
print("模拟ps".center(50, '-'))
print(psutil.test())
