"""
WCAG 2.x Color Contrast Checker
Author: <your name>

Reference: https://www.w3.org/TR/WCAG21/#dfn-relative-luminance
           https://www.w3.org/TR/WCAG21/#dfn-contrast-ratio

YOUR JOB: implement each function below (replace `raise NotImplementedError`).
Run the tests with:   python -m pytest -v
"""


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert '#RRGGBB', 'RRGGBB', or shorthand '#RGB' to an (r, g, b) tuple of 0-255 ints.

    Example: hex_to_rgb('#FF8000') -> (255, 128, 0)
             hex_to_rgb('#fff')    -> (255, 255, 255)
    """
    raise NotImplementedError


def relative_luminance(hex_color: str) -> float:
    """Return WCAG relative luminance (0.0 = black, 1.0 = white).

    Steps (from the WCAG spec):
      1. Divide each channel by 255 to get a value 0-1.
      2. Linearize each channel:
           if c <= 0.04045:  c / 12.92
           else:             ((c + 0.055) / 1.055) ** 2.4
      3. L = 0.2126 * R + 0.7152 * G + 0.0722 * B
    """
    raise NotImplementedError


def contrast_ratio(color1: str, color2: str) -> float:
    """Return the contrast ratio between two colors, from 1.0 to 21.0.

    Formula: (L_lighter + 0.05) / (L_darker + 0.05)
    Must give the same answer no matter which color is passed first.
    """
    raise NotImplementedError


def passes_aa(color1: str, color2: str, large_text: bool = False) -> bool:
    """WCAG AA: normal text needs >= 4.5:1, large text needs >= 3.0:1."""
    raise NotImplementedError


if __name__ == "__main__":
    # Simple command-line demo
    fg = input("Text color (hex): ")
    bg = input("Background color (hex): ")
    ratio = contrast_ratio(fg, bg)
    print(f"Contrast ratio: {ratio:.2f}:1")
    print("AA normal text:", "PASS" if passes_aa(fg, bg) else "FAIL")
    print("AA large text: ", "PASS" if passes_aa(fg, bg, large_text=True) else "FAIL")
