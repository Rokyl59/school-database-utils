import random
from datacenter.models import Schoolkid, Mark, Chastisement, Commendation, Lesson


def fix_marks(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name=schoolkid_name)
        Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)
        print(f"Оценки исправлены для {schoolkid_name}.")
    except Schoolkid.DoesNotExist:
        print(f"Ученик {schoolkid_name} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def remove_chastisements(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name=schoolkid_name)
        Chastisement.objects.filter(schoolkid=schoolkid).delete()
        print(f"Замечания удалены для {schoolkid_name}.")
    except Schoolkid.DoesNotExist:
        print(f"Ученик {schoolkid_name} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def create_commendation(full_name, subject_title):
    praises = [
        "Отлично поработал на уроке!",
        "Прекрасная работа!",
        "Замечательное внимание к деталям.",
        "Так держать!",
        "Ты много работал, и это приносит результаты!"
    ]
    try:
        schoolkid = Schoolkid.objects.get(full_name=full_name)
        last_lesson = Lesson.objects.filter(
            schoolkid=schoolkid, 
            subject__title=subject_title
        ).order_by('-date').first()

        if not last_lesson:
            print("Не найден урок по заданному предмету.")
            return

        praise_text = random.choice(praises)
        Commendation.objects.create(
            text=praise_text,
            created=last_lesson.date,
            schoolkid=schoolkid,
            subject=last_lesson.subject,
            teacher=last_lesson.teacher
        )
        print("Похвала успешно добавлена.")

    except Schoolkid.DoesNotExist:
        print("Ученик не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
