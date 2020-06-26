import sys

print(sys.platform)        # win32 / esp32 / linux
print(sys.implementation)  # name=micropython / cpython 
print(sys.path)
print(sys.version)

if sys.platform == "esp32":
    import machine
    print(machine.unique_id())