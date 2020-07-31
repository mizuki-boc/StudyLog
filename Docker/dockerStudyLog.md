## Docker 入門

## 7/3
- ```docker run --name some-nginx -d -p 8080:80 nginx``` で nginx サーバ起動
- ```docker ps -a``` で全てのプロセスを確認
- ```docker ps``` で起動中のプロセスのみ確認
- ```docker kill CONTAINER ID``` でコンテナ ID に該当するプロセスを kill