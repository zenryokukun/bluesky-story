"""mainモジュール
物語をbluesky apiの投稿する
"""

import json
from pathlib import Path
from bluesky import post_text

# 最後のstoryN.jsonファイルのN
MAX_FILE = 6

# 物語の現在位置
STORY_POS_FILE = Path() / "current.json"

# 現在位置を取得
with open(STORY_POS_FILE,"r") as f:
    current_pos = json.load(f)

file_id = current_pos["file_id"]
story_id = current_pos["story_id"]

# 物語ファイルを取得
story_file = Path() / "story" / f"story{file_id}.json"

# 物語ファイルを読み取り、現在位置に応じた物語をstory_txtに設定
with open(story_file,"r",encoding="utf-8") as f:
    stories = json.load(f)
    story_txt = ""
    for story in stories:
        if story_id == story["id"]:
            story_txt = story["msg"]

# ファイル内の最期の物語か？
is_last = story_id == len(stories)

# blueskyに投稿するメッセージ
msg = f"電子鉱夫全力君伝【地獄編】 第{file_id}章{story_id}話\n\n"
msg += story_txt
post_text(msg)


# 物語の現在位置を、次の物語位置に更新
with open(STORY_POS_FILE,"w") as f:
    if is_last:
        # ファイルの最後の話なら、次のファイルに移る。
        # 既に最後のファイルの場合、最初のファイルに戻る。
        # storyは最初に戻す
        file_id = 1 if file_id + 1 > MAX_FILE else file_id + 1
        story_id = 1
    else:
        # ファイルの最後の話でない場合、次の物語に移る
        story_id += 1
    
    # 現在位置を次の投稿用に更新
    json.dump({
        "file_id": file_id,
        "story_id": story_id,
    },f)


