try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

root = tk.Tk()
# keep the window from showing
root.withdraw()

# text from clipboard
clip_text = root.clipboard_get()
clip_text = clip_text.upper()

# clear the clipboard
root.clipboard_clear()

# put uppercase text into clipboard
root.clipboard_append(clip_text)