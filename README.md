# birthday
***ロボットシステム学(課題2)***  
ROS 2のサンプルコードです。  
[birthday_msgs](https://github.com/ryotarokarikomi/birthday_msgs.git)でこのパッケージで使用する型を設定しています。  
`mypkg/talker.py`に記述されている誕生時刻から、現在の誕生時刻を求めます。


## mypkg

### talker.py
* `from birthday_msgs.msg import Birthday` #Birthday型のメッセージを使用


## ビルドテスト [![build-test](https://github.com/ryotarokarikomi/birthday/actions/workflows/test.yaml/badge.svg)](https://github.com/ryotarokarikomi/birthday/actions/workflows/test.yaml)

### テスト環境
* Ubuntu(22.04.3 LTS)


## 著作権
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* © 2023 Ryotaro Karikomi
