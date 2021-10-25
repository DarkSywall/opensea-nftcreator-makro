# Package import
from time import sleep
import pyperclip
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

# Controller
keyboard = KeyboardController()
mouse = MouseController()
global_sleep = 0


# Functions
def wait(seconds):
    """
    wait - waits for x seconds till proceeding
    :param seconds: waiting time in seconds
    :return: -
    """
    sleep(seconds)


def press_tab(count):
    """
    press_tab - execute tab key press
    :param count: number of presses which should be executed
    :return: -
    """
    for i in range(count):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    wait(global_sleep)


def press_reverse_tab(count):
    """
    press_reverse_tab - execute shift + tab key press to go one tab / field back / up
    :param count: number of presses which should be executed
    :return: -
    """
    for i in range(count):
        keyboard.press(Key.shift)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.shift)
    wait(global_sleep)


def press_return(count):
    """
    press_return - execute return key press
    :param count: number of presses which should be executed
    :return: -
    """
    for i in range(count):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    wait(global_sleep)


def press_space(count):
    """
    press_space - execute space key press
    :param count: number of presses which should be executed
    :return: -
    """
    for i in range(count):
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    wait(global_sleep)


def press_escape(count):
    """
    press_escape - execute escape key press
    :param count: number of presses which should be executed
    :return: -
    """
    for i in range(count):
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
    wait(global_sleep)


def press_f5(count):
    """
    press_f5 - execute F5 key press for refreshing the browser
    :param count: number of presses which should be executed
    :return: -
    """
    for i in range(count):
        keyboard.press(Key.f5)
        keyboard.release(Key.f5)
    wait(global_sleep)


def click(x, y):
    """
    click - click on position X / Y
    :param x: cursor position X
    :param y: cursor position Y
    :return: -
    """
    mouse.position = (x, y)
    mouse.click(Button.left, 1)
    wait(global_sleep)


def doubleclick(x, y):
    """
    doubleclick - click on position X / Y
    :param x: cursor position X
    :param y: cursor position Y
    :return: -
    """
    click(x, y)
    click(x, y)
    wait(global_sleep)


def show_cursor_pos():
    """
    show_cursor_pos - loops cursor position in console
    :return: -
    """
    while 1 == 1:
        print("Current position: ", str(mouse.position))
        wait(global_sleep)


def paste_text(text):
    """
    paste_text - copies "text"-param into ram and paste it in selected field
    :param text: text which needs to be copied
    :return: -
    """
    wait(0.5)
    pyperclip.copy(text)
    wait(0.2)
    keyboard.press(Key.ctrl)
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release(Key.ctrl)
    wait(global_sleep)
