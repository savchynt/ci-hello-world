import sys
import unittest

sys.path.append('.')  # for units tests
from src.hello import hello


class TestHello(unittest.TestCase):
    def test_type(self):
        output = hello.hello()
        self.assertIsInstance(output, str, 'Wrong type!')

    def test_content(self):
        greetings = 'Hello'
        subject = 'World'
        output = hello.hello()
        self.assertIn(greetings, output, 'You should Say Hello!')
        self.assertIn(subject, output, 'Say Hello to the World!')

    def test_grammar(self):
        output = hello.hello()
        self.assertIn('!', output, "Use '!' in Greetings!")


if __name__ == '__main__':
    unittest.main()
