#!/usr/bin/env python3
# TOOL: FILE KHALED - ID MANAGER
# Green Theme - English Language - Termux/Python Ready 👹

import os
import sys
import time
import random
import re
import json
import requests
from collections import OrderedDict

# ================== اللون الأخضر ==================
GREEN = '\033[92m'
BRIGHT_GREEN = '\033[1;92m'
DARK_GREEN = '\033[38;5;22m'
WHITE = '\033[1;97m'
RED = '\033[1;91m'
YELLOW = '\033[1;93m'
CYAN = '\033[1;96m'
RESET = '\033[0m'

# ================== Basic Functions ==================
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def line():
    print(f"{GREEN}{'='*55}{RESET}")

def animation(text, delay=0.03):
    for char in text + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# ================== Logo (Same as Screenshot) ==================
def show_logo():
    clear()
    print(f"""{GREEN}
 ░▒▓██████▓▒░░▒▓███████▓▒░▒▓████████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░▒▓███████▓▒░  ░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░        ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░  
                                                                                                                         

<<?> KHALED : DJALIL GPT
<<?> FACEBOOK : N/A
<<?> KHALED : DJALIL-GPT
<1> TOOL    : FILE KHALED
<1> VERSION : 1.0
{RESET}""")
    line()

# ================== MENU ==================
def main_menu():
    while True:
        show_logo()
        
        print(f"""{GREEN}
[A] START FILE DUMP
[B] REMOVE DUPLICATE IDS
[C] REMOVE USED IDS FROM FILE
[D] SEPARATE IDS
[E] FILE MIXER
[F] DIVIDE FILE EQUALLY
[G] REMOVE STYLISH NAMES
[0] EXIT

<<?> CHOICE : {RESET}""", end='')
        
        choice = input().strip().upper()
        
        if choice == 'A':
            file_dump()
        elif choice == 'B':
            remove_duplicates()
        elif choice == 'C':
            remove_used_ids()
        elif choice == 'D':
            separate_ids()
        elif choice == 'E':
            file_mixer()
        elif choice == 'F':
            divide_file()
        elif choice == 'G':
            remove_stylish()
        elif choice == '0':
            animation(f"{BRIGHT_GREEN}[✓] Goodbye! 👹{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}[✗] Invalid Choice!{RESET}")
            time.sleep(1)

# ================== [A] START FILE DUMP ==================
def file_dump():
    show_logo()
    line()
    print(f"{GREEN}[*] START FILE DUMP - Facebook Friends Extractor{RESET}")
    line()
    
    # Check for token and cookie
    if not os.path.exists('.token.txt') or not os.path.exists('.cok.txt'):
        print(f"{YELLOW}[!] Please login first using cookie{RESET}")
        login_with_cookie()
        return
    
    token = open('.token.txt', 'r').read().strip()
    cookie = open('.cok.txt', 'r').read().strip()
    
    filename = input(f"{WHITE}[•] Enter filename (without /sdcard/): {GREEN}")
    filepath = f"/sdcard/{filename}"
    
    try:
        uid_count = int(input(f"{WHITE}[•] How many UIDs to process: {GREEN}"))
    except:
        uid_count = 1
    
    uids = []
    for i in range(uid_count):
        uid = input(f"{WHITE}[•] UID {i+1}: {GREEN}")
        uids.append(uid)
    
    try:
        limit = int(input(f"{WHITE}[•] Extract limit (0 for unlimited): {GREEN}"))
    except:
        limit = 0
    
    try:
        speed = int(input(f"{WHITE}[•] Speed (1-100, higher=faster): {GREEN}"))
        speed = max(1, min(100, speed))
    except:
        speed = 50
    
    delay = (101 - speed) / 100.0
    
    animation(f"{BRIGHT_GREEN}[✓] Starting extraction...{RESET}")
    
    all_ids = []
    extracted = 0
    
    for uid in uids:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36',
            'Content-Type': 'application/json',
        }
        
        params = {
            'access_token': token,
            'fields': 'friends.limit(5000)'
        }
        
        try:
            url = f"https://graph.facebook.com/{uid}/friends"
            response = requests.get(url, params=params, headers=headers, cookies={'cookie': cookie})
            data = response.json()
            
            if 'error' in data:
                print(f"{RED}[✗] UID {uid} is private or invalid{RESET}")
                continue
            
            friends = data.get('data', [])
            
            for friend in friends:
                if limit > 0 and extracted >= limit:
                    break
                
                friend_id = friend.get('id')
                friend_name = friend.get('name', 'Unknown')
                
                if friend_id and friend_id not in all_ids:
                    all_ids.append(friend_id)
                    with open(filepath, 'a') as f:
                        f.write(f"{friend_id}|{friend_name}\n")
                    extracted += 1
                    print(f"{GREEN}[+] {extracted}: {friend_id} | {friend_name[:30]}{RESET}")
                    
                time.sleep(delay)
                
        except Exception as e:
            print(f"{RED}[✗] Error with UID {uid}: {str(e)[:50]}{RESET}")
            continue
    
    line()
    print(f"{BRIGHT_GREEN}[✓] Extraction Complete!{RESET}")
    print(f"{WHITE}[•] Total IDs: {extracted}")
    print(f"{WHITE}[•] Saved to: {filepath}")
    line()
    input(f"{WHITE}[•] Press Enter to continue...{RESET}")

