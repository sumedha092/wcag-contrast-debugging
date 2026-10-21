"""
WCAG 2.x Color Contrast Checker
Author: Sumedha Gupta

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
    hex_color = hex_color.lstrip("#")

    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return (r, g, b)


def relative_luminance(hex_color: str) -> float:
    """Return WCAG relative luminance (0.0 = black, 1.0 = white).

    Steps (from the WCAG spec):
      1. Divide each channel by 255 to get a value 0-1.
      2. Linearize each channel:
           if c <= 0.04045:  c / 12.92
           else:             ((c + 0.055) / 1.055) ** 2.4
      3. L = 0.2126 * R + 0.7152 * G + 0.0722 * B
    """
    r, g, b = hex_to_rgb(hex_color)

    r = r / 255
    g = g / 255
    b = b / 255

    def linearize(c):
        if c <= 0.04045:
            return c / 12.92
        return ((c + 0.055) / 1.055) ** 2.4

    r = linearize(r)
    g = linearize(g)
    b = linearize(b)

    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color1: str, color2: str) -> float:
    """Return the contrast ratio between two colors, from 1.0 to 21.0.

    Formula: (L_lighter + 0.05) / (L_darker + 0.05)
    Must give the same answer no matter which color is passed first.
    """
    luminance1 = relative_luminance(color1)
    luminance2 = relative_luminance(color2)

    lighter = max(luminance1, luminance2)
    darker = min(luminance1, luminance2)

    return (lighter + 0.05) / (darker + 0.05)


def passes_aa(color1: str, color2: str, large_text: bool = False) -> bool:
    """WCAG AA: normal text needs >= 4.5:1, large text needs >= 3.0:1."""
    ratio = contrast_ratio(color1, color2)

    if large_text:
        threshold = 3.0
    else:
        threshold = 4.5

    return ratio >= threshold


if __name__ == "__main__":
    # Simple command-line demo
    fg = input("Text color (hex): ")
    bg = input("Background color (hex): ")
    ratio = contrast_ratio(fg, bg)
    print(f"Contrast ratio: {ratio:.2f}:1")
    print("AA normal text:", "PASS" if passes_aa(fg, bg) else "FAIL")
    print("AA large text: ", "PASS" if passes_aa(fg, bg, large_text=True) else "FAIL")
