# libwkwkwk v0.1

**Fail-Closed Comedy Engineering:** ketawa boleh bebas, klaim harus punya bukti.

`libwkwkwk` is a tiny Python comedy helper that prints a laugh and returns a structured result. It is intentionally **not** an audit tool and does not inspect Git, run tests, or certify production readiness.

## Requirements

- Python 3.9+ (uses built-in generics and `unittest`)
- No third-party runtime dependencies

## Usage

```python
from wkwkwk import wkwkwk

result = wkwkwk(
    topik="Qweny dan filesystem",
    level=8,
)

assert result["status"] == "NOT_VERIFIED"
assert result["pass_allowed"] is False
```

Example output:

```text
WKWKWKWKWKWKWK 😂
Topik: Qweny dan filesystem
Kesimpulan ilmiah: perlu ngopi dulu.
AUDIT: NOT_VERIFIED
PASS: DILARANG TANPA BUKTI
```

The `assert` example is illustrative: writing an assertion does not prove it was executed. Use the test command below to execute the regression suite.

## Input behavior

- `level` is converted to an integer and clamped to `1..20`.
- Values that cannot be converted fall back to `3` and add `LEVEL_INVALID_FALLBACK_3` to `warnings`.
- `fail_closed=True` prints an explicit `NOT_VERIFIED` disclaimer.
- `pass_allowed` is always `False`, even when `fail_closed=False`.
- `evidence` is always `None`; this function does not collect evidence.

## Run regression tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

Only the actual output from an executed test run can support a test-pass claim. This README alone is not test evidence.

## Project status

- Version: `0.1.0`
- Test framework: Python standard-library `unittest`
- External systems checked: none
- Git status checked by this package: no
- Production certification: none

## License

No license has been selected for this initial draft. All rights are reserved by default unless a license is added. Do not assume the code is open-source licensed until a license file is committed.
