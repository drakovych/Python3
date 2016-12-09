winner_map = {1: (2, 3, 4, 5, 6, 7, 8),
              2: (3, 4, 5, 6, 7, 8, 9),
              3: (4, 5, 6, 7, 8, 9, 10),
              4: (5, 6, 7, 8, 9, 10, 11),
              5: (6, 7, 8, 9, 10, 11, 12),
              6: (7, 8, 9, 10, 11, 12, 13),
              7: (8, 9, 10, 11, 12, 13, 14),
              8: (9, 10, 11, 12, 13, 14, 15),
              9: (10, 11, 12, 13, 14, 15, 1),
              10: (11, 12, 13, 14, 15, 1, 2),
              11: (12, 13, 14, 15, 1, 2, 3),
              12: (13, 14, 15, 1, 2, 3, 4),
              13: (14, 15, 1, 2, 3, 4, 5),
              14: (15, 1, 2, 3, 4, 5, 6),
              15: (1, 2, 3, 4, 5, 6, 7)
              }
choice_map = {1: 'Камень',
              2: 'Огонь',
              3: 'Ножницы',
              4: 'Змея',
              5: 'Человек',
              6: 'Дерево',
              7: 'Волк',
              8: 'Губка',
              9: 'Бумага',
              10: 'Воздух',
              11: 'Вода',
              12: 'Дракон',
              13: 'Дьявол',
              14: 'Молния',
              15: 'Пистолет'
              }
rules = {'Камень побеждает': ('Огонь', 'Ножницы', 'Змею', 'Человека', 'Дерево', 'Волка', 'Губку'),
'Огонь побеждает': ('Ножницы', 'Змею', 'Человека', 'Дерево', 'Волка', 'Губку', 'Бумагу'),
'Ножницы побеждают': ('Змею', 'Человека', 'Дерево', 'Волка', 'Губку', 'Бумагу', 'Воздух'),
'Змея побеждает': ('Человека', 'Дерево', 'Волка', 'Губку', 'Бумагу', 'Воздух', 'Воду'),
'Человек побеждает': ('Дерево', 'Волка', 'Губку', 'Бумагу', 'Воздух', 'Воду', 'Дракона'),
'Дерево побеждает': ('Волка', 'Губку', 'Бумагу', 'Воздух', 'Воду', 'Дракона', 'Дьявола'),
'Волк побеждает': ('Губку', 'Бумагу', 'Воздух', 'Воду', 'Дракона', 'Дьявола', 'Молнию'),
'Губка побеждает': ('Бумагу', 'Воздух', 'Воду', 'Дракона', 'Дьявола', 'Молнию', 'Пистолет'),
'Бумага побеждает': ('Воздух', 'Воду', 'Дракона', 'Дьявола', 'Молнию', 'Пистолет', 'Камень'),
'Воздух побеждает': ('Воду', 'Дракона', 'Дьявола', 'Молнию', 'Пистолет', 'Камень', 'Огонь'),
'Вода побеждает': ('Дракона', 'Дьявола', 'Молнию', 'Пистолет', 'Камень', 'Огонь', 'Ножницы'),
'Дракон побеждает': ('Дьявола', 'Молнию', 'Пистолет', 'Камень', 'Огонь', 'Ножницы', 'Змею'),
'Дьявол побеждает': ('Молнию', 'Пистолет', 'Камень', 'Огонь', 'Ножницы', 'Змею', 'Человека'),
'Молния побеждает': ('Пистолет', 'Камень', 'Огонь', 'Ножницы', 'Змею', 'Человека', 'Дерево'),
'Пистолет побеждает': ('Камень', 'Огонь', 'Ножницы', 'Змею', 'Человека', 'Дерево', 'Волка')}