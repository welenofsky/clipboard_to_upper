import pyperclip

clipboard_contents = pyperclip.paste()

if len(clipboard_contents):
    pyperclip.copy(clipboard_contents.upper())
