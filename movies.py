movies = [
    {
        'name': 'Interstellar',
        'ratings': {
            'John': 10,
            'Jack': 3
        }
    },
    {
        'name': 'Avengers: Infinity War',
        'ratings': {
            'Jack': 9,
            'Jane': 10,
        }
    },
    {
        'name': 'Matrix',
        'ratings': { }
    }
]

def get_avg_rating(item):
    average = get_avg_rating_as_float(item)
    if average > 0:
        return str(average)
    return 'Без рейтинга'

def get_avg_rating_as_float(item):
    if len(item['ratings']) > 0:
        average = sum(item['ratings'].values()) / len(item['ratings'])
        return average
    return 0

def list(movies):
    for item in movies:
        average = get_avg_rating(item)
        print(f"{item['name']:<25} {average:>14}")

def sort(movies):
    sorted_movies = sorted(movies, key=get_avg_rating_as_float)
    sorted_movies.reverse()
    list(sorted_movies) 

def find(movies, name=None):
    if not name:
        name = input("Введите название фильма:\n> ")
    for item in movies:
        if item['name'] == name:
            return item
    return None

def show(movies):
    movie = find(movies)
    if movie:
        print(f"{movie['name']:^35}")
        for key, value in movie['ratings'].items():
            print(f"{key:<20} {value:>14.1f}")
        average = get_avg_rating(movie)
        print(f"{'Средний рейтинг':<20} {average:>14}")
    else:
        print("Фильм не найден")

def add(movies):
    name = input("Введите название фильма:\n> ")
    movie = find(movies, name)
    if not movie:
        new_movie = {'name': name, 'ratings': {}}
        movies.append(new_movie)
        print("Фильм добавлен!")
    else:
        print("Такой фильм уже есть.")

def rate(movies):
    movie = find(movies)
    if movie is not None:
        name = input("Введите ваше имя:\n> ")
        rating = float(input("Введите рейтинг:\n> "))
        if rating == 0:
            if movie['ratings'].get(name):
                movie['ratings'].pop(name)
        elif rating < 1 or rating > 10:
            print("Рейтинг должен быть от 1 до 10!")
        else:
            movie['ratings'][name] = rating

def delete(movies):
    movie = find(movies)
    if movie is not None:
        movies.remove(movie)
        print("Фильм удалён")
    else:
        print('Фильм не найден')


# list(movies)
# rate(movies)
# show(movies)
# sort(movies)
# add(movies)
# list(movies)
# show(movies)
# delete(movies)
# list(movies)


# movies = load_movies()
# while True:
    # ...
    # if command == 'add':
    #     add(movies)
    #     save_movies()
    # ...


# А можно будет разобрать второе задание из домашки?
# С телефонной книгой проблем не было, 
# а вот с фильмами только запись получилось сделать
