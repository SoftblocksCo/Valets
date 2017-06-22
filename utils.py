from sys import stdout

def write_same_line(text):
    stdout.write('\r' + text)
    stdout.flush()
