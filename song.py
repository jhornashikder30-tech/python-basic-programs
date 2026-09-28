import time
import sys
import os

# Colors
PINK = "\033[95m"
BLUE = "\033[94m"
RESET = "\033[0m"

def clear_screen():
    os.system("cls")

def typing_effect(text, color, speed=0.09):
    sys.stdout.write(color)

    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)

    sys.stdout.write(RESET + "\n")


def lyric_animation(text, color):
    # ♪ animation
    for symbol in ["♪", "♫", "♪"]:
        sys.stdout.write("\r" + color + symbol + RESET + " ")
        sys.stdout.flush()
        time.sleep(0.3)

    sys.stdout.write("\r   \r")
    sys.stdout.flush()

    # Lyric
    typing_effect(text, color)

    time.sleep(1)


clear_screen()

lyric_animation("Kabhi Toh😘", PINK)
lyric_animation("Pass Mere Aao💕", PINK)
lyric_animation("Kabhi Toh", PINK)

lyric_animation("Nazre Mujse Milao💖", BLUE)
lyric_animation("Kabhi Toh", BLUE)
lyric_animation("Dilse Dil Milao👌", BLUE)
lyric_animation("O Janna😩", BLUE)

print("\n" + PINK + "♪ ♫ ♪" + RESET)