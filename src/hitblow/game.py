"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    from .mode import select_game_mode
    from .ternlimit import select_difficulty

    # 1. ゲームモード（通常 vs 回数制限 vs 時間制限）を選択
    game_mode = select_game_mode()
    
    # 2. 変数の初期化
    max_tries = float("inf")
    
    # 3. モードに応じた処理の分岐
    if game_mode == "count":
        # 回数制限が選ばれたら、続けて難易度を選択
        max_tries = select_difficulty()
    elif game_mode == "time":
        print("【時間制限モード】で開始します。")

    from .mode import select_time_limit
    import time

    time_limit = select_time_limit()
    start_time = time.time()
    # 通常モード（normal）の場合は初期値のままで何もしない

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue

        from .mode import is_time_over

        if game_mode == "time":
            if is_time_over(start_time, time_limit):
                print("時間切れ！")
                print(f"答えは {secret} でした")
                break

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")
        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            from .score import calculate_score

            score = calculate_score(tries)

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            print(f"あなたのスコア：{score} 点")
            break

        
