# _*_ coding: utf-8 _*_

import requests
import urllib.parse
import re

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
creator_name = "一之瀬りと"

# htmlの保存先
htmlPath = "data/page.html"
#生データの保存先
rawdataPath = "data/raw_data.csv"

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

# htmlはとりあえず保存しとく
with open(htmlPath, mode='w') as f:
    f.write(requests.get(search_url).text)

# パース処理
with open(htmlPath, mode='r') as f:
    flag = 0
    count = 0
    for line in f:
        # 開始タグ
        if line == '<tr class="">\n' :
            count = count + 1
            flag = 1
        # 終了タグ
        if line == '</tr>\n' :
            flag = 0
        
        if flag == 1:
            # RJの通し番号
            titlePattern = ".*product_id/(.*).html.*\">(.*)</a></dt>"
            result = re.match(titlePattern, line)
            if result:
                print("\n", count, result.group(1), result.group(2))

            # サークル名
            circlePattern = ".*circle/profile/.*"
            result = re.match(circlePattern, line)
            if result:
                line = f.readline()
                author = line.replace('</a>', '')
                author = author.replace("\n", "")
                print(author)

            # 声優名
            # キャストが複数人いる場合があるので
            castPattern = "class=\"\">(.*?)</a>"
            for result in re.finditer(castPattern, line, re.MULTILINE):
                cast = result.groups(1)[0]
                print(cast, "; " , end="")

            # 価格
            pricePattern = ".*work_price\">(.*)<i>.*"
            result = re.match(pricePattern, line)
            if result:
                print("\n", result.group(1))
            
            # 割引時の処理
            salePattern = ".*strike\">(.*)<i>.*"
            result = re.match(salePattern, line)
            if result:
                print("\n", result.group(1))

    print("作品数：", count)


# 生データの生成処理
with open(rawdataPath, mode='w') as f:
    f.write("通し番号,RJナンバー,タイトル,サークル,声優,値段,販売数,ジャンル,発売年,発売月,発売日")
print("探索終了！")

