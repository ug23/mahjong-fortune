麻雀占い
-----

麻雀占いを提供するSlack App用Webアプリケーションです。

Flaskで作っています。

# 使い方
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


# 既知の問題
- dynoスリープ時にメンションをもらうと占い結果を2,3回返してしまうらしい