# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1 as r1
import room_2 as r2

print()

rooms = [
    {r1.__name__: r1.folks},
    {r2.__name__: r2.folks}
]
for room in rooms:
    for room_name, folks in room.items():
        print('В комнате', room_name, 'живут:')
        for folk in folks:
            print(folk)
