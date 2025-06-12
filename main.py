import requests
from bs4 import BeautifulSoup
import re
import os
import time

def main():
    # banner
    print(fr"""
 ______ _ _   _                     _           
|  ____(_) | | |                   | |          
| |__   _| |_| |     ___   __ _  __| | ___ _ __ 
|  __| | | __| |    / _ \ / _` |/ _` |/ _ \ '__|
| |    | | |_| |___| (_) | (_| | (_| |  __/ |   
|_|    |_|\__|______\___/ \__,_|\__,_|\___|_|    
===============================================================
FitLoader (Fitgirl Downloader)aplikasi untuk membuat link
direct download IDM untuk website Download Game FITGIRL
(Menggunakan Mirror Download)

Author  : Husni
Version : 1.0
---------------------------------------------------------------""")
    print(' Daftar File TXT Di Directory Ini: '.center(63,'-'))
    list_files = os.listdir()
    for file in list_files:
        if file.endswith('.txt'):
            print(f'-->> {file}')
    print('-'.center(63,'-'))
    
    while True:
        
        try:
            file_name: str = input('Masukkan Nama File Berisi Link [enter to default: game_url.txt]: ') or 'game_url.txt'
            if not os.path.exists(file_name):
                raise FileNotFoundError
                
        except FileNotFoundError:
            print(f'Nama File \'{file_name}\' Tidak Ditemukan, Masukkan nama file dan Pastikan extensi file adalah \'txt\'')
            
        except KeyboardInterrupt:
            print('\nKeyboard Interrupt Terdeteksi...')
            time.sleep(1)
            print('Sedang Keluar Aplikasi...')
            time.sleep(2)
            break
            
        else:
            print(f'File \'{file_name}\' Ditemukan, Lanjut Memproses...')
            time.sleep(2)
            print(' on process '.center(63,'-'))
            # Clean Link
            clean_link = []
            with open(file_name, 'r') as raw_file:
                raws_reader = raw_file.read().splitlines()
                for raw_reader in raws_reader:
                    if raw_reader.startswith('-'):
                        replace_url = raw_reader.replace('- ','')
                        clean_link.append(replace_url)

            # search direct link / hidden link
            direct_url = []
            # for urls in range(len(clean_link)):
            for index, urls in enumerate(range(len(clean_link)), 1):
                clean_url = clean_link[urls]
                response = requests.get(clean_url)
                soup = BeautifulSoup(response.content, 'html.parser')
                real_link = soup.find('script', string=re.compile('window.open'))
                if real_link:
                    found_link_tag = re.search(r'window\.open\("([^"]+)"\)', real_link.string)
                    found_link = found_link_tag.group(1)
                    print(f'{index}/{len(clean_link)}. {found_link}')
                    direct_url.append(found_link)
                    
                else:
                    print('no link found')

            # create direct link file
            with open('direct_link.txt', 'w') as direct_file:
                for direct_link in range(len(direct_url)):
                    direct_file.write(direct_url[direct_link]+'\n')
                    
            print(' Selesai '.center(63,'-'))
            time.sleep(1)
            print('Link Tersimpan di file \'direct_link.txt\', silahkan di cek.')
            time.sleep(2)
            print('Gunakan Link Yang Jadi, dan Download Menggunakan BATCH DOWNLOAD IDM')
            time.sleep(2)
            print('Sedang Menghentikan Aplikasi...')
            time.sleep(5)
            break

if __name__ == '__main__':
    main()
