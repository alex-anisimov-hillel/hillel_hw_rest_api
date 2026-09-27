from pytest_factoryboy import register
from book_shop.factory.factories import CategoryFactory, BookFactory, UserFactory, PaymentFactory, OrderFactory


register(CategoryFactory)
register(BookFactory)
register(UserFactory)
register(PaymentFactory)
register(OrderFactory)