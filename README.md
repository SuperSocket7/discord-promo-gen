# これは何
もうわかるでしょ、もう<br>
使い方は自分で考えろ

## 2024年3月ごろに変わったこと
唐突にAPIのドメインが変わり、v2に変わって、今までのスクリプトが対策された<br>
変更点は、今までの謎のUUIDからGXのアカウントのトークンらしきものをAuthorizationヘッダーに入れるように求められるようになったって感じ<br>
GXの垢を作ってそれでトークンを取得すればおけ

## なんか変わった？(2024/03/07)
OperaGXを使った正規の方法でも403エラーが返されるようになった。<br>
また何か変更があるのかもしれない、その時になったら対応する
#### もう治ったっぽい(2024/03/09)

## プロモの生成条件が厳しくなった？
2024/03/13のこと、だいぶプロモURLの生成の条件が厳しくなった？<br>
- 生成時、メールアドレスの認証が必須に？(gx-games-email-not-verified)
- ~~1回だけしか生成できない？~~ 1アカウントで1日に1回しか生成できない(gx-games-auth-invalid)

マジで1垢1プロモともなれば、もうこのプログラムは更新しないことにする。<br>
そもそも1アカウントで大量生成できてたのがおかしいんだけどね笑<br>
アカウント作成の自動化はめんどいから誰か代わりにやって〜

#### 2024/03/17にわかったこと
- プロモが1アカウントに1回しか生成できなくなったかと思えば、1日に1回しか生成できなくなった？
普通アカウントに生成したか否かを記録するとこを、なんで日付にするんだ？訳わかんねーわ

#### 無限生成するなら？
- アカウントを大量生成して回す
- 大量生成は諦めて1日1回コツコツ生成する
- 神になって時間を変える

そしてなんなんだよOperaってやつは
![頭おかしいJSON](http://nekokawa.net/assets/%e3%82%b9%e3%82%af%e3%83%aa%e3%83%bc%e3%83%b3%e3%82%b7%e3%83%a7%e3%83%83%e3%83%88%202024-03-13%202.19.04.png)<br>
なんだよこのJSON、頭おかしいんじゃねーか、絶対Opera使ってやらねーわ

## cookies.txtの取り方
流石にアカウントを作るのを自動化するのはだるいから、手動でCookie取ってくれ<br>
Operaアカウントを作ってログインした状態で https://api.gx.me/ にアクセスして、<br>
拡張機能の"Get cookies.txt LOCALLY"とかでcookies.txtをexportして、cookies.txtって名前でおいてくれ<br>

## なぜCookieなのか
トークンはなんか定期的に変わるっぽいので、Cookieの方が現実的だと思う