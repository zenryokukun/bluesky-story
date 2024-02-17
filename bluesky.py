"""bluesky api wrapper
bluseskyのAPI実行用モジュール

blueskyのドキュメント：https://www.docs.bsky.app/docs/get-started

公開する関数：
  post_text(str)
  post_img(str,str,str)

認証情報:
投稿するアカウント情報はcred.jsonに格納。
cred.jsonは{"identifier":str,"pwd":str}。
  identifier: アカウント
  pwd: アカウントのパスワード
"""

from atproto import Client

import json

with open("./cred.json","r") as f:
    cred = json.load(f)

client = Client(base_url='https://bsky.social')
client.login(cred["identifier"], cred["pwd"])


def post_text(txt):
    """textをpostする

    Args:
        txt (str): postする文字列
    """
    post = client.send_post(txt)


def post_image(txt, img_path, alt=""):
    """画像を埋め込んでtextをpostする

    Args:
        txt (str): postする文字列
        img_path (str): 投稿する画像ファイルのパス
        alt (str, optional): 画像のalt. Defaults to "".
    """
    with open(img_path, "rb") as f:
        img_data = f.read()
        
    client.send_image(txt, img_data, alt)
