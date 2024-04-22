# Как использовать:


* Сохраните этот файл в директории вашего проекта Django, где находится `manage.py`.

* Запустите _Django shell_ командой:

```shell
python manage.py shell
```

* Импортируйте и используйте функции:

```python
from school_utils import fix_marks, remove_chastisements, create_commendation
fix_marks('Фролов Иван Григорьевич')
remove_chastisements('Голубев Феофан Владленович')
create_commendation('Фролов Иван Григорьевич', 'Музыка')
```

1. `fix_marks` - исправление оценок 2,3 на оценку 5

2. `remove_chastisements` - Удаление замечаний

3. `create_commendation` - создание похвал