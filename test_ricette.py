import pathlib
import unittest

RICETTE = pathlib.Path(__file__).parent / "ricette"


class TestRicette(unittest.TestCase):
    def test_ogni_ricetta_ha_titolo_e_ingredienti(self):
        file = sorted(RICETTE.glob("*.md"))
        self.assertTrue(file, "nessuna ricetta trovata")
        for ricetta in file:
            with self.subTest(ricetta=ricetta.name):
                testo = ricetta.read_text(encoding="utf-8")
                self.assertTrue(testo.startswith("# "), "manca il titolo")
                self.assertIn("## Ingredienti", testo)


if __name__ == "__main__":
    unittest.main()