#!/usr/bin/python
import subprocess
import sys

P, e, i, u, g, s, t, c, h = sys.argv[1:]

breakpad = subprocess.Popen(['/usr/lib/core_handler', P, f'/var/lib/minidump/{e}-{i}.md'], stdin=subprocess.PIPE)
systemd = subprocess.Popen(['/usr/lib/systemd/systemd-coredump', P, u, g, s, t, c, h], stdin=subprocess.PIPE)

while True:
    buffer = sys.stdin.buffer.read(4096)
    if not buffer:
        break
    try:
        breakpad.stdin.write(buffer)
    except:
        pass
    try:
        systemd.stdin.write(buffer)
    except:
        pass

breakpad.stdin.close()
try:
    breakpad.wait(5)
except:
    pass

systemd.stdin.close()
try:
    systemd.wait(5)
except:
    pass
