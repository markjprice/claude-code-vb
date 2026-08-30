import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import convert
from convert import ConversionError, convert as do_convert, main

SCRIPT = Path(__file__).resolve().parents[1] / "convert.py"


def test_cup_to_ml():
    result, cat = do_convert(1, "cup", "ml")
    assert cat == "volume"
    assert result == 236.59


def test_liter_to_ml_alias():
    assert do_convert(2, "litre", "ml")[0] == 2000.0


def test_volume_round_trip():
    ml, _ = do_convert(3, "cup", "ml")
    cups, _ = do_convert(ml, "ml", "cup")
    assert cups == pytest.approx(3, abs=0.01)


def test_currency_round_trip():
    eur, cat = do_convert(100, "usd", "eur")
    assert cat == "currency"
    back, _ = do_convert(eur, "eur", "usd")
    assert back == pytest.approx(100, abs=0.5)


def test_rounding_to_two_decimals():
    result, _ = do_convert(1, "tsp", "ml")
    assert result == 4.93


def test_unknown_unit_names_supported():
    with pytest.raises(ConversionError) as exc:
        do_convert(1, "cup", "furlong")
    msg = str(exc.value)
    assert "furlong" in msg
    assert "gallon" in msg  # lists supported volume units


def test_cross_category_rejected():
    with pytest.raises(ConversionError) as exc:
        do_convert(5, "usd", "ml")
    assert "same kind" in str(exc.value)


def test_forced_category_unknown():
    with pytest.raises(ConversionError):
        do_convert(1, "cup", "ml", category_name="currency")


def test_main_happy(capsys):
    rc = main(["1", "cup", "ml"])
    assert rc == 0
    assert capsys.readouterr().out.strip() == "1 cup = 236.59 ml"


def test_main_error_exit_code(capsys):
    rc = main(["1", "cup", "furlong"])
    assert rc == 1
    assert "furlong" in capsys.readouterr().err


def test_cli_list_runs():
    out = subprocess.run([sys.executable, str(SCRIPT), "--list"],
                         capture_output=True, text=True)
    assert out.returncode == 0
    assert "volume" in out.stdout and "currency" in out.stdout
