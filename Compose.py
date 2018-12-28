#!/usr/bin/env python3

import sys
import yaml
from collections import defaultdict

class Compose:

    def __init__(self, template_yaml_file = 'docker-compose.yml.template',
                 syslog_container = 'syslog-server'):
        self.networks = []
        self.SYSLOG_CONTAINER = syslog_container

        self.fd = open(template_yaml_file, 'r')
        self.compose = yaml.load(self.fd)
        
        # check version of compose
        if not(2.0 <= float(self.compose['version']) < 3.0):
            print('Error:\t Currently supported docker-compose version is 2.x')
            return

    def add_service(self, SSH_USER = 'sshuser', SSH_PASSWORD = 'Password1', 
                    SSH_LISTEN_PORT = 10022, SERVER_NAME = 'ssh-serverX',
                    CONTAINER_NAME = 'circleX', NETWORK_NAME = 'ssh-networkX',
                    HOST_VOLUME_PATH = './www-data'):
        self.networks.append(NETWORK_NAME)

        # build container-info
        self.compose['services'][SERVER_NAME] = {
            'container_name': CONTAINER_NAME,
            'hostname': CONTAINER_NAME,
            'build': 'ssh-server/',
            'restart': 'always',
            'environment': {
                'SSH_USER': SSH_USER,
                'SSH_PASSWORD': SSH_PASSWORD,
                'SSH_PORT': SSH_LISTEN_PORT,
                'SYSLOG_SERVER': self.SYSLOG_CONTAINER,
            },
            'volumes': [HOST_VOLUME_PATH + ':/www-data/public_html'],
            'depends_on': [self.SYSLOG_CONTAINER],
            'ports': [str(SSH_LISTEN_PORT) + ':' + str(SSH_LISTEN_PORT)],
            'cpu_shares': 10,
            'mem_limit': '20m',
            'memswap_limit': '40m',
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

    def build(self):
        # add container's network to syslog-container's network
        self.compose['services'][self.SYSLOG_CONTAINER]['networks'] = self.networks

        # add container's networks to custom network
        self.compose['networks'] = {}
        for net in self.networks:
            self.compose['networks'][net] = None

    def write(self, OUTPUT_FILE = 'docker-compose.yml'):
        with open('docker-compose.yml', 'w') as f:
            f.write(yaml.dump(self.compose, default_flow_style=False))
        self.fd.close()


def main(args):

    '''
    # check parameter 
    if len(args) != 1:
        print("Error:\t you have to set one parameter")
        print("Usage:\t ./gen-compose.py [template-yaml-file]")
        return
    '''

    comp = Compose()
    comp.add_service('user1', 'pass1', 20001, 'ssh-server1', 'circleA', 'ssh-network1', './www-data')
    comp.add_service('user3', 'pass3', 20003, 'ssh-server3', 'circleC', 'ssh-network3', './www-data')
    comp.build()
    comp.write()


if __name__ == '__main__':
    main(sys.argv[1:])

