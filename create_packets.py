from scapy.all import *

##------------------------------------------------
## @author Isac Canedo
##------------------------------------------------

ports = [80,8080,22,21,3306,25]
hosts = ['example1.com', 'example2.com']

pacote = IP(dst=hosts)/TCP(dport=ports, flags='S')

recebido, nao_recebido = sr(pacote, timeout=1)

for n in range(len(recebido)):
    print recebido[n][0][IP].dst, ":", recebido[n][0][TCP].dport
