import pyautogui, time, os

"""Inicie el programa y espere 5 segundos, durante esos 5
segundos debe colocar el cursor y hacer clik sobre la casilla
del pin y los pines comenzaran a ingresarse """

os.system('clear')
banner = """
 ██░ ██  ▄▄▄      ▄████▄   ██ ▄█▀                    
▓██░ ██▒▒████▄   ▒██▀ ▀█   ██▄█▒                     
▒██▀▀██░▒██  ▀█▄ ▒▓█    ▄ ▓███▄░                     
░▓█ ░██ ░██▄▄▄▄██▒▓▓▄ ▄██▒▓██ █▄                     
░▓█▒░██▓ ▓█   ▓██▒ ▓███▀ ░▒██▒ █▄                    
 ▒ ░░▒░▒ ▒▒   ▓▒█░ ░▒ ▒  ░▒ ▒▒ ▓▒                    
 ▒ ░▒░ ░  ▒   ▒▒ ░ ░  ▒   ░ ░▒ ▒░                    
 ░  ░░ ░  ░   ▒  ░        ░ ░░ ░                     
 ░  ░  ░      ░  ░ ░      ░  ░                       
 ███▄    █▓█████▄▄▄█████▓  █████▒██▓     ██▓▒██   ██▒
 ██ ▀█   █▓█   ▀▓  ██▒ ▓▒▓██   ▒▓██▒    ▓██▒▒▒ █ █ ▒░
▓██  ▀█ ██▒███  ▒ ▓██░ ▒░▒████ ░▒██░    ▒██▒░░  █   ░
▓██▒  ▐▌██▒▓█  ▄░ ▓██▓ ░ ░▓█▒  ░▒██░    ░██░ ░ █ █ ▒ 
▒██░   ▓██░▒████▒ ▒██▒ ░ ░▒█░   ░██████▒░██░▒██▒ ▒██▒
░ ▒░   ▒ ▒░░ ▒░ ░ ▒ ░░    ▒ ░   ░ ▒░▓  ░░▓  ▒▒ ░ ░▓ ░
░ ░░   ░ ▒░░ ░  ░   ░     ░     ░ ░ ▒  ░ ▒ ░░░   ░▒ ░
   ░   ░ ░   ░    ░       ░ ░     ░ ░    ▒ ░ ░    ░  
         ░   ░  ░                   ░  ░ ░   ░    ░                                                      
"""
print(banner)
start = int(input("Comienza desde: "))
end = int(input("Termina en: "))
end += 1
os.system('clear')

banner = """
⣿⣿⣷⡁⢆⠈⠕⢕⢂⢕⢂⢕⢂⢔⢂⢕⢄⠂⣂⠂⠆⢂⢕⢂⢕⢂⢕⢂⢕⢂
⣿⣿⣿⡷⠊⡢⡹⣦⡑⢂⢕⢂⢕⢂⢕⢂⠕⠔⠌⠝⠛⠶⠶⢶⣦⣄⢂⢕⢂⢕
⣿⣿⠏⣠⣾⣦⡐⢌⢿⣷⣦⣅⡑⠕⠡⠐⢿⠿⣛⠟⠛⠛⠛⠛⠡⢷⡈⢂⢕⢂
⠟⣡⣾⣿⣿⣿⣿⣦⣑⠝⢿⣿⣿⣿⣿⣿⡵⢁⣤⣶⣶⣿⢿⢿⢿⡟⢻⣤⢑⢂
⣾⣿⣿⡿⢟⣛⣻⣿⣿⣿⣦⣬⣙⣻⣿⣿⣷⣿⣿⢟⢝⢕⢕⢕⢕⢽⣿⣿⣷⣔
⣿⣿⠵⠚⠉⢀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⢕⢕⢕⢕⢕⢕⣽⣿⣿⣿⣿
⢷⣂⣠⣴⣾⡿⡿⡻⡻⣿⣿⣴⣿⣿⣿⣿⣿⣿⣷⣵⣵⣵⣷⣿⣿⣿⣿⣿⣿⡿
⢌⠻⣿⡿⡫⡪⡪⡪⡪⣺⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠣⡁⠹⡪⡪⡪⡪⣪⣾⣿⣿⣿⣿⠋⠐⢉⢍⢄⢌⠻⣿⣿⣿⣿⣿⣿⣿⣿⠏⠈
⡣⡘⢄⠙⣾⣾⣾⣿⣿⣿⣿⣿⣿⡀⢐⢕⢕⢕⢕⢕⡘⣿⣿⣿⣿⣿⣿⠏⠠⠈
⠌⢊⢂⢣⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢐⢕⢕⢕⢕⢕⢅⣿⣿⣿⣿⡿⢋⢜⠠⠈
⠄⠁⠕⢝⡢⠈⠻⣿⣿⣿⣿⣿⣿⣿⣷⣕⣑⣑⣑⣵⣿⣿⣿⡿⢋⢔⢕⣿⠠⠈
⠨⡂⡀⢑⢕⡅⠂⠄⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⢔⢕⢕⣿⣿⠠⠈
⠄⠪⣂⠁⢕⠆⠄⠂⠄⠁⡀⠂⡀⠄⢈⠉⢍⢛⢛⢛⢋⢔⢕⢕⢕⣽⣿⣿⠠⠈
"""
print(banner)
t = 5
while t:
    min, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(min, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

os.system('clear')
for number in range(start, end, 1):
    letra = '{0:04}'.format(number)
    print(f"Pin: {letra}")
    
    for i in str(letra):
        time.sleep(0.08)
        pyautogui.typewrite(str(i))
