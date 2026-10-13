"""Regression tests for libwkwkwk."""

import unittest
from contextlib import redirect_stdout
from io import StringIO

from wkwkwk import wkwkwk


class WkwkwkTests(unittest.TestCase):
    def call_silently(self, *args, **kwargs):
        output = StringIO()
        with redirect_stdout(output):
            result = wkwkwk(*args, **kwargs)
        return result, output.getvalue()

    def test_never_allows_pass(self):
        result, output = self.call_silently(
            topik="Qweny dan filesystem",
            level=8,
        )
        self.assertEqual(result["status"], "NOT_VERIFIED")
        self.assertIs(result["pass_allowed"], False)
        self.assertIs(result["coffee_required"], True)
        self.assertEqual(result["level"], 8)
        self.assertEqual(result["warnings"], [])
        self.assertIsNone(result["evidence"])
        self.assertIn("AUDIT: NOT_VERIFIED", output)
        self.assertIn("PASS: DILARANG TANPA BUKTI", output)

    def test_invalid_level_falls_back_and_warns(self):
        result, output = self.call_silently(
            topik="Bug yang berubah jadi fitur",
            level="QWENY",
        )
        self.assertEqual(result["status"], "NOT_VERIFIED")
        self.assertIs(result["pass_allowed"], False)
        self.assertEqual(result["level"], 3)
        self.assertIn("LEVEL_INVALID_FALLBACK_3", result["warnings"])
        self.assertIn("WKWKWK 😂", output)

    def test_level_is_clamped_to_supported_range(self):
        low, _ = self.call_silently(level=0)
        high, _ = self.call_silently(level=100)
        self.assertEqual(low["level"], 1)
        self.assertEqual(high["level"], 20)

    def test_fail_closed_false_still_does_not_allow_pass(self):
        result, output = self.call_silently(fail_closed=False)
        self.assertIs(result["fail_closed"], False)
        self.assertIs(result["pass_allowed"], False)
        self.assertEqual(result["status"], "NOT_VERIFIED")
        self.assertNotIn("AUDIT: NOT_VERIFIED", output)

    def test_bool_level_is_normalized_by_int_conversion(self):
        result, _ = self.call_silently(level=True)
        self.assertEqual(result["level"], 1)
        self.assertEqual(result["warnings"], [])

    def test_unconvertible_level_types_fall_back(self):
        result, _ = self.call_silently(level=None)
        self.assertEqual(result["level"], 3)
        self.assertIn("LEVEL_INVALID_FALLBACK_3", result["warnings"])


if __name__ == "__main__":
    unittest.main()
