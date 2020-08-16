import json
import glob
import numpy as np
import sklearn.preprocessing


def read_races(target_dir='data'):
    result = []

    files = glob.glob(target_dir + '/*.json')
    for file in files:
        data = json.load(open(file, 'r'))
        result.extend(data['racedata'])

    return result


def sort_horse(val):
    return val['枠']


def preprocessing(data):
    x = []
    y = []

    for race in data:
        race_proc = []

        # レース特徴
        if race['馬場状態'] is None or race['距離'] is None or race['天気'] is None:
            # 欠損値を無視
            continue
        race_proc.append(['芝', 'ダート'].index(race['馬場状態']))
        race_proc.append(race['距離'])
        race_proc.append(['晴', '曇', '雨'].index(race['天気']))

        # 競走馬特徴
        race['競走馬'] = sorted(race['競走馬'], key=sort_horse)
        for i in range(21):
            if i < len(race['競走馬']):
                horse = race['競走馬'][i]
                horse_proc = []
                horse_proc.append(horse['枠'])
                horse_proc.append(['牡', '牝', 'セ'].index(horse['性別']))
                horse_proc.append(horse['年齢'])
                horse_proc.append(horse['単勝オッズ'])
                horse_proc.append(horse['体重'])
                horse_proc.append(horse['体重増減'])
                horse_proc.append(horse['斤量'])
                race_proc.extend(horse_proc)

                if horse['順位'] == 1:
                    y.append(i)
            else:
                race_proc.extend(np.zeros(len(horse_proc)))

        x.append(race_proc)

    # 標準化（平均0，分散1）
    scaler = sklearn.preprocessing.StandardScaler()
    x = scaler.fit_transform(x)
    x = np.array(x)
    y = np.array(y)

    return x, y
