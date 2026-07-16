"""ゲームモード（通常・回数制限・時間制限）を選択・管理するモジュール。"""

def select_game_mode():
    """ゲームモードを選択させ、モードの種類を返す。
    
    Returns:
        str: "normal" (通常), "count" (回数制限), "time" (時間制限)
    """
    print("\nゲームモードを選んでください：")
    print("1: 通常モード     (制限なしでじっくりプレイ)")
    print("2: 回数制限モード (指定された回数内で挑戦)")
    print("3: 時間制限モード (タイマー機能)")
    
    while True:
        choice = input("選択 (1-3) > ").strip()
        if choice == "1":
            print("【通常モード】で開始します。")
            return "normal"
        elif choice == "2":
            return "count"
        elif choice == "3":
            return "time"
        else:
            print("1, 2, 3 のいずれかを入力してください。")

import time

def select_time_limit():
    """制限時間を選択させる"""

    while True:
        try:
            limit = int(input("制限時間（秒）を入力してください > "))
            if limit > 0:
                return limit
            print("1以上を入力してください。")
        except ValueError:
            print("数字を入力してください。")

def is_time_over(start_time, limit):
    """制限時間を超えたか判定する"""

    elapsed = time.time() - start_time
    return elapsed >= limit