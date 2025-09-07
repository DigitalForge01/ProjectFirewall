import logging

LOG_FILE = 'firewall.log'

logging.basicConfig(filename=LOG_FILE,
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def log_blocked(reason, packet_summary):
    logging.info(f'{reason} | {packet_summary}')
