import subprocess
import sys
import unittest

from billing import build_receipt, overalltotalcost, tax_paid, total_percent_paid


class MoneyFunctionTests(unittest.TestCase):
    def test_tax(self):
        self.assertAlmostEqual(tax_paid(100), 5.50)

    def test_tip_is_on_cost_not_tax(self):
        self.assertAlmostEqual(total_percent_paid(100, 20), 20.00)

    def test_format(self):
        self.assertEqual(overalltotalcost(125.5), "$125.50")

    def test_receipt_known_values(self):
        receipt = build_receipt(100, 20)
        self.assertIn("5.50", receipt)
        self.assertIn("20.00", receipt)
        self.assertIn("$125.50", receipt)

    def test_receipt_rounding(self):
        receipt = build_receipt(19.99, 15)
        self.assertIn("$24.09", receipt)


class ScriptTests(unittest.TestCase):
    def run_script(self, text):
        return subprocess.run(
            [sys.executable, "billing.py"], input=text, capture_output=True, text=True
        )

    def test_full_run(self):
        out = self.run_script("100\n20\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("$125.50", out.stdout)

    def test_inf_is_rejected(self):
        out = self.run_script("inf\n")
        self.assertEqual(out.returncode, 1)
        self.assertIn("Please enter a number.", out.stdout)

    def test_nan_is_rejected(self):
        out = self.run_script("10\nnan\n")
        self.assertEqual(out.returncode, 1)

    def test_negative_is_rejected(self):
        out = self.run_script("-1\n")
        self.assertEqual(out.returncode, 1)
        self.assertIn("not negative", out.stdout)

    def test_eof_has_no_traceback(self):
        out = self.run_script("")
        self.assertEqual(out.returncode, 1)
        self.assertNotIn("Traceback", out.stderr)


if __name__ == "__main__":
    unittest.main()
