import unittest
from PitcherGame import pitcherGameMinSteps, getData

class TestPitcherGame(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName)
        self.test_data_files = ['test_data1.txt', 'test_data2.txt', 'test_data3.txt']

    def test_pitcher_game_min_steps_file1(self):
        data = getData(self.test_data_files[0])
        result = pitcherGameMinSteps(data)
        expected = 20
        self.assertEqual(result, expected)

    def test_pitcher_game_min_steps_file2(self):
        data = getData(self.test_data_files[1])
        result = pitcherGameMinSteps(data)
        expected = 3
        self.assertEqual(result, expected)

    def test_pitcher_game_min_steps_file3(self):
        data = getData(self.test_data_files[2])
        result = pitcherGameMinSteps(data)
        expected = -1
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()