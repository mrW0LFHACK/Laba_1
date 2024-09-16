import json_handler
import xml_handler
from media import Movie, TVSeries
# Добавь функции в класс
def get_positive_int(x):
    while True:
        try:
            value = int(input(x))
            if value > 0:
                return value
            else:
                print("Число должно быть положительным.")
        #except Exception: 
        #    print("Пожалуйста, введите целое число.")
        except Exception as e: 
            print(e)

def get_year(x):
    while True:
        try:
            year = int(input(x))
            if 1895 <= year <= 2024:
                return year
            else:
                print("Год должен быть в диапазоне от 1895 до 2024.")
        except Exception as e: 
            print(e)
#       except Exception: 
#           print("Пожалуйста, введите целое число.")
            
def print_data(data, file_format):
    if file_format == 'json':
        print("\nДанные из JSON:")
    elif file_format == 'xml':
        print("\nДанные из XML:")
    
    print("\nФильмы:")
    for movie in data['movies']:
        print(f"Название: {movie['title']}, Режиссер: {movie['director']}, Год: {movie['year']}, Длительность: {movie['duration']} мин.")

    print("\nСериалы:")
    for series in data['tvseries']:
        print(f"Название: {series['title']}, Режиссер: {series['director']}, Год: {series['year']}, Сезонов: {series['seasons']}, Эпизодов: {series['episodes']}")

def sync_data(json_data, xml_data):    
    json_movies = {} 
    for movie in json_data['movies']:  
            title = movie['title'] 
            json_movies[title] = movie  

    xml_movies = {}  
    for movie in xml_data['movies']: 
        title = movie['title']  
        xml_movies[title] = movie  

    for title, movie in json_movies.items():
        if title not in xml_movies:
            print(f"Добавляем фильм '{title}' в XML из JSON.")
            xml_data['movies'].append(movie)

    for title, movie in xml_movies.items():
        if title not in json_movies:
            print(f"Добавляем фильм '{title}' в JSON из XML.")
            json_data['movies'].append(movie)

    json_tvseries = {} 
    for series in json_data['tvseries']: 
        title = series['title']  
        json_tvseries[title] = series 

    xml_tvseries = {} 
    for series in xml_data['tvseries']: 
        title = series['title']  
        xml_tvseries[title] = series  

    for title, series in json_tvseries.items():
        if title not in xml_tvseries:
            print(f"Добавляем сериал '{title}' в XML из JSON.")
            xml_data['tvseries'].append(series)

    for title, series in xml_tvseries.items():
        if title not in json_tvseries:
            print(f"Добавляем сериал '{title}' в JSON из XML.")
            json_data['tvseries'].append(series)

def main():
    print("Выберите формат файла (json/xml):")
    file_format = input().lower()
    filename_json = 'data.json'
    filename_xml = 'data.xml'
    if file_format == 'json':
        filename = 'data.json'
        data = json_handler.load_from_json(filename)
        handler = json_handler
    elif file_format == 'xml':
        filename = 'data.xml'
        data = xml_handler.load_from_xml(filename)
        handler = xml_handler
    else:
        print("Неверный формат!")
        return

    counter = 0 

    while True:
        print("\nВыберите действие:")
        print("1 - Добавить фильм")
        print("2 - Добавить сериал")
        print("3 - Удалить фильм")
        print("4 - Удалить сериал")
        print("5 - Сохранить")
        print("6 - Выход")
        print("7 - Сравнить и синхронизировать JSON и XML")
        print("13 - Вывести данные из JSON")
        print("169 - Вывести данные из XML")

        action = input().strip()

        if action == '1':
            title = input("Введите название фильма: ")
            director = input("Введите режиссера фильма: ")
            year = get_year("Введите год выпуска фильма: ")
            duration = get_positive_int("Введите длительность фильма (в минутах): ")
            movie = Movie(title, director, year, duration)
            handler.add_movie(data, movie)

        elif action == '2':
            title = input("Введите название сериала: ")
            director = input("Введите режиссера сериала: ")
            year = get_year("Введите год выпуска сериала: ")
            seasons = get_positive_int("Введите количество сезонов: ")
            episodes = get_positive_int("Введите количество эпизодов: ")
            tvseries = TVSeries(title, director, year, seasons, episodes)
            handler.add_tvseries(data, tvseries)

        elif action == '3':
            title = input("Введите название фильма для удаления: ")
            handler.delete_movie(data, title)

        elif action == '4':
            title = input("Введите название сериала для удаления: ")
            handler.delete_tvseries(data, title)

        elif action == '5':
            json_handler.save_to_json(data, filename_json)
            xml_handler.save_to_xml(data, filename_xml)
            print(f"Данные сохранены в {filename_json} и {filename_xml}")

        elif action == '6':
            break

        elif action == '7':
            json_data = json_handler.load_from_json('data.json')
            xml_data = xml_handler.load_from_xml('data.xml')
            sync_data(json_data, xml_data)
            json_handler.save_to_json(json_data, 'data.json')
            xml_handler.save_to_xml(xml_data, 'data.xml')
            print("Данные успешно синхронизированы и сохранены в оба файла.")

        elif action == '13':
            if file_format != 'json':
                print("Неверный формат! Вы выбрали XML, а пытаетесь открыть JSON.")
            else:     
                print_data(data, file_format)

        elif action == '169':
            if file_format != 'xml':
                counter += 1
                if counter == 1:
                    print("Бывает, промахнулся, ничего страшного.")
                elif counter ==2:
                    print("Чумба, попей колесики.")
                else:
                    print("Ты меня пугаешь...неужели ты не понял что вообще нет смысла в разделении... и ничего мне не мешало немного изменить код? Я просто хотел хоть где то оставить свою лепту, ибо меняя названия переменных я бы потом вообще не понял, а где что....")
            else:     
                print_data(data, file_format)

        else:
            print("Неверная команда!")

if __name__ == "__main__":
    main()
