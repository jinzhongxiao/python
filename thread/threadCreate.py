#!/usr/bin/python
# -*- coding:UTF-8 -*-

import threading
import time


exitFlag = 0

class myThread(threading.Thread):
	"""
		Python使用两个标准库thread threading提供对线程的支持。 
			threadind.currentThread()：返回当前的线程变量
			threading.enumerate():返回一个包含正在运行的线程list，
			threading.activeCount(): 返回正运行的线程数量, == len(threading.enumerate())
		Thread提供以下类来处理线程：
			run():表示线程活动
			start() : 启动线程
			join([time]): 阻塞进程直到线程执行完毕，或者抛出未处理的异常-或者是可选的超时发生
			isAlive()：返回线程是否活动
			getName()   setName()
	"""
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):  #将执行的代码写到run函数里，线程在创建后会直接运行run函数
		print "Starting " + self.name
		print_time(self.name, self.counter, 5)
		print "Exiting " + self.name


def print_time(ThreadName, delay, counter):
	while counter:
		if exitFlag:
			thread.exit()
		time.sleep(delay)
		print "%s : %s "%(ThreadName, time.ctime(time.time()))
		counter -= 1



thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

print "Exiting Main Thread!"
