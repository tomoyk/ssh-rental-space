# ssh-rental-space

## About

Container based SSH/SFTP rental space

## Requirement

- Python: 3
  - package: `pyyaml`
- Docker: 17.06 or later
- Docker-Compose: file format `v2.4` supported

## Usage

1. Edit container's credential on `container-credentials.csv`

Example) `$ vim container-credentials.csv`

```
SSH_USER,SSH_PASSWORD,SSH_LISTEN_PORT,SERVER_NAME,CONTAINER_NAME,NETWORK_NAME,HOST_VOLUME_PATH
sshuser1,sshpass1,32201,ssh-server1,circle1,ssh-network1,/var/www/circle1
sshuser2,sshpass2,32202,ssh-server2,circle2,ssh-network2,/var/www/circle2
```

**Note)** You should not use space on csv-file.

2. Build `docker-compose.yml` by use of `main.py`

```
$ python3 main.py
```

On error, You would like to install `pyyaml` packaege.
```
ModuleNotFoundError: No module named 'yaml'
```

3. Upstart containers by generated docker-compose

```
$ docker-compose up -d
```

<!--

## 概要

- [x] sftp/scpでのファイルアップロード環境をユーザごとに提供
- [x] 認証情報(SSHホスト, SSHポート, SSHパスワード)はユーザごとに異なる
- [x] syslogコンテナによりSSHDのログを一括管理
- [x] VolumeマウントでWebサーバのドキュメントルートをコンテナの特定パスに割当
- [x] コンテナ同士の通信制限
- [x] コンテナのリソース(RAM, CPU)を制限

-->

## Architecture

Some containers is isolated by using docker's custom network. This system is used docker's function of CPU/RAM/STORAGE limitation. 

<!-- img src="https://i.imgur.com/SB96roH.png" width="400" -->

<img src="https://raw.githubusercontent.com/tomoyk/ssh-rental-space/master/architecture.png" width="700">
