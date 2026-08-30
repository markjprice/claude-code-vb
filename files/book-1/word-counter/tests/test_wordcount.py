import pytest

from wordcount import analyze, count_sentences, count_words, main, read_text_file


def write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return p


def test_normal_txt_file(tmp_path):
    p = write(tmp_path, "sample.txt", "Hello world. How are you? I am fine!")
    text = read_text_file(p)
    assert analyze(text) == {"words": 8, "sentences": 3, "characters": 36}


def test_single_word_no_punctuation():
    assert count_words("hello") == 1
    assert count_sentences("hello") == 1


def test_empty_file(tmp_path):
    p = write(tmp_path, "empty.txt", "")
    assert analyze(read_text_file(p)) == {"words": 0, "sentences": 0, "characters": 0}


def test_whitespace_only_is_zero_sentences():
    assert count_sentences("   \n\t ") == 0


def test_ellipsis_counts_as_one_sentence():
    assert count_sentences("wait... what") == 1


def test_non_txt_rejected(tmp_path):
    p = write(tmp_path, "notes.md", "hi")
    with pytest.raises(ValueError):
        read_text_file(p)


def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        read_text_file(tmp_path / "nope.txt")


def test_main_missing_file_exits_1(tmp_path, capsys):
    assert main([str(tmp_path / "nope.txt")]) == 1
    assert "error:" in capsys.readouterr().err


def test_main_reports_counts(tmp_path, capsys):
    p = write(tmp_path, "a.txt", "One two three.")
    assert main([str(p)]) == 0
    out = capsys.readouterr().out
    assert "words:      3" in out
    assert "sentences:  1" in out
