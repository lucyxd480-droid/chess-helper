import chess
import chess.engine

class ChessHelper:
    def __init__(self, path, think_time=0.4):
        self.engine = chess.engine.SimpleEngine.popen_uci(path)
        self.board = chess.Board()
        self.time = think_time

    def get_suggestion(self, moves):
        self.board.reset()

        for m in moves:
            try:
                self.board.push_san(m)
            except:
                break

        result = self.engine.play(
            self.board,
            chess.engine.Limit(time=self.time)
        )

        return self.board.san(result.move)
