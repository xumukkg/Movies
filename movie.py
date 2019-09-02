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
print(movies)
def write_rate():    
    with open('moviesRuslan.txt', 'w') as f:
        for item in movies:
            rate = []
            for mov in item['ratings']:
                v=item['ratings'][mov]
                rate_str = f'{mov},{v}'
                rate.append(rate_str)
            all_rate_str = ';'.join(rate)
            movie_str = f'{item["name"]}|{all_rate_str}\n'
            f.write(movie_str)
write_rate()
def read_rate():
    with open('moviesRuslan.txt', 'r') as f:
        movies = []
        for line in f:
            movie = {}
            name, rate_str = line.strip().split("|")
            if rate_str =='':
                rate_str={}
                rate = rate_str
                movie['name']= name
                movie['ratings'] = rate
            else:
                new_rate_str = rate_str.split(';')
                rate = {}
                for i in new_rate_str:
                    elements = i.split(',')
                    rate[elements[0]]=int(elements[1])
                movie['name']= name
                movie['ratings'] = rate
            movies.append(movie)
        print(movies)
read_rate()
def read():
    with open('movies.txt', 'r') as f:
        mrt = {}
        for line in f:
          movie_name, ratings = line.strip().split('|')
          if ratings == '':
            rating = [] 
          else:
            rating = ratings.strip().split(';')
          mrt = {}
          for item in rating:
            user_name, mark = item.split(',')
            mrt.update({
                user_name: float(mark)
            })
          movies.append({
            'name': movie_name,
            'ratings': mrt
          })

def write(movies):
    with open('movies.txt', 'w') as f:
        for item in movies:
            d = []
            for mov in item['ratings']:
                v = item['ratings'][mov]
                movie_str = f'{mov},{v}'
                d.append(movie_str)
            all_mov_str = ';'.join(d)
            movic_str = f'{item["name"]}|{all_mov_str}\n'
            f.write(movic_str)

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
        # del movie # не работает
        # del movies[0] # работает, но нужно знать индекс
        movies.remove(movie)
        print("Фильм удалён")
    else:
        print('Фильм не найден')

print("""    Команды:
* list - показать список Фильм
* find - найти Фильм по имени
* add - добавить  в книгу
* edit - поменять данные контакта
* delete - удалить контакт
* help - показать список команд
* exit - выход.""")


def handle_command(command):
    if command == 'list':
        list_contacts()
    elif command == 'find':
        show_contact(movies)
    elif command == 'add':
        add_contact(movies)
    elif command == 'edit':
        edit_contact(movies)
    elif command == 'delete':
        delete_contact(movies)
        write(movies)
    elif command == 'help':
        help()
    else:
        print("Неизвестная команда.")


def main():
    print("Добро пожаловать в телефонную книгу!")
    help()
    while True:
        command = nice_input("\nВведите команду")
        if command == 'exit':
            print("Выход")
            break
        else:
            
            handle_command(command)


main()



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
