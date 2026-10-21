# WCAG Contrast Checker — Debugging Competency Project

A Python accessibility tool that calculates color contrast ratios and checks whether color combinations meet WCAG contrast requirements. The project began with WCAG 2.1 AA checking and was extended during debugging to include AAA checking, invalid-input validation, and CSS-style RGB color support.

Built for the CSE 485 _Growing a Competency_ assignment to practice the **Seven Steps of Debugging** and apply systematic debugging techniques to accessibility-related software.

## How to Run

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the complete test suite:

```bash
python -m pytest -v
```

Run the interactive contrast checker:

```bash
python contrast.py
```

On macOS, `python3` and `pip3` may be used instead.

## Features

- Converts full hexadecimal colors such as `#FF8000`
- Supports hexadecimal colors without `#`
- Supports shorthand colors such as `#fff`
- Supports CSS-style RGB strings such as `rgb(255, 0, 0)`
- Validates malformed hexadecimal and RGB input
- Calculates WCAG relative luminance
- Calculates contrast ratios from 1:1 to 21:1
- Checks WCAG AA requirements
  - Normal text: 4.5:1
  - Large text: 3.0:1
- Checks WCAG AAA requirements
  - Normal text: 7.0:1
  - Large text: 4.5:1

## Project Structure

```text
contrast.py            # Color parsing, luminance, contrast, AA, and AAA checks
tests/test_contrast.py # 20 automated tests
DEBUG_LOG.md           # Seven-step debugging log for three bugs
screenshots/           # Debugger, test, diff, and application evidence
```

## Test Results

The final test suite contains **20 tests**, including the original WCAG tests and additional tests created while debugging and extending the checker.

Final result:

```text
20 passed
```

## Debugging Summary

| Bug                        | Symptom                                                                                           | Root cause                                                               | Fix commit |
| -------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------- |
| 1. Invalid hex characters  | `#GGG` produced Python's low-level `int()` conversion error instead of a clear validation message | Hex characters were passed to `int(..., 16)` without explicit validation | `520c05f`  |
| 2. Incorrect AAA threshold | Normal text with a 5.74:1 ratio incorrectly passed AAA                                            | `passes_aaa()` used the 4.5 large-text threshold for normal text         | `e785f26`  |
| 3. RGB strings rejected    | `rgb(255, 0, 0)` raised `ValueError("Invalid hex color")`                                         | Every input was treated as hexadecimal before its format was identified  | `f86b9f5`  |

See [DEBUG_LOG.md](DEBUG_LOG.md) for the complete seven-step debugging process, breakpoint observations, fixes, verification results, and reflections for each bug.

## Accessibility Application

I used the completed checker on a common enterprise UI color combination: light-gray text (`#999999`) on a white (`#FFFFFF`) background.

The checker calculated a contrast ratio of **2.85:1**, which fails WCAG AA requirements for both normal and large text. This demonstrates how the tool can identify color choices that may make interface text difficult to read.

Evidence is included in `screenshots/capstone_check.png`.

## Resources

- _The Seven Steps of Debugging_ (YouTube)
- WCAG 2.1 relative luminance and contrast ratio definitions (W3C)
- VS Code Python debugging documentation
