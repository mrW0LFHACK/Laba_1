import xml.etree.ElementTree as ET

# Функция для добавления отступов (pretty-print)
def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def save_to_xml(data, filename):
    root = ET.Element('data')

    movies = ET.SubElement(root, 'movies')
    for movie in data['movies']:
        movie_element = ET.SubElement(movies, 'movie')
        for key, value in movie.items():
            child = ET.SubElement(movie_element, key)
            child.text = str(value)  

    tvseries = ET.SubElement(root, 'tvseries')
    for series in data['tvseries']:
        series_element = ET.SubElement(tvseries, 'series')
        for key, value in series.items():
            child = ET.SubElement(series_element, key)
            child.text = str(value)  
    indent(root)

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
