# DojinHakusho
『DLsite』をクロールし，任意のクリエイターの情報を収集・整理するフリーソフトです． 

## DojinHakusho is 何？
図を用いて詳細な動作を説明します（と言っても動作は非常に簡素です）．

<img src="https://user-images.githubusercontent.com/44240143/96359980-823e2280-1153-11eb-930f-5d25f9db1e0e.png" width=70%>

- ユーザの操作

ユーザはエントリーポイント上の変数を用い，情報を収集したいクリエイター名を指定します．

これは文字列で指定され，DLsite上で用いられるクリエイタータグと一致する必要があります．

- ツールの動作

ツールは検索用のURLを生成し，DLsiteにアクセス，HTMLを取得します．
検索結果が複数ページにわたる場合は全作品を取得するまでクロールを繰り返します．

ツールは得られたHTMLを構文解析し，クリエイターの作品データをまとめたCSV形式の生データを生成します．
生データにはタイトル，発売日，値段，参加クリエイター，販売数，ジャンルなどの情報が含まれます．

ツールは生データを更に解析し，指定されたクリエイターに関するレポートを自動生成します．
レポートには売り上げのヒストグラムやジャンルの共起関係など，基本的な図表が含まれます．

## HOW TO USE
wiki嫁

## 利用規約
本ツールはDLsiteを利用するクリエイター様を支援することを目的に開発されたツールです．
従って，本ツールによって得られるデータを，その目的から大きく逸脱して使用することはお控えください．
（例えば，データを用いた対立煽りや中傷行為などがこれに該当します．）

また，本ツールはDLsite様にアクセスしHTMLソースを取得することで動作するクローラーです．
従って，本ツールの利用は常識の範囲内で行い，サーバ管理者から攻撃と見做されるような行為はお控えください．

上記規約に従う限り，本ツールは完全にフリーです．
リンク，商用利用，転載，改変，二次配布などは自由に行っていただいて構いませんし，連絡の必要もありません．
なお，製作者はその結果生じたいかなる事態にも責任を負いかねます．

## 動作要件
Javaが動作し，ネットワークに接続可能なPCでの利用を想定しています．

## 解析依頼
任意のクリエイターの活動を解析し，図表とその説明を記載した数ページのPDFファイルをお渡しします．

『依頼者がクリエイター本人かつSNS上でツールを宣伝いただくこと』

『製作者ブログ上で実績として解析結果を開示することへの許諾』

上記2点を条件に解析を無料でお引き受けしています．

何はともあれ，とりあえずご相談ください．

## FAQ
### ○○していい？
利用規約に従い，他人様に迷惑を掛けない限りは基本的に自由です．

### ツールこうしてああして
利用者目線のフィードバックに飢えていますので，忌憚ないご意見お待ちしております．

改良は続けていく予定ですので，ご連絡くだされば検討します．（コミットしてくれてもいいのよ？）

### 金目当て？
本ツールは完全に無償です．

製作者に金儲けの意図はありませんし，将来的にも行いません．

## SPECIAL THANKS
konkon3249様，『DLsiteとFANZAの同人音声作品を題材とした探索的データ解析』（2019-11-29）
