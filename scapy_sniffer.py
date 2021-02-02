from scapy.all import *

##------------------------------------------------
## @author Isac Canedo
##------------------------------------------------

def imprime_pacote(pacote):
    header = str(pacote[TCP].payload)[0:4]
    if header == 'POST':
        if 'pass' in str(pacote[TCP].payload).lower():
            print pacote[TCP].payload


sniff(filter='port 80', store=0, prn=imprime_pacote)
