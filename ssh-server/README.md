# docker-ssh-sftp

SSHとSFTPを動かすためのコンテナ

## 使い方

1. ビルドする.
```
chmod +x ./_build.sh
./_build.sh
```

2. 動かす.
```
chmod +x ./_run.sh
./_run.sh
```

## Note

1. 指定できる値

- `SSH_PORT` : SSHサーバのLISTENするポート
- `SSH_USER` : SSHに使用するユーザ
- `SSH_PASSWORD` : SSHに使用するパスワード

2. あらかじめ設定された値

Dockerfileで初期化しているため、環境変数では指定できない値

- /etc/ssh/sshd_config
  - `MaxSessions 3`
  - `PermitRootLogin no`
