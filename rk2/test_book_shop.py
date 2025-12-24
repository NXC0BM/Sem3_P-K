import unittest
from book_shop import Book, BookShop, BookShopLink, get_one_to_many, get_many_to_many, task_a1, task_a2, task_a3

shops = [
    BookShop(1, "Читай-город"),
    BookShop(2, "Лабиринт"),
    BookShop(3, "Книжный дом"),
    BookShop(4, "Дом книги"),
    BookShop(5, "Буквоед")
]

books = [
    Book(1, "Преступление и наказание", 500, 1),
    Book(2, "Мастер и Маргарита", 650, 2),
    Book(3, "Война и мир", 800, 3),
    Book(4, "Отцы и дети", 450, 3),
    Book(5, "Евгений Онегин", 400, 3),
    Book(6, "Герой нашего времени", 550, 1)
]

book_shop_links = [
    BookShopLink(1, 1),
    BookShopLink(2, 2),
    BookShopLink(3, 3),
    BookShopLink(3, 4),
    BookShopLink(3, 5),
    BookShopLink(1, 6),
    BookShopLink(4, 1),
    BookShopLink(4, 3),
    BookShopLink(5, 2),
    BookShopLink(5, 5)
]

class TestBookShop(unittest.TestCase):
    def setUp(self):
        self.one_to_many = get_one_to_many(shops, books)
        self.many_to_many = get_many_to_many(shops, books, book_shop_links)

    def test_one_to_many_length(self):
        self.assertEqual(len(self.one_to_many), 6)

    def test_many_to_many_length(self):
        self.assertEqual(len(self.many_to_many), 10)

    def test_one_to_many_contains_correct_shop(self):
        shop_names = [item[2] for item in self.one_to_many]
        self.assertIn("Читай-город", shop_names)
        self.assertIn("Книжный дом", shop_names)

    def test_task_a2_calculation(self):
        from book_shop import task_a2
        one_to_many = get_one_to_many(shops, books)
        res = []
        for s in shops:
            s_books = list(filter(lambda i: i[2] == s.name, one_to_many))
            if len(s_books) > 0:
                s_prices = [price for _, price, _ in s_books]
                s_prices_sum = sum(s_prices)
                res.append((s.name, s_prices_sum))
        for name, total in res:
            if name == "Книжный дом":
                self.assertEqual(total, 1650)
                break

    def test_task_a3_filter(self):
        from book_shop import task_a3
        result = {}
        for s in shops:
            if 'дом' in s.name.lower():
                s_books = list(filter(lambda i: i[2] == s.name, self.many_to_many))
                s_book_titles = [title for title, _, _ in s_books]
                result[s.name] = s_book_titles
        self.assertIn("Книжный дом", result)
        self.assertIn("Дом книги", result)
        self.assertNotIn("Буквоед", result)

if __name__ == '__main__':
    unittest.main()