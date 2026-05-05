import xml.etree.ElementTree as ET
from pathlib import Path


def parse_xml_file(filename: str = "library.xml"):
    """Парсить XML з файлу і повертає кореневий елемент"""
    filepath =  filename
    tree = ET.parse(filepath)
    return tree


if __name__ == "__main__":
    curr_dir = Path(__file__).parent
    filename = curr_dir / "groups.xml"
    file_xml = parse_xml_file(filename)
    print(file_xml)
    root = file_xml.getroot()
    print(root)
    print(root.tag)
    print(f"Атрибути кореня: {root.attrib}")
    print(f"Текст кореня: {repr(root.text)}")
    print("Дочірні елементи кореня:")
    for child in root:
        print(f"  - {child.tag} (атрибути: {child.attrib})")
        # for subchild in child:
        #     print(f" =- {subchild.tag} (атрибути: {subchild.attrib})")
    
    # find() - знаходить ПЕРШИЙ елемент
    first_book = root.find("book")
    print(f"Перша знайдена книга: {first_book.find('title').text}")

    # findall() - знаходить ВСІ елементи
    all_books = root.findall("book")
    print(f"Кількість книг: {len(all_books)}")

    first_title = root.findtext("book/title")
    print(f"Назва першої книги: {first_title}")
    print("РОБОТА З АТРИБУТАМИ")
    print("=" * 50)

    for book in root.findall("book"):
        book_id = book.get("id")          # get() - безпечний спосіб
        # genre = book.attrib.get("genre")   # через attrib словник
        genre = book.get("genre") # БЕЗ attrib словник
        
        print(f"Книга ID: {book_id}, Жанр: {genre}")
    
    # Пошук на будь-якому рівні вкладеності
    all_names = root.findall(".//name")  # .// означає "будь-де в дереві"
    print("Імена авторів:")
    for name in all_names:
        print(f"  - {name.text}")

    # Пошук з умовами (XPath)
    fiction_books = root.findall(".//book[@genre='fiction']")
    print(f"\nКількість художніх книг: {len(fiction_books)}")

    # Пошук за текстом
    expensive_books = root.findall(".//book[price>200]")
    print(f"Книги дорожче 200 грн: {len(expensive_books)}")