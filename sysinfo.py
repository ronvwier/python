import sys

print('sys.platform:',sys.platform)        # win32 / esp32 / linux
print('sys.implementation:',sys.implementation)  # name=micropython / cpython 
print('sys.path:',sys.path)
print('sys.version:',sys.version)

if sys.platform == "esp32":
    import machine
    print('machine.unique_id:',machine.unique_id())
else:
    import platform
    print('platform.node:',platform.node())     # toshiba-ron
    print('platform.system:',platform.system())   # Windows / Linux 