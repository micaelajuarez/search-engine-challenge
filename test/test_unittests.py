import unittest

# Unit tests for classes
import search_engine_classes as sec


class TestPaths(unittest.TestCase):
	def test_add_path_to_instance_and_get_correct_list(self):
		path = ["/test/path/"]
		paths = sec.Paths()
		paths.add_path(path[0])

		self.assertEqual(paths.get(), path)

	def test_add_many_paths_individually_to_instance_and_get_correct_list(self):
		aux_paths = [str(i) for i in range(0, 200)]
		paths = sec.Paths()

		for path in aux_paths:
			paths.add_path(path)

		self.assertEqual(paths.get(), aux_paths)

	def test_add_paths_instance_to_an_empty_one_and_get_correct_list(self):
		aux_paths = [str(i) for i in range(0, 200)]
		paths1 = sec.Paths()

		for path in aux_paths:
			paths1.add_path(path)

		paths2 = sec.Paths()
		paths2.add_paths(paths1)

		self.assertEqual(paths2.get(), aux_paths)

	def test_add_empty_paths_instance_to_non_empty_one_and_get_correct_list(self):
		aux_paths = [str(i) for i in range(0, 200)]
		paths1 = sec.Paths()

		for path in aux_paths:
			paths1.add_path(path)

		paths2 = sec.Paths()
		paths1.add_paths(paths2)

		self.assertEqual(paths1.get(), aux_paths)

	def test_add_empty_paths_instance_to_another_empty_one_and_get_correct_list(self):
		paths1 = sec.Paths()
		paths2 = sec.Paths()
		paths2.add_paths(paths1)

		self.assertEqual(paths2.get(), [])


class TestWords(unittest.TestCase):
	def test_words_from_whitespace_character_return_empty_list(self):
		self.assertEqual(sec.Words(" ").get(), [])

	def test_words_from_text_with_no_letters_return_empty_list(self):
		self.assertEqual(sec.Words("  %#$#!--- -- -!!$12312::.3").get(), [])

	def test_words_from_text_return_correct_list(self):
		test_list = ["hi", "how", "are", "you", "doing", "today"]
		self.assertEqual(sec.Words("hi how are you doing today").get(), test_list)

	def test_words_from_text_with_symbols_return_correct_list(self):
		test_list = ["hi", "how", "are", "you", "doing", "today"]
		self.assertEqual(sec.Words("  hi%#$ how#!--- are -- -!!$1 2you3 12:doing:   .3today").get(), test_list)


if __name__ == '__main__':
	unittest.main()
