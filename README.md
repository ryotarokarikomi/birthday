# birthday
***ロボットシステム学(課題2)***  
ROS 2のサンプルコードです。  
[birthday_msgs](https://github.com/ryotarokarikomi/birthday_msgs.git)でこのパッケージで使用する型を設定しています。  
生年月日とその日の時刻から現在までの経過時間を求めます。


## mypkg

### talker.py
* ```
  from birthday_msgs.msg import Birthday
  ```  
  * メッセージは[birthday_msgs](https://github.com/ryotarokarikomi/birthday_msgs.git)よりBirthday型として使用  
<br><br>
* ```
  pub = node.create_publisher(Birthday, "birthday", 10)
  ```  
  * パブリッシャをメッセージの型をBirthday、トピックをbirthdayとして定義  
  
* ```
  class birth:
    year = 2000
    month = 9
    day = 13
    hour = 0
    minute = 0
    second = 0
  ```
  * birthクラスに求めたい人の生年月日とその日の時刻を記述
  
* cb関数にてbirthクラスから経過時間を求める
  
* ```
  node.create_timer(1, cb)
  ```  
  * 1秒ごとにcb関数を呼び出し、経過時間を送信

### listener.py
* 


## ビルドテスト [![build-test](https://github.com/ryotarokarikomi/birthday/actions/workflows/test.yaml/badge.svg)](https://github.com/ryotarokarikomi/birthday/actions/workflows/test.yaml)

### テスト環境
* Ubuntu(22.04.3 LTS)


## 著作権
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* © 2023 Ryotaro Karikomi
