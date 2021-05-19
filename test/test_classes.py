import unittest
import search_engine as se

# Unit tests for classes Words, Paths, Index


class TestIndex(unittest.TestCase):
	# TODO: update test, it's deprecated
	def test_one_word_one_path_returns_correct_value(self):
		index = se.Index()
		index.add("test word", "test_textfile.txt")
		self.assertEqual(index.add("test word", "test_textfile.txt"), "test_textfile.txt")


if __name__ == '__main__':
	unittest.main()
