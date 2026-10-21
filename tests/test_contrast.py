"""Expected values verified against the WCAG 2.1 formula."""
import pytest
from contrast import hex_to_rgb, relative_luminance, contrast_ratio, passes_aa, passes_aaa

# ---------- hex_to_rgb ----------
def test_hex_full():
    assert hex_to_rgb("#FF8000") == (255, 128, 0)

def test_hex_no_hash():
    assert hex_to_rgb("00FF00") == (0, 255, 0)

def test_hex_lowercase():
    assert hex_to_rgb("#abcdef") == (171, 205, 239)

def test_hex_shorthand():
    assert hex_to_rgb("#fff") == (255, 255, 255)


# ---------- relative_luminance ----------
def test_luminance_black():
    assert relative_luminance("#000000") == pytest.approx(0.0)

def test_luminance_white():
    assert relative_luminance("#FFFFFF") == pytest.approx(1.0)

def test_luminance_red():
    assert relative_luminance("#FF0000") == pytest.approx(0.2126, abs=1e-4)

def test_luminance_gray():
    assert relative_luminance("#808080") == pytest.approx(0.2159, abs=1e-4)


# ---------- contrast_ratio ----------
def test_ratio_black_white():
    assert contrast_ratio("#000000", "#FFFFFF") == pytest.approx(21.0, abs=0.01)

def test_ratio_order_independent():
    assert contrast_ratio("#FFFFFF", "#000000") == pytest.approx(21.0, abs=0.01)

def test_ratio_same_color():
    assert contrast_ratio("#336699", "#336699") == pytest.approx(1.0)

def test_ratio_gray_777():
    assert contrast_ratio("#777777", "#FFFFFF") == pytest.approx(4.48, abs=0.01)

def test_ratio_blue():
    assert contrast_ratio("#0000FF", "#FFFFFF") == pytest.approx(8.59, abs=0.01)


# ---------- passes_aa (integration of all functions) ----------
def test_aa_fail_just_below():
    assert passes_aa("#777777", "#FFFFFF") is False      # 4.48 < 4.5

def test_aa_pass_just_above():
    assert passes_aa("#767676", "#FFFFFF") is True       # 4.54 >= 4.5

def test_aa_large_text_pass():
    assert passes_aa("#949494", "#FFFFFF", large_text=True) is True   # 3.03 >= 3.0

def test_aa_large_text_red():
    assert passes_aa("#FF0000", "#FFFFFF", large_text=True) is True   # 4.0
    assert passes_aa("#FF0000", "#FFFFFF") is False

# ---------- input validation ----------
def test_invalid_hex_characters():
    with pytest.raises(ValueError, match="Invalid hex color"):
        hex_to_rgb("#GGG")

def test_aaa_normal_text_threshold():
    assert passes_aaa("#666666", "#FFFFFF") is False

def test_rgb_string_input():
    assert hex_to_rgb("rgb(255, 0, 0)") == (255, 0, 0)