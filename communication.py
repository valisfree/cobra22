import sys
import select

def stopEnter():
    '''
    При вызове если нажат ентер, то возвращает истину.
    '''
    i,o,e = select.select([sys.stdin],[],[],0.001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            print(input)
            return True
    return False
def data_input():
    """
    Считывает данные с клавиатуры. Возвращает список из трех значений.
    """
    print("The file must be in the directory with the program.")
    book_input = input("Filename (Fileformat .txt, for example  file.txt): ")
    cur_input = input("Bookmark (Enter 0 if you haven't read the book): ").split()
    cur_input = int(cur_input[0])
    speed_input = input("Speed of reading (Enter 300 for reading with a speed 300 words\sec): ").split()
    speed_input = int(speed_input[0])
    return (book_input, cur_input, speed_input)
def no_file_or_not_txt():
    print("File does not exist or not txt. Try again please.")
def introductory_text():
    i = input("After start press enter to stop.")
    return i
def press_any_key():
    print("To save the label and exit write any word and press enter.")
    print("If you just press enter, then reading will resume.")
def wait_for_the_start():
    """
    Ожидает нажатия enter. Передает введено ли хоть что-то либо пустую строку.
    """
    i = input()
    return i
def data_saved():
    print("The data saved. Exit program.")
    return
