# _*_ coding: utf-8 _*_

import requests
import urllib.parse
import re
import os
import time
import sys
import urllib.robotparser

# DojinHakushoをご利用いただきありがとうございます．
# 本ツールはDLsiteをクロールし，サークル・声優の出演作情報を取得，図表としてレポートする機能を持ちます．
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

# 本ツールはrobotss.txtを遵守しています!
rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://www.dlsite.com/robots.txt')
rp.read()

# 開始時刻の取得
start = time.time()

# HTMLのパース処理
count = 0 # ツール上の管理番号
def parse(htmlPath, count):
    with open(htmlPath, mode='r', encoding='utf_8') as f:
        flag = 0
        
        rjno = "-" # DLsite上での管理番号
        title = "-" # タイトル
        author = "-" # サークル
        cast = "-" # 声優
        price = "0" # 価格（非セール時）
        tag = "-" # DLsiteタグ（性癖）
        date = "-" # 発売日
        sales = "0" # 売上本数
        for line in f:
            # 404になったら脱出する
            notFoundPattern = ".*404 | DLsite.*"
            if(re.match(notFoundPattern, line)):
                return False, count
            
            # 開始タグ
            if line == '<tr class="">\n' :
                count = count + 1
                flag = 1

            # 終了タグ
            if line == '</tr>\n' and flag == 1:
                flag = 0
                
                with open(rawdataPath, mode='a', encoding='utf_8') as csv:
                    csv.write(str(count) + "," + rjno + ",\"" + title + "\",\"")
                    csv.write(author + "\",\"" + cast + "\",")
                    csv.write(price.replace(',','') + "," + sales.replace(',','') + ",\"")
                    csv.write(tag + "\"," + date + "\n")
            
                # 初期値に戻しておく
                rjno = "-"
                title = "-"
                author = "-"
                cast = "-"
                price = "0"
                tag = "-"
                date = "-"
                sales = "0"
                
            # ここから抽出処理
            if flag == 1:
                # RJの通し番号
                titlePattern = ".*product_id/(.*).html.*\">(.*)</a></dt>"
                result = re.match(titlePattern, line)
                if result:
                    rjno = result.group(1)
                    title = result.group(2)
                    
                # サークル名
                circlePattern = ".*circle/profile/.*"
                result = re.match(circlePattern, line)
                if result:
                    line = f.readline()
                    author = line.replace('</a>', '')
                    author = author.replace("\n", "")
                    
                # 声優名
                # キャストが複数人いる場合があるので
                castPattern = "class=\"\">(.*?)</a>"
                for result in re.findall(castPattern, line):
                    if(cast == "-"):
                        cast = result
                    else:
                        cast = cast + "," + result
                        
                # 価格
                pricePattern = ".*work_price\">(.*)<i>.*"
                result = re.match(pricePattern, line)
                if result:
                    price = result.group(1)
                    
                # 割引時の処理
                salePattern = ".*strike\">(.*)<i>.*"
                result = re.match(salePattern, line)
                if result:
                    price = result.group(1)
                    
                # 性癖タグの抽出
                tagLinePattern = ".*search_tag.*"
                result = re.match(tagLinePattern, line)
                if result:
                    line = f.readline()
                    tagPattern = ".*>(.*?)</a>"
                    tagEndPattern = "  </dd>"
                    while(not re.match(tagEndPattern, line)):
                        tagName = re.match(tagPattern, line)
                        
                        if tagName:
                            #print(tagName.group(1))
                            if(tag == "-"):
                                tag = tagName.group(1)
                                #print(tagName.group(1))
                            else:
                                tag = tag + "," + tagName.group(1)
                                #print(tagName.group(1))
                        #print(line)
                        line = f.readline()
                    #print("out!")
                    #for result in re.findall(tagPattern, line):
                    #    if(tag == "-"):
                    #        tag = result
                    #    else:
                    #        tag = tag + "," + result
                            
                # 発売日の抽出
                launchDatePattern = ".*sales_date\">販売日:&nbsp;(.*?)</li>.*"
                result = re.match(launchDatePattern, line)
                if result:
                    #print(line)
                    date = result.group(1)
                    date = date.replace("年", '-')
                    date = date.replace("月", '-')
                    date = date.replace("日", '')
                    
                # 販売数の抽出
                dlCountPattern = ".*dl_count.*>(.*)</span>.*"
                result = re.match(dlCountPattern, line)
                if result:
                    sales = result.group(1)
        return True, count

# 標準出力
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

# robots.txtを遵守！！！
if(not rp.can_fetch("*", search_url)):
    print("Disallow access !")
    sys.exit()

print("\n探索終了までお待ちください…\n")

# htmlの保存先
htmlPath = "data/page.html"
#生データの保存先
rawdataPath = "data/raw_data.csv"

# 最初のHTMLを取得する
with open(htmlPath, mode='w', encoding='utf_8') as f:
    f.write(requests.get(search_url).text)

i = 1 # ページ数
access_url = search_url

# 生データの生成処理
with open(rawdataPath, mode='w', encoding='utf_8') as f:
    f.write("id,RJ_No,title,circle,cast,price,sales,tag,date\n")

# DLsiteへのクロールとパース処理
while True:
    rtn, count = parse(htmlPath, count)
    # これ以上存在しなかったら第1返り値がFalseになる
    if rtn == False:
        break
    
    # アクセス過多を避けるため5秒間待機します
    # 数字の根拠はrobots.txt
    time.sleep(5)

    # 次ページのURLを生成しHTMLを取得する
    i = i + 1
    access_url = search_url + "/page/" + str(i)
    
    # robots.txtを遵守！！！
    if(not rp.can_fetch("*", search_url)):
        print("Disallow access !")
        sys.exit()
    
    with open(htmlPath, mode='w', encoding='utf_8') as f:
        f.write(requests.get(access_url).text)

print("探索終了！")
print("作品数　　：　", count, "[個]")

# ソースをGitに流すのはまずいので意図的にHTMLを削除しています
os.remove(htmlPath)

print("実行時間　：", '{:.1f}'.format(time.time()-start), "[sec]")
