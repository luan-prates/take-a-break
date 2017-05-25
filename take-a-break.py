import time
import webbrowser

total_breaks = 3
break_cont = 0

print("this program started on " + time.ctime())
while(break_cont < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=y6Sxv-sUYtM")
    break_cont = break_cont + 1
