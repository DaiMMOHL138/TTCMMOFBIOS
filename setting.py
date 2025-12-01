title = r"""
$$$$$$$\       $$$$$$$$\  $$$$$$\   $$$$$$\  $$\       
$$  __$$\      \__$$  __|$$  __$$\ $$  __$$\ $$ |      
$$ |  $$ |        $$ |   $$ /  $$ |$$ /  $$ |$$ |      
$$ |  $$ |$$$$$$\ $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$ |  $$ |\______|$$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$ |  $$ |        $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$$$$$$  |        $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\ 
\_______/         \__|    \______/  \______/ \________|
-------------------------------------------------------"""

def clear_screen():
    import os
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')
def delay(seconds):
    import time
    import colorama
    for i in range(seconds, -1, -1):
        print(f'{colorama.Fore.CYAN}Vui lòng chờ {i} giây                    ', end="\r")
        time.sleep(1)
min_delay = 10
max_delay = 20