# ================== [B] REMOVE DUPLICATE IDS ==================
def remove_duplicates():
    show_logo()
    line()
    print(f"{GREEN}[*] REMOVE DUPLICATE IDS{RESET}")
    line()
    
    file_path = input(f"{WHITE}[•] File path (e.g., /sdcard/ids.txt): {GREEN}")
    
    if not os.path.exists(file_path):
        print(f"{RED}[✗] File not found!{RESET}")
        input(f"{WHITE}[•] Press Enter...{RESET}")
        return
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    unique = list(OrderedDict.fromkeys([l.strip() for l in lines if l.strip()]))
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique) + '\n')
    
    print(f"{BRIGHT_GREEN}[✓] Done!{RESET}")
    print(f"{WHITE}[•] Before: {len(lines)} | After: {len(unique)}")
    input(f"{WHITE}[•] Press Enter...{RESET}")

# ================== [C] REMOVE USED IDS FROM FILE ==================
def remove_used_ids():
    show_logo()
    line()
    print(f"{GREEN}[*] REMOVE USED IDS FROM FILE{RESET}")
    line()
    
    main_file = input(f"{WHITE}[•] Main file: {GREEN}")
    used_file = input(f"{WHITE}[•] Used IDs file: {GREEN}")
    
    if not os.path.exists(main_file) or not os.path.exists(used_file):
        print(f"{RED}[✗] One or both files not found!{RESET}")
        input(f"{WHITE}[•] Press Enter...{RESET}")
        return
    
    with open(main_file, 'r', encoding='utf-8', errors='ignore') as f:
        main_ids = set(f.read().splitlines())
    with open(used_file, 'r', encoding='utf-8', errors='ignore') as f:
        used_ids = set(f.read().splitlines())
    
    remaining = main_ids - used_ids
    
    with open(main_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(remaining) + '\n')
    
    print(f"{BRIGHT_GREEN}[✓] Remaining IDs: {len(remaining)}{RESET}")
    input(f"{WHITE}[•] Press Enter...{RESET}")

