#!/usr/bin/env python3

import sys
import yaml

def main(args):
    # check parameter 
    if len(args) != 1:
        print("Error:\t you have to set one parameter")
        print("Usage:\t ./gen-compose.py [template-yaml-file]")
        return

    TEMPLATE_YAML_FILE = args[0]
    with open(TEMPLATE_YAML_FILE, 'r') as f:
        compose = yaml.load(f)
    
    # check version of compose
    if not(2.0 <= float(compose['version']) < 3.0):
        print('Error:\t Currently supported docker-compose version is 2.x')
        return
    
    SSH_USER = 'sshuser'
    SSH_PASSWORD = 'Password1'
    SSH_LISTEN_PORT = 10022
    CONTAINER_NAME = 'circleX'
    NETWORK_NAME = 'ssh-networkX'
    HOST_VOLUME_PATH = './www-data'
    SYSLOG_CONTAINER = 'syslog-server'

    compose['services']['ssh-serverX'] = {
        'container_name': CONTAINER_NAME,
        'hostname': CONTAINER_NAME,
        'build': 'ssh-server/',
        'restart': 'always',
        'environment': {
            'SSH_USER': SSH_USER,
            'SSH_PASSWORD': SSH_PASSWORD,
            'SSH_PORT': SSH_LISTEN_PORT,
            'SYSLOG_SERVER': SYSLOG_CONTAINER,
        },
        'volumes': [HOST_VOLUME_PATH + ':/www-data/public_html'],
        'depends_on': SYSLOG_CONTAINER,
        'ports': [str(SSH_LISTEN_PORT) + ':' + str(SSH_LISTEN_PORT)],
        'cpu_shares': 10,
        'mem_limit': '20m',
        'memswap_liit': '40m',
        'sysctls': {
            'net.core.somaxconn': 128,
            'net.ipv4.tcp_syncookies': 0,
        },
        'ulimits': {
            'nproc': 512,
            'nofile': {
                'soft': 2048,
                'hard': 2048,
            }
        },
        'networks': [NETWORK_NAME]
    }

    # create network
    compose['networks'] = {NETWORK_NAME: None}
    compose['services'][SYSLOG_CONTAINER]['networks'] = [NETWORK_NAME]
    
    # print(compose)
    with open('docker-compose.yml', 'w') as f:
        f.write(yaml.dump(compose, default_flow_style=False))


if __name__ == '__main__':
    main(sys.argv[1:])
    # main(['hello', 1, 'world', 2])

