import os 

fd = os.popen("adb shell getprop ro.product.model")
print(fd.read())