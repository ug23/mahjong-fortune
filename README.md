# 麻雀占い

麻雀占いを提供するSlack App用Webアプリケーションです。

Flaskで作っています。

![ 2021-06-23 12 28 59](https://user-images.githubusercontent.com/2645151/123031043-a2c72680-d41e-11eb-8a67-7544e4232984.png)


## 使い方
※あとでDeploy to herokuボタンを置いておきます

gitとheroku CLIが必要です。

- Slack Appを作成し、OAuthトークンを払い出す
- このリポジトリをclone
- `heroku create` でアプリを作成
- `OAUTH_TOKEN`という環境変数に払い出したOAuthトークンを設定する
  - `heroku config:set OAUTH_TOKEN=xoxb-XXXXXXXXXX....`
- `git push heroku master`
- `heroku open` コマンドで開かれるページ:blowfish:が出たら成功
- 開かれたページのURLをSlack Appの **Event Subscriptions** から登録し、認証する
- botユーザを作成し、chat:write権限を与えます（このときbotを呼ぶチャンネルを聞かれるはず）
- botユーザにメンションして占い結果がかえってくればOK


## 既知の問題
- ~dynoスリープ時にメンションをもらうと占い結果を2,3回返してしまうらしい~
  - SlackのEvent Subscriptionの仕様でレスポンスに3秒以上かかったりエラーになったりした場合、複数回retryする機構がある

## Contribution
IssueでもPRでも適当にください
