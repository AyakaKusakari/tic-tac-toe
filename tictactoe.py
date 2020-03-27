"""
1.最初のプレイヤーが記号を書き込む
2.その時点で記号が3つ並んでいるかを確認
3.次のプレイヤーが記号を書き込む
3以降は2〜3をくり返す
"""

start = """
_/_/_/_/_/_/_/_/_/_/_/_/_/

      Tic Tac Toe

_/_/_/_/_/_/_/_/_/_/_/_/_/

【遊び方】
1～9で座標を選んでください。
※0を入力すると、ゲームが終了します。
"""

table = """
1|2|3
-----
4|5|6
-----
7|8|9
"""

win = """

"""

print(start)
print(table)

# 1～9までのリスト
candidates = [i for i in range(1, 10)]
# 先行
first_list = []
# 後攻
second_list = []
# カウント用
n = 1

# coordinate = 今まで書き込んだ座標リスト
# coordinateの中身のリストをset関数でソートさせ、もう１つのsetとの共通部分をリスト化させ、比較する
def judgment(coordinate):
    # 横のパターン
    if [1, 2, 3] == list(set([1, 2, 3]) & set(coordinate)):
        return True
    elif [4, 5, 6] == list(set([4, 5, 6]) & set(coordinate)):
        return True
    # 効かない
    elif [7, 8, 9] == list(set([7, 8, 9]) & set(coordinate)):
        return True
    # 縦のパターン
    elif [1, 4, 7] == list(set([1, 4, 7]) & set(coordinate)):
        return True
    # 効かない
    elif [2, 5, 8] == list(set([2, 5, 8]) & set(coordinate)):
        return True
    # 効かない
    elif [3, 6, 9] == list(set([3, 6, 9]) & set(coordinate)):
        return True
    # 斜めのパターン
    elif [1, 5, 9] == list(set([1, 5, 9]) & set(coordinate)):
        return True
    elif [3, 5, 7] == list(set([3, 5, 7]) & set(coordinate)):
        return True
    return False

while True:
    # 奇数回の時
    if n % 2 == 1:
        print(f"      ---{n}手目---\n")
        first = input("○の座標を入力してください：")
        # 整数に変換
        first = int(first)
        
        if first in candidates:
            # 入力した数字を○に置換
            table = table.replace(str(first), "o")
            # 元の座標リストから、入力した数字を削除
            candidates.remove(first)
            # リストに入力した座標を追加
            first_list.append(first)
            print(table)
            n += 1
            if judgment(first_list):
                print(" ---------------\n|   ○の勝ち!!   |\n ---------------")
                break
        elif first == 0:
            print("\n -------------------------\n|   ゲームを終了します。   |\n -------------------------")
            break
        else:
            print("\n※正しい座標を入力してください\n")
            continue
    # 9回で勝敗がつかなかったらあいこ
    elif n == 10:
        print(" -------------------\n|   あいこでした。   |\n -------------------")
        break
    # 偶数回の時
    else:
        print(f"      ---{n}手目---\n")
        second = input("×の座標を入力してください：")
        # 整数に変換
        second = int(second)
        
        if second in candidates:
            # 入力した数字を×に置換
            table = table.replace(str(second), "x")
            # 元の座標リストから、入力した数字を削除
            candidates.remove(second)
            # リストに入力した座標を追加
            second_list.append(second)
            print(table)
            n += 1
            if judgment(second_list):
                print(" ---------------\n|   ×の勝ち!!   |\n ---------------")
                break
        elif second == 0:
            print("\n -------------------------\n|   ゲームを終了します。   |\n -------------------------")
            break
        else:
            print("\n※正しい座標を入力してください\n")
            continue