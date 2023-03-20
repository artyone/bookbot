
BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    marks = [',', '!', ':', ';', '?', '.']
    end = start + size
    if end >= len(text):
        part_text = text[start:]
    else:
        for i in range(end - 1, start - 1, -1):
            if text[i] in marks and text[i + 1] not in marks:
                part_text = text[start: i + 1]
                break
    return (part_text, len(part_text))


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf8') as file:
        read_size = PAGE_SIZE + 1
        page = file.read(read_size)
        counter = 1
        while page:
            text, length = _get_part_text(page, 0, PAGE_SIZE)
            book[counter] = text.strip()
            page = page[length:] + file.read(read_size - (read_size - length))
            counter += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)


