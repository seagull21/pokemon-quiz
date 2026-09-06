import streamlit as st
from PIL import Image
import random

# --------------------------------------------------
# 1. データの準備と初期化
# --------------------------------------------------
# answer をリスト形式にすることで、複数の表記を正解判定できるようにしています
quiz_data = [
    {
        "images": ["アマージョ.png", "マスカーニャ.png", "ビークイン.png", "サーナイト.png", "マフォクシー.png", "ヒメグマ.png"],
        "answer": ["すみれ", "すみれさん","栄川さん","上司"],
        "hint": "3年女子"
    },
    {
        "images": ["シャワーズ.png", "ラプラス.png", "スターミー.png", "マナフィ.png", "サニーゴ.png", "タッツー.png"],
        "answer": ["あおい", "あおちゃん","水野さん","水野","みずのさん","あおいさん","あおい"],
        "hint": "3年女子"
    },
    {
        "images": ["ヤバソチャ.png", "モトトカゲ.png", "ヤナップ.png", "アーケン.png", "ロトム.png", "ダイノーズ.png"],
        "answer": ["くぼっち", "窪田"],
        "hint": "3年男子"
    },
    {
        "images": ["ケッキング.png", "カビゴン.png", "マフィティフ.png", "ヤドン.png", "モジャンボ.png", "ミツハニー.png"],
        "answer": ["りん", "りんちゃん","坂本さん","代表"],
        "hint": "3年男子"
    },
    {
        "images": ["ブイゼル.png", "ワルビル.png", "クレッフィ.png"],
        "answer": ["にいちゃん", "にーちゃん", "ゆうき","ゆうきさん","新本"],
        "hint": "3年男子"
    },
    {
        "images": ["ガーディ(ヒスイの姿).png", "シュバルゴ.png"],
        "answer": ["こーへい", "こうへい"],
        "hint": "3年男子"
    },
    {
        "images": ["ピカチュウ.png", "ゲコガシラ.png", "ゴーゴート.png", "ルクシオ.png", "アギルダー.png", "ミツハニー.png"],
        "answer": ["さとっしー", "小倉"],
        "hint": "3年男子"
    },
    {
        "images": ["ムーランド.png", "トロピウス.png", "フライゴン.png", "カイリュー.png"],
        "answer": ["カトゥーン", "カトゥーンさん","加藤さん","加藤"],
        "hint": "4年生以上男子"
    },
    {
        "images": ["ペラップ.png", "ルンパッパ.png", "ニャース.png", "バリヤード.png", "ドンカラス.png", "キテルグマ.png"],
        "answer": ["さわとも", "さわともさん"],
        "hint": "4年生以上男子"
    },
    {
        "images": ["チリーン.png", "マーイーカ.png", "メブキジカ.png"],
        "answer": ["あっきー", "あっきーさん","あきしか","あきしかさん","穐鹿さん","穐鹿"],
        "hint": "4年生以上男子"
    },
    {
        "images": ["チリーン.png", "ヒトモシ.png", "バケッチャ.png", "ネッコアラ.png"],
        "answer": ["あやかん", "あやかんさん","あやね","あやねちゃん","今坂","今坂さん","いまさか","いまさかさん"],
        "hint": "2年女子"
    },
    {
        "images": ["マホイップ.png", "プリン.png", "ピクシー.png"],
        "answer": ["かいびぃ", "かいびぃさん","稲井","かい","かいさん","いないさん"],
        "hint": "2年男子"
    },
    {
        "images": ["オーベム.png", "ヌケニン.png", "ブラッキー.png", "ジメレオン.png", "マネネ.png"],
        "answer": ["フルオロ", "フルオロさん","ふくよし","ふくよしさん"],
        "hint": "2年男子"
    },
    {
        "images": ["バクオング.png", "グライガー.png", "カラナクシ.png", "グレッグル.png", "マダツボミ.png"],
        "answer": ["じん", "じんさん","仁","ジン","イニ","ジンさん","さすじん","佐塚"],
        "hint": "2年生男子"
    },
    {
        "images": ["ペロリーム.png", "リーフィア.png", "メガヤンマ.png"],
        "answer": ["ともっきー", "ともっきーさん","ともき","ともきさん"],
        "hint": "2年男子"
    },
    {
        "images": ["パモット.png", "ヌオー.png", "オンバット.png","フラべべ.png", "オタマロ.png", "ビクティニ.png"],
        "answer": ["こうちゃん", "こうちゃんさん","こうさん","猪木","猪木さん"],
        "hint": "2年男子"
    }
]

# セッション状態の初期化
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "shuffled_data" not in st.session_state:
    st.session_state.shuffled_data = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "is_finished" not in st.session_state:
    st.session_state.is_finished = False
if "answered" not in st.session_state:
    st.session_state.answered = False
if "last_result" not in st.session_state:
    st.session_state.last_result = None

# ゲーム開始処理を行う関数
def start_game(num_questions=None):
    if num_questions and num_questions < len(quiz_data):
        # 指定数（10問など）をランダム抽出
        st.session_state.shuffled_data = random.sample(quiz_data, num_questions)
    else:
        # 全問をシャッフル
        st.session_state.shuffled_data = random.sample(quiz_data, len(quiz_data))
    
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.is_finished = False
    st.session_state.answered = False
    st.session_state.game_started = True

# --------------------------------------------------
# 2. 画面表示の制御
# --------------------------------------------------
st.title("日本茶メンバーのポケモン連想クイズ")

# --- A. スタート画面（モード選択） ---
if not st.session_state.game_started:
    st.write("モードを選んでゲームを始めてね！")
    st.write(f"（登録されている問題数：**全 {len(quiz_data)} 問**）")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎲 10問にチャレンジ！", type="primary", use_container_width=True):
            start_game(num_questions=10)
            st.rerun()
            
    with col2:
        if st.button(f"🔥 全問挑戦！（{len(quiz_data)}問）", use_container_width=True):
            start_game(num_questions=None)
            st.rerun()

# --- B. 終了画面 ---
elif st.session_state.is_finished:
    st.balloons()
    st.success("🎉 お疲れ様でした！クイズ終了です！")
    total_q = len(st.session_state.shuffled_data)
    st.write(f"### 最終スコア: **{st.session_state.score} / {total_q}**")
    
    if st.button("タイトルに戻る"):
        st.session_state.game_started = False
        st.rerun()

# --- C. クイズ実行画面 ---
else:
    current_q = st.session_state.shuffled_data[st.session_state.current_index]
    total_q = len(st.session_state.shuffled_data)
    
    st.subheader(f"第 {st.session_state.current_index + 1} 問 / 全 {total_q} 問")
    st.write("表示されている画像に関連する単語を答えてね！")

    # 画像を表示（3枚ごとに改行）
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
            answers = current_q["answer"]
            
            # answer が文字列の場合はリストに変換（互換性確保）
            if isinstance(answers, str):
                answers = [answers]
            
            # 入力された文字がリストのいずれかと一致するか判定
            if user_answer.strip() in answers:
                st.session_state.score += 1
                st.session_state.last_result = ("success", "🎉 正解！")
            else:
                st.session_state.last_result = ("error", f"❌ 不正解...（正解は「{answers[0]}」でした）")
            
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
            st.session_state.answered = False
            if st.session_state.current_index + 1 < total_q:
                st.session_state.current_index += 1
            else:
                st.session_state.is_finished = True
            st.rerun()
