# WCAG Contrast Checker — Debugging Competency Project

A Python tool that checks whether two colors meet **WCAG 2.1 AA** contrast requirements
(4.5:1 for normal text, 3:1 for large text). Built for the CSE 485 *Growing a Competency*
assignment to practice the **Seven Steps of Debugging**, and related to my capstone project
(20 Studio XE — Accessibility Conformance for Enterprise Platform).

## How to run

```bash
pip install -r requirements.txt
python -m pytest -v        # run the test suite
python contrast.py         # interactive checker
```

## Project structure

```
contrast.py            # the checker (hex parsing, luminance, ratio, AA check)
tests/test_contrast.py # 17 tests with WCAG-verified expected values
DEBUG_LOG.md           # step-by-step log of every bug I found and fixed
screenshots/           # evidence from the VS Code debugger
```

## Debugging summary

| Bug | Symptom | Root cause | Fix commit |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

See [DEBUG_LOG.md](DEBUG_LOG.md) for the full 7-step process on each bug.

## Resources
- *The Seven Steps of Debugging* (YouTube)
- WCAG 2.1 — Relative luminance & contrast ratio definitions (W3C)
- VS Code Python debugging docs
