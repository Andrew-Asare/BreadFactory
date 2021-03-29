from Naan_Factory import naan_factory
import unittest


# run_factory()

class test_bread_factory(unittest.TestCase):
    factory = naan_factory()

    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough("water", "flour"), "dough")

    def test_bake_dough(self):
        self.assertEqual(self.factory.bake_dough('dough'), "bread")

    def test_run_factory(self):
        self.assertEqual(self.factory.run_factory("water", "flour"), "naan")