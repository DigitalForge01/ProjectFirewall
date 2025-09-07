from scapy.all import sniff
from rules_manager import load_rules
from logger import log_blocked

firewall_running = False

def match_rules(packet):
    rules = load_rules()
    
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]

        # Block IPs
        if ip_layer.src in rules['block_ips']:
            return 'BLOCKED', f'Blocked IP: {ip_layer.src}'

        # Allow ports
        if packet.haslayer("TCP"):
            tcp_layer = packet["TCP"]
            if rules['allow_ports'] and tcp_layer.dport not in rules['allow_ports']:
                return 'BLOCKED', f'Blocked Port: {tcp_layer.dport}'

        # Block Protocols (e.g., ICMP)
        if ip_layer.proto == 1 and 'ICMP' in rules['block_protocols']:
            return 'BLOCKED', 'Blocked Protocol: ICMP'

    return 'ALLOWED', ''

def packet_callback(packet):
    status, reason = match_rules(packet)
    if status == 'BLOCKED':
        log_blocked(reason, packet.summary())

def start_firewall():
    global firewall_running
    firewall_running = True
    sniff(prn=packet_callback, store=0, stop_filter=lambda x: not firewall_running)

def stop_firewall():
    global firewall_running
    firewall_running = False
