# ssh-rental-space

Docker作るレンタルスペースサービス

## 概要

- [x] sftp/scpでのファイルアップロード環境をユーザごとに提供
- [x] 認証情報(SSHホスト, SSHポート, SSHパスワード)はユーザごとに異なる
- [x] syslogコンテナによりSSHDのログを一括管理
- [ ] VolumeマウントでWebサーバのドキュメントルートをコンテナの特定パスに割当
- [ ] コンテナ同士の通信制限
- [ ] コンテナのリソース(RAM, CPU)を制限

イメージ: 

<img src="https://i.imgur.com/I83bTc8.png" width="400">
