import streamlit as st
from PIL import Image
import random

# --------------------------------------------------
# 1. データの準備と初期化
# --------------------------------------------------
quiz_data = [
    {
        "images": ["アマージョ.png", "マスカーニャ.png","ビークイン.png"],
        "answer": "すみれ",
        "hint": "3年女子"
    },
    {
        "images": ["シャワーズ.png", "ラプラス.png"],
        "answer": "あおい",
        "hint": "3年女子"
    },
    {
        "images": ["ヤバソチャ.png", "モトトカゲ.png", "ヤナップ.png"],
        "answer": "くぼっち",
        "hint": "3年男子"
    },
    {
        "images": ["ケッキング.png", "カビゴン.png", "マフィティフ.png", "ミツハニー.png"],
        "answer": "りん",
        "hint": "3年男子"
    },
    {
        "images": ["ブイゼル.png", "ワルビル.png"],
        "answer": "にいちゃん",
        "hint": "3年男子"
    },
    {
        "images": ["ガーディ(ヒスイの姿).png", "シュバルゴ.png"],
        "answer": "こーへい",
        "hint": "3年男子"
    },
    {
        "images": ["フカマル.png", "ゲコガシラ.png", "ウソッキー.png", "ゴーゴート.png", "ミツハニー.png"],
        "answer": "さとっしー",
        "hint": "3年男子"
    }
]

# セッション状態の初期化
if "shuffled_data" not in st.session_state:
    st.session_state.shuffled_data = random.sample(quiz_data, len(quiz_data))
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.is_finished = False
    st.session_state.answered = False  # 回答済みかどうかを管理
    st.session_state.last_result = None # 直前の結果メッセージ

# --------------------------------------------------
# 2. 画面表示の制御
# --------------------------------------------------
st.title("🖼️ 画像連想クイズ")

if st.session_state.is_finished:
    # --- 終了画面 ---
    st.balloons()
    st.success("🎉 全問終了です！お疲れ様でした！")
    st.write(f"### 最終スコア: **{st.session_state.score} / {len(quiz_data)}**")
    
    if st.button("もう一度遊ぶ"):
        st.session_state.shuffled_data = random.sample(quiz_data, len(quiz_data))
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.is_finished = False
        st.session_state.answered = False
        st.rerun()

else:
    # --- クイズ実行画面 ---
    current_q = st.session_state.shuffled_data[st.session_state.current_index]
    total_q = len(quiz_data)
    
    st.subheader(f"第 {st.session_state.current_index + 1} 問 / 全 {total_q} 問")
    st.write("表示されている画像に関連する単語を答えてね！")

    # 画像を表示（1行あたり最大3枚まで表示し、4枚目以降は自動で次の行へ）
    images = current_q["images"]
    IMAGES_PER_ROW = 3

    for i in range(0, len(images), IMAGES_PER_ROW):
        row_images = images[i : i + IMAGES_PER_ROW]
        cols = st.columns(len(row_images))
        
        for col, img_path in zip(cols, row_images):
            try:
                image = Image.open(img_path)
                col.image(image, use_container_width=True)
            except Exception:
                col.error("画像が見つかりません")

    st.write("---")

    # 【まだ回答していない場合】回答欄と回答ボタンを表示
    if not st.session_state.answered:
        user_answer = st.text_input("回答を入力してください：", key=f"ans_input_{st.session_state.current_index}")
        
        if st.button("回答する", type="primary"):
            correct_answer = current_q["answer"]
            if user_answer.strip() == correct_answer:
                st.session_state.score += 1
                st.session_state.last_result = ("success", "🎉 正解！")
            else:
                st.session_state.last_result = ("error", f"❌ 不正解...（正解は「{correct_answer}」でした）")
            
            # 回答済み状態にして画面更新
            st.session_state.answered = True
            st.rerun()

    # 【回答した後】入力欄を隠して結果と「次の問題へ」ボタンを表示
    else:
        res_type, res_msg = st.session_state.last_result
        if res_type == "success":
            st.success(res_msg)
        else:
            st.error(res_msg)

        if st.button("次の問題へ進む ➔"):
            # 次の問題の準備
            st.session_state.answered = False
            if st.session_state.current_index + 1 < total_q:
                st.session_state.current_index += 1
            else:
                st.session_state.is_finished = True
            st.rerun()
