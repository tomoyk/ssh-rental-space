# ssh/sftp container

This image provide SSH/SFTP container.

## Usage

1. Build image
```
bash ./_build.sh
```

2. Run image
```
bash ./_run.sh
```

## Optional Variables

These variables can be defined before running.

- `SSH_PORT` : SSH Server listened port (tcp) 
  - Default: `22/tcp`
- `SSH_USER` : SSH User to connect
  - Default: `guest22`
- `SSH_USER_UID` : SSH User's uid
  - Default: `2000`
- `SSH_PASSWORD` : SSH Password to connect
  - Default: `L1nuxCLU8`
- `MAX_SESSION` : SSH Maximum session
  - Default: `3`
- `PERMIT_ROOT_LOGIN` : Allow to connecting by root account
  - Default: `no``
- `SYSLOG\_SERVER` : Log server address to send ssh-log
  - Default: `172.17.0.2`
- `SYSLOG\_PORT` : Log server listend udp port
  - Default: `514/udp`

