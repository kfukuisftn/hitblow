"""難易度選択と回数制限の設定を行うモジュール。"""

def select_difficulty():
    """ユーザーに難易度を選択させ、最大挑戦回数を返す。"""
    print("\n--- 回数制限モード ---")
    print("難易度を選んでください：")
    print("1: イージー (制限なし)")
    print("2: ノーマル (10回制限)")
    print("3: ハード   (5回制限)")
    
    while True:
        choice = input("選択 (1-3) > ").strip()
        if choice == "1":
            print("【イージーモード】で開始します。")
            return float("inf")
        elif choice == "2":
            print("【ノーマルモード】10回以内に当ててください！")
            return 10
        elif choice == "3":
            print("【ハードモード】5回以内に当ててください！")
            return 5
        else:
            print("1, 2, 3 のいずれかを入力してください。")