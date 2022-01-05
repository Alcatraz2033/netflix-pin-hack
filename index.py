import pyautogui, time, os, argparse, signal


"""Inicie el programa y espere 5 segundos, durante esos 5
segundos debe colocar el cursor y hacer clik sobre la casilla
del pin y los pines comenzaran a ingresarse """

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

parse = argparse.ArgumentParser()
parse.add_argument('-s', '--start', help="Numero a empezar")
parse.add_argument('-e', '--end', help="Numero a terminar")
parse = parse.parse_args()

if parse.start and parse.end:
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
    CREATED BY: Alcatraz and Sergio Rivera
    """
    print(banner)
    time.sleep(3)
    os.system('clear')

    start = int(parse.start)
    end = int(parse.end)
    end += 1

    def salir(signo, frame):
        print(RED + "\n\n[!]Saliendo...\n")
        exit(1)
    signal.signal(signal.SIGINT, salir)


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
        print(MAGENTA + "Pin: " + CYAN + letra)
        
        for i in str(letra):
            time.sleep(0.08)
            pyautogui.typewrite(str(i))
else: 
    print(RED + "\nNo ha ingrsado los parametros del rango de numeros")
    