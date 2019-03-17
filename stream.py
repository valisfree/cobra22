from word_time import *
from processing import *
from communication import *
import sys
import os

def stream(work_stream, books, book, cur, base_time):
    """
    Запускает вывод на экран.
    """
    os.system('clear')
    flag = True
    while flag:
        for i in range(cur,len(work_stream)):
            sys.stdout.write("\r  %s            \r" % work_stream[i])
            sys.stdout.flush()
            stream_time_pause(work_stream[i], base_time)
            if stopEnter():
                press_any_key()
                wait = wait_for_the_start()
                if wait == '':
                    os.system('clear')
                    continue
                else:
                    return i
