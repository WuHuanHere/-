import time

# 定义常量
WORK_TIME = 25 * 60   # 工作时间为25分钟
BREAK_TIME = 5 * 60   # 休息时间为5分钟

# 定义计时器函数
def countdown(t):
    while t:
        mins, secs = divmod(t, 60) # 最多60秒计算一次，divmod() 返回商和余数
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")    # \r 回车符，光标返回行首
        time.sleep(1)
        t -= 1

# 定义主函数
def pomodoro():
    print("开始工作！")
    countdown(WORK_TIME)
    print("休息一下～")
    countdown(BREAK_TIME)
    print("回到工作状态！")
    countdown(WORK_TIME)
    print("休息一下～")
    countdown(BREAK_TIME)

# 运行程序
pomodoro()
