import unittest
import os
import importlib


class TestMethods(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.modules = map(
            lambda x: x[:-3],
            filter(
                lambda x: x.endswith('queue.py'),
                os.listdir('qslib')
            )
        )

    def test_get_all_metric(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                print(m.__name__)
                self.assertIn('get_all_metric', dir(m))
                del m

    def test_get_p0(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_p0', dir(m))

    def test_get_p_k(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_p_k', dir(m))

    def test_get_p_fail(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_p_fail', dir(m))

    def test_get_p_queue(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_p_queue', dir(m))

    def test_get_n_queue(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_n_queue', dir(m))

    def test_get_n_serv(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_n_serv', dir(m))

    def test_get_n_sys(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_n_sys', dir(m))

    def test_get_t_queue(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_t_queue', dir(m))

    def test_get_t_serv(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_t_serv', dir(m))

    def test_get_t_sys(self):
        for module in self.modules:
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                self.assertIn('get_t_sys', dir(m))

    def test_get_t_wait(self):
        print(list(self.modules))
        for module in self.modules:
            print(module)
            with self.subTest(module=module):
                m = importlib.import_module('qslib.' + module)
                print(module)
                self.assertIn('get_t_wait', dir(m))


if __name__ == '__main__':
    unittest.main(verbosity=2)
