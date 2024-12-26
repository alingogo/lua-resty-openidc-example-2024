# python_di_first

## 手順
#### 環境構築
```
$ pipenv install
```
#### 環境設定とサービス起動
```
export PLATFORM=onpre
pipenv run uvicorn app:app --reload
```

## テスト

#### クラウド版 -> I am S3
環境設定とサービス起動
```
export PLATFORM=cloud
pipenv run uvicorn app:app --reload
```

アクセス
```
curl http://localhost:8000
{"who":"I am Minio."}
```

#### オンプレ版 -> I am Minio
環境設定とサービス起動
```
export PLATFORM=onpre
pipenv run uvicorn app:app --reload
```

アクセス
```
curl http://localhost:8000
{"who":"I am Minio."}
```
