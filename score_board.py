class ScoreBoard:
    """Fixed length sequence of high scores in non decreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacityself.

        All entries are initially noneself.
        """

        self._board = [None] * capacity   #reserve space for future scores
        self._n = 0   #number of actual entries

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Consider adding entries to high scores."""
        score = entry.get_score()
        #Does new entry qualify as a high score?
        #answer is true if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            #shift lower scores rightwards to make room for new entry
            j = self._n -1
            while j>0 and self._board[j-1].get_score() < score :
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry
