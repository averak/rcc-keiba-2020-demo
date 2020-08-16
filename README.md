# デモ用軽量版レシピ

[![Twitter](https://img.shields.io/badge/Twitter-競馬AI班-blue?style=flat-square&logo=twitter)](https://twitter.com/search?q=%23rcc_keiba)

RCC 2020 年度競馬 AI 班

## 概要

競馬の 1 着のみを予測する 競馬 AI のレシピです

少量の特徴量から DNN を用いて予測する軽量な 競馬 AI を体験できます

## 実行環境

- Ubuntu 20.04
- Python ~> 3.8.0
- TensorFlow 2.2

## 軽量版 競馬 AI レシピのインストールと学習

軽量版競馬 AI レシピと，競馬データ（サブセット）を用意します

### レシピの展開

[デモ用軽量版競馬 AI レシピ](https://github.com/averak/rcc-keiba-2020-demo/archive/master.zip)をダウンロードして展開する

### インストール

```sh
$ pip install -U pip
$ pip install -r requirements.txt
```

### 競馬データのセットアップ

1. [サブセット](https://drive.google.com/u/0/uc?id=1HivwQZzO7PPCBkz8TamnVOqcFAmqyhhw&export=download)をダウンロード
2. 展開し，json ファイルを data/ 配下にコピー

```sh
$ cp -ip "サブセット/*.json" data
```

### 学習

```sh
$ ./train.py
```

## AI について

1 レースは 21 頭の競走馬が競うものとし，その中から 1 着を予測する

### DNN

- 64 nodes の feed-forward 層（ReLU，Dropout 率：0.1）
- 128 nodes の feed-forward 層（ReLU，Dropout 率：0.4）
- 256 nodes の feed-forward 層（ReLU，Dropout 率：0.4）
- 21 nodes の feed-forward 層（softmax）

### 特徴量

特徴量は，レース特徴と競走馬特徴を用いる

下記の 3 項目をレース特徴とする

- 馬場状態：芝 or ダート
- 距離：[m]
- 天気：晴 or 曇 or 雨

21 頭の競走馬それぞれが下記の 7 次元ベクトルの特徴をもつ

- 枠
- 性別：牡 or 牝 or セ
- 年齢
- 単勝オッズ
- 体重
- 体重増減
- 斤量

上記のレース特徴（3 次元）と，競走馬特徴（7 次元\*21 頭）を合わせた 150 次元のベクトルを特徴量とし，DNN へ入力する

この入力ベクトルから，1 着競走馬のクラスタリング問題として予測を行う

## 作成者

- [Averak](https://github.com/averak)
