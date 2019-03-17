import time

time_for_punctuation = 0.12
time_for_long_words = 0.08 # if len word > 5

def speed(speed):
    """
    Принимает скорость. Возвращает базовое время вывода одног слова.
    """
    x = 60 / speed
    y = x * 5 # препдолагаю, что 3 слова обычных, одно больше 5 букв и один знак пунктуации
    z = (3 * x) + (x + time_for_punctuation) + (x + time_for_long_words)
    a  = (z - y) / 5 # разница от среднего значения. Поправка на 2 из 5 слов
    base_time = x - a
    
    return base_time
def stream_time_pause(word, base_time):
    '''
    Создает задержку между выводом следующего слова.
    '''
    delta = word_time_lench(word) + time_punktuation(word)
    counting_time = base_time + delta
    time.sleep(counting_time)

def word_time_lench(word):
    """
    Считает длину слова. Возвращает значение прибавки к задержке
    """
    counted_time = 0
    if len(word) > 5:
        counted_time += time_for_long_words
    return counted_time
def time_punktuation(word):
    """
    Ищет знаки препинания. Возвращает значение прибавки к задержке.
    """
    counted_time = 0
    if ',' or '.' or '!' in word:
        counted_time += time_for_punctuation
    return counted_time
