from PyQt5 import Qsci


class HeaderWidget(Qsci.QsciScintilla):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLexer(Qsci.QsciLexerYAML(self))
