# robosys2023_ros2
***ロボットシステム学(課題2)***  
ROS 2のサンプルコードです。  
`birthday/mypkg/talker.py`に記述されている誕生時刻から、現在の誕生時刻を求めます。

## 使用方法
### インストール
```
$ mkdir -p ~/ros2_ws/src
$ cd ~/ros2_ws/src
$ git clone https://github.com/ryotarokarikomi/robosys2023_ros2.git
```

### ビルド
```
$ cd ~/ros2_ws
$ colcon build
$ source ~/ros2_ws/install/setup.bash
```

### 実行
```
$ ros2 launch mypkg birthday.launch.py
```

## ビルドテスト [![build-test](https://github.com/ryotarokarikomi/robosys2023_ros2/actions/workflows/test.yaml/badge.svg)](https://github.com/ryotarokarikomi/robosys2023_ros2/actions/workflows/test.yaml)
### テスト環境
* Ubuntu(22.04.3 LTS)

## 著作権
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* © 2023 Ryotaro Karikomi
