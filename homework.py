import os
shutdown = input("do you want to shut your computer down y for yes and n for no")
if shutdown == "n":
    exit()
else:
    os.system("shutdown /s /t 1")