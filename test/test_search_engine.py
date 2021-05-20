import search_engine
import unittest

TEST_PATH = "/home/micaelita/PycharmProjects/search-engine-challenge/test/textfiles"

# Integration tests


class TestSearchEngine(unittest.TestCase):
	# TODO: update test, it's deprecated
	def test_one_word_input_is_found_returns_true(self):
		self.assertEqual(search_engine.main(TEST_PATH, "dynamite"), True)

	# TODO: update test, it's deprecated
	def test_one_word_input_is_not_found_returns_false(self):
		self.assertEqual(search_engine.main(TEST_PATH, "asdfghjklqwerty"), False)


if __name__ == '__main__':
	unittest.main()
