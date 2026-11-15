import importlib.util
import tempfile
import unittest
from pathlib import Path

source = Path(__file__).parent / "processar_fotos.py"
spec = importlib.util.spec_from_file_location("wmk", source)
wmk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wmk)

class Tests(unittest.TestCase):
    def test_plano(self):
        with tempfile.TemporaryDirectory() as temp:
            a = Path(temp) / "originais"
            a.mkdir()
            (a / "foto.png").write_bytes(b"x")
            b = Path(temp) / "resultado"
            self.assertEqual(wmk.planejar(a, b, "webp")[0][1], b / "foto.webp")
            self.assertFalse(b.exists())
    def test_recusa_sobrescrever(self):
        with tempfile.TemporaryDirectory() as temp:
            a = Path(temp) / "originais"
            a.mkdir()
            (a / "foto.png").touch()
            with self.assertRaises(ValueError):
                wmk.planejar(a, a / "saida", "webp")
    def test_recusa_colisao(self):
        with tempfile.TemporaryDirectory() as temp:
            a = Path(temp) / "originais"
            a.mkdir()
            (a / "foto.png").touch()
            (a / "foto.jpg").touch()
            with self.assertRaises(ValueError):
                wmk.planejar(a, Path(temp) / "saida", "webp")

if __name__ == "__main__":
    unittest.main()
