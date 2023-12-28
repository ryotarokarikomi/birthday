# birthday
***ロボットシステム学(課題2)***  
ROS 2のサンプルコードです。  
[birthday_msgs](https://github.com/ryotarokarikomi/birthday_msgs.git)でこのパッケージで使用する型を設定しています。  
生年月日とその日の時刻から現在までの経過時間を求めます。


## 使い方
* ```
  class birth:
    year = 2000
    month = 9
    day = 13
    hour = 0
    minute = 0
    second = 0
  ```
  `mypkg/talker.py`の`birth`クラスを任意の人物の生年月日とその日の時刻に変更してください。

* ターミナル1
  ```
  $ ros2 run mypkg talker
  ```

* ターミナル2
  ```
  $ ros2 run mypkg listener
  ```

* ターミナル2に`birth`クラスに記述した生年月日とその日の時刻から現在までの経過時間が表示されます。

## ビルドテスト [![build-test](https://github.com/ryotarokarikomi/birthday/actions/workflows/test.yaml/badge.svg)](https://github.com/ryotarokarikomi/birthday/actions/workflows/test.yaml)

### テスト環境
* Ubuntu(22.04.3 LTS)


## 著作権
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* © 2023 Ryotaro Karikomi
