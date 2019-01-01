#!/usr/bin/env python3

import csv
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

    def add_service(self, info = { 
            'SSH_USER': 'sshuser',
            'SSH_PASSWORD': 'Password1', 
            'SSH_CLIENT_PORT': 10022, 
            'SERVER_NAME': 'ssh-serverX',
            'CONTAINER_NAME': 'circleX',
            'NETWORK_NAME': 'ssh-networkX',
            'HOST_VOLUME_PATH': './www-data' 
        }):

        self.networks.append( info['NETWORK_NAME'] )

        # build container-info
        self.compose['services'][ info['SERVER_NAME'] ] = {
            'container_name': info['CONTAINER_NAME'],
            'hostname': info['CONTAINER_NAME'],
            'build': 'ssh-server/',
            'restart': 'always',
            'environment': {
                'SSH_USER': info['SSH_USER'],
                'SSH_PASSWORD': info['SSH_PASSWORD'],
                'SSH_PORT': info['SSH_LISTEN_PORT'],
                'SYSLOG_SERVER': self.SYSLOG_CONTAINER,
            },
            'volumes': [ info['HOST_VOLUME_PATH'] + ':/www-data/public_html'],
            'depends_on': [self.SYSLOG_CONTAINER],
            'ports': [ '{SSH_LISTEN_PORT}:{SSH_LISTEN_PORT}'.format(**info) ],
            'cpu_shares': 10,
            'mem_limit': '20m',
            'memswap_limit': '40m',
            'sysctls': {
                'net.core.somaxconn': 128,
                # 'net.ipv4.tcp_syncookies': 0,
            },
            'ulimits': {
                'nproc': 512,
                'nofile': {
                    'soft': 2048,
                    'hard': 2048,
                }
            },
            'networks': [ info['NETWORK_NAME'] ]
        }

    def build(self):
        # remove duplicated networks
        self.networks = list(set(self.networks))

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

    @classmethod
    def csv_dump(cls, csv_file = 'container-credentials.csv'):
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)

            labels = []
            values = []
            for row in reader:
                if reader.line_num == 1:
                    labels = row
                    continue

                line = {labels[i]: row[i] for i in range(len(row))}
                values.append(line)
            
            return values

