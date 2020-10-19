# _*_ coding: utf-8 _*_

import requests
import urllib.parse

# DoujinHakushoをご利用いただきありがとうございます．
# 本ツールはDLsiteをクロールし，サークル・声優の出演作情報を取得，
# 図表としてレポートする機能を持ちます．
# 現在は販売中の男性向けオーディオファイルに対応しています．
# 詳細につきましては以下URLをご参照ください．
# https://github.com/birdManIkioiShota/DoujinHakusho

# ここに調べたいサークルの名前を入力する．
# 名前はDLsiteのサークル名と一致させる必要がある
# サークル不問の場合は空欄にすること
circle_name = ""

# ここに調べたい声優の名前を入力する．
# 名前はDLsiteのクリエイタータグと一致させる必要がある．
# 声優不問の場合は空欄にすること
creator_name = "砂糖しお"

print("検索条件：")
print(" サークル名　　：\"" + circle_name + "\"")
print(" 声優名　　　　：\"" + creator_name + "\"")
print(" 販売状況　　　：\"販売中\"")
print(" 対象性別　　　：\"男性向け\"")
print(" ファイル形式　：\"オーディオファイル\"")

# URLにエンコードする
circle_name_url = urllib.parse.quote(circle_name)
creator_name_url = urllib.parse.quote(creator_name)

search_url = "https://www.dlsite.com/maniax/fsr/=/language/jp/sex_category%5B0%5D/male/keyword_maker_name/" + circle_name_url + "/keyword_creater/" +  creator_name_url + "/ana_flg/off/genre_and_or/or/options_and_or/or/file_type_category%5B0%5D/audio_file/file_type_category_name%5B0%5D/%E3%82%AA%E3%83%BC%E3%83%87%E3%82%A3%E3%82%AA%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB/per_page/100/show_type/1/without_order/1/order/release_d"

print("探索開始…")
url_info = requests.get(search_url)
print("探索終了")

