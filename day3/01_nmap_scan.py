import nmap

def run_nmap_scan(targetIP):
    nm=nmap.PortScanner()
    nm.scan(targetIP,'22-443')
    return nm.all_hosts()

print (run_nmap_scan("10.1.60.55"))


