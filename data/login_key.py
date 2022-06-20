
import requests, time, os, re

from urllib.error import URLError
from rich import print as prints
from rich.panel import Panel

from data import logo as asy
from platform import platform

M = '\x1b[1;91m' # MERAH
N = '\x1b[0m'    # MATI
H = '\x1b[1;92m' # HIJAU

class Log_key:

    def __init__(self, url):
        asy.Logo().log();print("");prints(Panel("""        👋
CONTACT CHINDA TO BUY KEY: [green]+2349067338953[/]
IF YOU DONT UNDERSTAND THE TOOL JUST TYPE [green]tutorial[/]""",title="[green]PESAN[/]"))
        key = input("  [*] Api Key : ")
        if key in[""]:
            print("");prints(Panel("😡[bold red] jangan kosong"));time.sleep(3);Log_key()
        elif key in ["tutorial", "Tutorial", "TUTORIAL"]:
            print("");prints(Panel("😋[bold cyan] anda akan di alihkan ke youtube"));os.system("xdg-open https://youtu.be/bK8-A400sJQ");Log_key()
        try:
            xxx = requests.get(url).text
            nan = re.findall('line">(.*?)<', str(xxx))
            if key in nan:
                exit(f"\n  [{H}✓{N}] your key valid!\n run again tools!\ntype: python chinda")
            else:
                exit(f"\n  [{M}×{N}] Key invalid ")
        except KeyError:
            print("");prints(Panel("😔[bold red] oppsh key anda telah mencapai batas masa aktif nya, silahkan upgrade ke premium."));exit()