# Bluesky 自動投稿bot

## これは何ですか

昔Twitterで動かしていた物語投稿botを、Blueskyに移行しました。Pythonで実装されています。

サーバのスケジューラ等で登録し、一定間隔で実行します。

## 依存パッケージ

```atproto```を使っています。バージョンは**0.0.41**です。

```bash
pip install atproto
```

## ファイルについて

### ```main.py```

エントリ・ポイントです。

### ```bluesky.py```

bluesky投稿用のモジュールです。

### ```/story```フォルダ

物語のファイルが格納されています。直下に```story1.json```から```story6.json```が入っています。

### ```/story/story{n}.json```

投稿する物語のファイルです。以下の形である必要があります。

```ts
[
  {
		"id": number,   // index
		"msg": string,  // 投稿する文字列
		"img": string   // 投稿する画像ファイルのパス
  },
]
```

### ```/cred.json```

認証用ファイルです。プロジェクト直下に配置が必要です。以下の形である必要があります。

```ts
{
	"identifier":         string, // アカウント名
	"pwd":                string, // パスワード
	"app-password-name"?: string, // [任意]パスワードの遂になるname
}
```

パスワードはBlueskyアカウントの「設定」→「アプリパスワード」で生成できます。生成するとパスワードに名前をつけることができます。```app-password-name```にはその名前を設定していますが、現状未使用のためなくても問題ありません。

リンク：https://bsky.app/settings/app-passwords

### ```/current.json```

現在の物語の位置を格納しています。以下の形である必要があります。

```ts
{
	"file_id": number  // 物語ファイルの番号
	"story_id": number // 物語の位置。storyN.jsonのid
}
```

