import colorama

if __name__ == '__main__':
    colorama.init(autoreset=True)
    print(colorama.Fore.RED + 'Texto em vermelho')
    print(colorama.Fore.BLUE + 'Texto em azul')
    print(colorama.Fore.GREEN + 'Texto em verde')
