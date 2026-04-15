from pyrogram import Client, filters
from parser import parse_game
from engine import ChessHelper

# 🔑 Fill your details here
API_ID = 123456
API_HASH = "your_api_hash"
BOT_USERNAME = "GameFactoryBot"

STOCKFISH_PATH = "stockfish"  # Termux/mobile
# STOCKFISH_PATH = "stockfish.exe"  # PC

app = Client("chess_session", api_id=API_ID, api_hash=API_HASH)
helper = ChessHelper(STOCKFISH_PATH)

last_state = None

@app.on_message(filters.chat(BOT_USERNAME))
def handle(client, message):
    global last_state

    if not message.text:
        return

    text = message.text

    # ignore game end
    if "win" in text.lower() or "result" in text.lower():
        return

    moves, my_turn = parse_game(text)

    if not moves:
        return

    state = " ".join(moves)
    if state == last_state:
        return

    last_state = state

    if not my_turn:
        return

    suggestion = helper.get_suggestion(moves)

    print("\n🔥 Your Turn!")
    print("Best move:", suggestion)
    print("")

app.run()
