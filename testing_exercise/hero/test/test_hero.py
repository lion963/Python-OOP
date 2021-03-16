from testing_exercise.hero.project.hero import Hero
import unittest


class HeroTests(unittest.TestCase):

    def __get_exception(self, player, enemy):
        with self.assertRaises(Exception) as context:
            player.battle(enemy)
        return context.exception

    def test_attributes_equal(self):
        params_player = ['Asen', 0, 100.0, 10.0]
        player = Hero(*params_player)
        result = [player.username, player.level, player.health, player.damage]
        expected_result = ['Asen', 0, 100.0, 10.0]
        self.assertListEqual(result, expected_result)

    def test_battle_method_enemy_username_equal_username(self):
        params_enemy = ['Asen', 0, 100.0, 10.0]
        enemy = Hero(*params_enemy)
        params_player = ['Asen', 0, 100.0, 10.0]
        player = Hero(*params_player)
        exception = self.__get_exception(player, enemy)
        self.assertIsNotNone(exception)

    def test_health_below_zero(self):
        params_enemy = ['Nikolay', 0, 100.0, 10.0]
        enemy = Hero(*params_enemy)
        params_player = ['Asen', 0, -1, 10.0]
        player = Hero(*params_player)
        exception = self.__get_exception(player, enemy)
        self.assertIsNotNone(exception)

    def test_health_equal_zero(self):
        params_enemy = ['Nikolay', 0, 100.0, 10.0]
        enemy = Hero(*params_enemy)
        params_player = ['Asen', 0, 0, 10.0]
        player = Hero(*params_player)
        exception = self.__get_exception(player, enemy)
        self.assertIsNotNone(exception)

    def test_enemy_health_below_zero(self):
        params_enemy = ['Nikolay', 0, -1, 10.0]
        enemy = Hero(*params_enemy)
        params_player = ['Asen', 0, 100.0, 10.0]
        player = Hero(*params_player)
        exception = self.__get_exception(player, enemy)
        self.assertIsNotNone(exception)

    def test_enemy_health_equal_zero(self):
        params_enemy = ['Nikolay', 0, 0, 10.0]
        enemy = Hero(*params_enemy)
        params_player = ['Asen', 0, 100.0, 10.0]
        player = Hero(*params_player)
        exception = self.__get_exception(player, enemy)
        self.assertIsNotNone(exception)

    def test_battle_method_draw(self):
        params_enemy = ['Nikolay', 2, 10.0, 10.0]
        enemy = Hero(*params_enemy)
        params_player = ['Asen', 2, 10.0, 10.0]
        player = Hero(*params_player)
        result = player.battle(enemy)
        expected_result = 'Draw'
        self.assertEqual(result, expected_result)

    def test_battle_method_win(self):
        params_enemy = ['Nikolay', 2, 10.0, 10.0]
        enemy = Hero(*params_enemy)
        params_player = ['Asen', 2, 100.0, 10.0]
        player = Hero(*params_player)
        msg = player.battle(enemy)
        result = [player.level, player.health, player.damage, msg]
        expected_result = [3, 85.0, 15.0, 'You win']
        self.assertListEqual(result, expected_result)

    def test_battle_method_lose(self):
        params_enemy = ['Nikolay', 2, 30.0, 10.0]
        enemy = Hero(*params_enemy)
        params_player = ['Asen', 2, 100.0, 10.0]
        player = Hero(*params_player)
        msg = player.battle(enemy)
        result = [enemy.level, enemy.health, enemy.damage, msg]
        expected_result = [3, 15.0, 15.0, 'You lose']
        self.assertListEqual(result, expected_result)

    def test__str__method(self):
        params_enemy = ['Nikolay', 2, 30.0, 10.0]
        enemy = Hero(*params_enemy)
        params_player = ['Asen', 2, 100.0, 10.0]
        player = Hero(*params_player)
        result = str(player)
        expected_result = 'Hero Asen: 2 lvl\nHealth: 100.0\nDamage: 10.0\n'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