# ================== [D] SEPARATE IDS ==================
def separate_ids():
    show_logo()
    line()
    print(f"{GREEN}[*] SEPARATE IDS{RESET}")
    line()
    
    source = input(f"{WHITE}[•] Source file: {GREEN}")
    if not os.path.exists(source):
        print(f"{RED}[✗] File not found!{RESET}")
        input(f"{WHITE}[•] Press Enter...{RESET}")
        return
    
    output = input(f"{WHITE}[•] Output file: {GREEN}")
    pattern = input(f"{WHITE}[•] Pattern to search (e.g., 6155): {GREEN}")
    
    with open(source, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    matched = [l for l in lines if pattern in l]
    
    with open(output, 'w', encoding='utf-8') as f:
        f.writelines(matched)
    
    print(f"{BRIGHT_GREEN}[✓] Separated {len(matched)} lines{RESET}")
    input(f"{WHITE}[•] Press Enter...{RESET}")

# ================== [E] FILE MIXER ==================
def file_mixer():
    show_logo()
    line()
    print(f"{GREEN}[*] FILE MIXER - Shuffle IDs{RESET}")
    line()
    
    file_path = input(f"{WHITE}[•] File path: {GREEN}")
    if not os.path.exists(file_path):
        print(f"{RED}[✗] File not found!{RESET}")
        input(f"{WHITE}[•] Press Enter...{RESET}")
        return
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    random.shuffle(lines)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"{BRIGHT_GREEN}[✓] Mixed {len(lines)} lines{RESET}")
    input(f"{WHITE}[•] Press Enter...{RESET}")

# ================== [F] DIVIDE FILE EQUALLY ==================
def divide_file():
    show_logo()
    line()
    print(f"{GREEN}[*] DIVIDE FILE EQUALLY{RESET}")
    line()
    
    file_path = input(f"{WHITE}[•] Source file: {GREEN}")
    if not os.path.exists(file_path):
        print(f"{RED}[✗] File not found!{RESET}")
        return
    
    try:
        parts = int(input(f"{WHITE}[•] Number of parts: {GREEN}"))
    except:
        parts = 2
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    total = len(lines)
    size = (total + parts - 1) // parts
    
    for i in range(parts):
        start = i * size
        end = min((i + 1) * size, total)
        part_lines = lines[start:end]
        
        part_name = f"{file_path}.part{i+1}"
        with open(part_name, 'w', encoding='utf-8') as f:
            f.writelines(part_lines)
        print(f"{GREEN}[✓] Part {i+1}: {len(part_lines)} lines -> {part_name}{RESET}")
    
    input(f"{WHITE}[•] Press Enter...{RESET}")

# ================== [G] REMOVE STYLISH NAMES ==================
def remove_stylish():
    show_logo()
    line()
    print(f"{GREEN}[*] REMOVE STYLISH NAMES{RESET}")
    line()
    
    file_path = input(f"{WHITE}[•] File path: {GREEN}")
    if not os.path.exists(file_path):
        print(f"{RED}[✗] File not found!{RESET}")
        return
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    cleaned = []
    for line in lines:
        if '|' in line:
            parts = line.split('|')
            if len(parts) >= 2:
                # Keep only basic characters
                name = re.sub(r'[^\w\s]', '', parts[1])
                cleaned.append(f"{parts[0]}|{name}\n")
            else:
                cleaned.append(line)
        else:
            cleaned.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned)
    
    print(f"{BRIGHT_GREEN}[✓] Cleaned {len(lines)} lines{RESET}")
    input(f"{WHITE}[•] Press Enter...{RESET}")

# ================== Login Function ==================
def login_with_cookie():
    line()
    print(f"{YELLOW}[!] Facebook Cookie Login Required{RESET}")
    line()
    
    cookie = input(f"{WHITE}[•] Enter your Facebook cookie: {GREEN}")
    
    with open('.cok.txt', 'w') as f:
        f.write(cookie)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36',
    }
    
    try:
        response = requests.get('https://graph.facebook.com/me', headers=headers, cookies={'cookie': cookie})
        data = response.json()
        
        if 'id' in data:
            print(f"{BRIGHT_GREEN}[✓] Login successful!{RESET}")
            # Try to get token
            token = input(f"{WHITE}[•] Enter access token (if you have one, else press Enter): {GREEN}")
            if token:
                with open('.token.txt', 'w') as f:
                    f.write(token)
        else:
            print(f"{RED}[✗] Invalid cookie!{RESET}")
    except:
        print(f"{RED}[✗] Connection error!{RESET}")
    
    input(f"{WHITE}[•] Press Enter...{RESET}")

# ================== Main Entry ==================
if __name__ == "__main__":
    main_menu()
