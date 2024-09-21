import xml.etree.ElementTree as ET

def save_to_xml(data, filename):
    import xml.etree.ElementTree as ET

    # Создаем корневой элемент XML с тегом 'data'
    root = ET.Element('data')

    movies = ET.SubElement(root, 'movies')
    for movie in data['movies']:
        # Для каждого фильма создаем элемент 'movie'
        movie_element = ET.SubElement(movies, 'movie')
        
        # Добавляем подэлементы для каждого свойства фильма 
        for key, value in movie.items():
            child = ET.SubElement(movie_element, key)
            child.text = str(value)  # Преобразуем значение в строку и добавляем в элемент

    tvseries = ET.SubElement(root, 'tvseries')
    for series in data['tvseries']:

        series_element = ET.SubElement(tvseries, 'series')
        
        for key, value in series.items():
            child = ET.SubElement(series_element, key)
            child.text = str(value)  

    # Создаем дерево XML и записываем его в файл
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

    print(f"Данные успешно сохранены в файл '{filename}'")

def load_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except FileNotFoundError:
        return {"movies": [], "tvseries": []}

    data = {"movies": [], "tvseries": []}
    
    for movie in root.find('movies'):
        movie_data = {}
        for child in movie:
            movie_data[child.tag] = child.text
        data['movies'].append(movie_data)

    for series in root.find('tvseries'):
        series_data = {}
        for child in series:
            series_data[child.tag] = child.text
        data['tvseries'].append(series_data)

    return data

def add_movie(data, movie):
    data['movies'].append(movie.to_dict())

def add_tvseries(data, tvseries):
    data['tvseries'].append(tvseries.to_dict())

def delete_movie(data, title):
    # Тут мем в том что я создаю 2й список просто в нем нет 1го удаленного XD
    upd = []
    for movie in data['movies']:
        if movie['title'] != title:
            upd.append(movie)
    
    data['movies'] = upd

def delete_tvseries(data, title):
    upd_ser = []
    
    for series in data['tvseries']:
        if series['title'] != title:
            upd_ser.append(series)
    
    data['tvseries'] = upd_ser