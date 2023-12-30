# stopwatch[![test](https://github.com/ryotarokarikomi/stopwatch/actions/workflows/test.yml/badge.svg)](https://github.com/ryotarokarikomi/stopwatch/actions/workflows/test.yml)
***ロボットシステム学(課題2)***  
ROS 2のサンプルコードです。  
[time_msgs](https://github.com/ryotarokarikomi/time_msgs.git)でこのパッケージで使用する型を設定しています。  
ストップウォッチです。


# 使い方
## ros2 run
* 端末1  
  以下のコマンドでlistenerを実行し、ストップウォッチを待機状態にします。
  ```
  $ ros2 run stopwatch listener
  (何も表示されません) 
  ```
* 端末2  
  別の端末で以下のコマンドでtalkerを実行し、ストップウォッチを開始します。
  ```
  $ ros2 run stopwatch talker
  (何も表示されません) 
  ```
* 実行結果
  listenerを実行した端末にタイムが表示されます。
  ```
  端末1: $ ros2 run stopwatch listener
  [INFO] [1703777637.558325501] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=1, sec=1)
  [INFO] [1703777638.552275732] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=2, sec=2)
  [INFO] [1703777639.551959578] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=3, sec=3)
  [INFO] [1703777640.551337000] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=4, sec=4)
  [INFO] [1703777641.552207370] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=5, sec=5)
  [INFO] [1703777642.551613274] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=6, sec=6)
  [INFO] [1703777643.552373554] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=7, sec=7)
  [INFO] [1703777644.551553361] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=8, sec=8)
  [INFO] [1703777645.552878640] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=9, sec=9)
  [INFO] [1703777646.552502583] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=10, sec=10)
  ・
  ・
  ・
  ```
## ros2 launch
* 端末1  
  以下のコマンドで実行し、ストップウォッチを開始します。
  ```
  $ ros2 launch stopwatch stopwatch.lauch.py
  ```
* 実行結果
  ```
  端末1: $ ros2 launch stopwatch stopwatch.lauch.py
  [INFO] [launch]: All log files can be found below /home/ryotarokarikomi/.ros/log/2023-12-29-00-36-39-159630-LAPTOP-KDT91KQF-6260
  [INFO] [launch]: Default logging verbosity is set to INFO
  [INFO] [talker-1]: process started with pid [6261]
  [INFO] [listener-2]: process started with pid [6263]
  [listener-2] [INFO] [1703777800.554534707] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=1, sec=1)
  [listener-2] [INFO] [1703777801.537734989] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=2, sec=2)
  [listener-2] [INFO] [1703777802.536468180] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=3, sec=3)
  [listener-2] [INFO] [1703777803.537790245] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=4, sec=4)
  [listener-2] [INFO] [1703777804.537599941] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=5, sec=5)
  [listener-2] [INFO] [1703777805.537884118] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=6, sec=6)
  [listener-2] [INFO] [1703777806.538848149] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=7, sec=7)
  [listener-2] [INFO] [1703777807.539539262] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=8, sec=8)
  [listener-2] [INFO] [1703777808.538801828] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=9, sec=9)
  [listener-2] [INFO] [1703777809.539169773] [listener]: time_msgs.msg.Time(hour=0, minute=0, second=10, sec=10)
  ・
  ・
  ・
  ```

# ノード
## talker.py
* メッセージの型を符号なし64ビット整数、トピックを`/time`としてパブリッシャを定義
* 1秒ごとにトピックを通じてメッセージを送信
## listener.py
* メッセージの型を符号なし64ビット整数、トピックを`/time`としてサブスクライバを定義
* トピックを通じてメッセージを受信

## 必要なソフトウェア
* Python
  * テスト済み: 3.7 ~ 3.10

## テスト環境
* Ubuntu(22.04.3 LTS)
* ROS 2 foxy


## 著作権
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージの`test/test.bash`の一部のコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを一部加筆し、本人の許可を得て自身の著作としたものです。
  * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2023 Ryotaro Karikomi
