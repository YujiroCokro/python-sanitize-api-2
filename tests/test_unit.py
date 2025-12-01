from app.main import replace_chars

def test_replace_basic_chars():
    replacements = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}
    assert replace_chars("kotor", replacements) == "k0t0r"

def test_replace_multiple_words():
    replacements = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}
    assert replace_chars("aku suka nasi", replacements) == "4ku 5uk4 n451"

