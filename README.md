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
$ pip install -r requerements.txt
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

## 作成者

- [Averak](https://github.com/averak)
