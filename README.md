# discord-promo-gen
わるいこのためのNitro生成マシン<br>
使い方は自分で考えろ

## 2024年3月ごろに変わったこと
唐突にAPIのドメインが変わり、v2に変わって、今までのスクリプトが対策された<br>
変更点は、今までの謎のUUIDからGXのアカウントのトークンらしきものをAuthorizationヘッダーに入れるように求められるようになったって感じ<br>
GXの垢を作ってそれでトークンを取得すればおけ

## cookies.txtの取り方
流石にアカウントを作るのを自動化するのはだるいから、手動でCookie取ってくれ<br>
Operaアカウントを作ってログインした状態で https://api.gx.me/ にアクセスして、<br>
拡張機能の"Get cookies.txt LOCALLY"とかでcookies.txtをexportして、cookies.txtって名前でおいてくれ<br>

## なぜCookieなのか
トークンはなんか定期的に変わるっぽいので、Cookieの方が現実的だと思う