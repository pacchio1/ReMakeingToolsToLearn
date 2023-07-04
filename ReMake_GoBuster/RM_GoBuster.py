a = """
▄▄▄  ▄▄▄ .• ▌ ▄ ·.  ▄▄▄· ▄ •▄ ▪   ▐ ▄  ▄▄ •
▀▄ █·▀▄.▀··██ ▐███▪▐█ ▀█ █▌▄▌▪██ •█▌▐█▐█ ▀ ▪
▐▀▀▄ ▐▀▀▪▄▐█ ▌▐▌▐█·▄█▀▀█ ▐▀▀▄·▐█·▐█▐▐▌▄█ ▀█▄
▐█•█▌▐█▄▄▌██ ██▌▐█▌▐█▪ ▐▌▐█.█▌▐█▌██▐█▌▐█▄▪▐█
.▀  ▀ ▀▀▀ ▀▀  █▪▀▀▀ ▀  ▀ ·▀  ▀▀▀▀▀▀ █▪·▀▀▀▀

 ▄▄ •       ▄▄▄▄· ▄• ▄▌.▄▄ · ▄▄▄▄▄▄▄▄ .▄▄▄
▐█ ▀ ▪ ▄█▀▄ ▐█ ▀█▪█▪██▌▐█ ▀. •██  ▀▄.▀·▀▄ █·
▄█ ▀█▄▐█▌.▐▌▐█▀▀█▄█▌▐█▌▄▀▀▀█▄ ▐█.▪▐▀▀▪▄▐▀▀▄
▐█▄▪▐█▐█▌.▐▌██▄▪▐█▐█▄█▌▐█▄▪▐█ ▐█▌·▐█▄▄▌▐█•█▌
·▀▀▀▀  ▀█▄▀▪·▀▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀

"""
# https://texteditor.com/multiline-text-art/
import requests

print(a)


def scan_dir(url, wordlist):
    with open(wordlist, "r") as f:
        dirs = f.read().splitlines()

    for directory in dirs:
        dir_url = url + "/" + directory
        response = requests.get(dir_url)
        if response.status_code == 200:
            print("[+] Found directory: " + dir_url)


if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    wordlist = "Wordlist.txt"
    scan_dir(url, wordlist)
