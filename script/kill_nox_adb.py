import os
import subprocess


# 结束进程的函数
def kill_process(process_name):
    # 使用tasklist命令获取进程列表
    tasks = subprocess.check_output(['tasklist', '/fi', "IMAGENAME eq %s" % process_name]).decode('utf-8')
    # 如果进程正在运行
    if process_name in tasks:
        # 使用taskkill命令结束进程
        os.system('taskkill /f /im %s' % process_name)


# 关闭nox_adb.exe进程
kill_process('nox_adb.exe')
