import unittest
import search_engine as se

# Unit tests for classes Words, Paths, Index


class TestPaths(unittest.TestCase):
	def test_add_path_to_instance_and_get_correct_list(self):
		path = ["/test/path/"]
		paths = se.Paths()
		paths.add_path(path[0])

		self.assertEqual(paths.get(), path)

	def test_add_many_paths_individually_to_instance_and_get_correct_list(self):
		aux_paths = [str(i) for i in range(0, 200)]
		paths = se.Paths()

		for path in aux_paths:
			paths.add_path(path)

		self.assertEqual(paths.get(), aux_paths)

	def test_add_paths_instance_to_an_empty_one_and_get_correct_list(self):
		aux_paths = [str(i) for i in range(0, 200)]
		paths1 = se.Paths()

		for path in aux_paths:
			paths1.add_path(path)

		paths2 = se.Paths()
		paths2.add_paths(paths1)

		self.assertEqual(paths2.get(), aux_paths)

	def test_add_empty_paths_instance_to_non_empty_one_and_get_correct_list(self):
		aux_paths = [str(i) for i in range(0, 200)]
		paths1 = se.Paths()

		for path in aux_paths:
			paths1.add_path(path)

		paths2 = se.Paths()
		paths1.add_paths(paths2)

		self.assertEqual(paths1.get(), aux_paths)

	def test_add_empty_paths_instance_to_another_empty_one_and_get_correct_list(self):
		paths1 = se.Paths()
		paths2 = se.Paths()
		paths2.add_paths(paths1)

		self.assertEqual(paths2.get(), [])


if __name__ == '__main__':
	unittest.main()
