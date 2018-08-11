# これはexampleです

from unittest import TestCase
from scripts.foo import Foo

class TestFoo(TestCase):

    def test_say(self):
        self.assertEqual(Foo.say(self), 'foo')