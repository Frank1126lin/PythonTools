import os
import argparse

# 获取需要杀死的进程名
parser = argparse.ArgumentParser(description='kill process by names')
parser.add_argument('names', type=str, nargs='+', help='process names')
args = parser.parse_args()

# 遍历所有的进程，找到包含进程名的进程并杀死
for arg in args.names:
    print(f"kill process by name: {arg}")
    os.system(f"ps -ef | grep {arg} | grep -v grep | grep -v {os.getpid()} | awk '{{print $2 }}' | xargs kill -9")
    print("done")
