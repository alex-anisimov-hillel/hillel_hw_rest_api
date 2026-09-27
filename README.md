# Book Shop

Django-застосунок інтернет-магазину книг з кошиком на сесіях, оформленням
замовлень та оплатою через Stripe.

## Можливості

- Каталог книг з категоріями (django-mptt), CRUD для книг
- Кошик на сесіях (async views) — додавання/видалення позицій, підрахунок суми
- Оформлення замовлення (гостьове або від імені зареєстрованого користувача)
- Оплата через Stripe: створення `PaymentIntent`, підтвердження оплати,
  email-сповіщення про успішну оплату
- Кастомна модель користувача (email як логін)
- Локалізація (django `gettext`)

## Технології

Django 6.1, Django REST Framework, django-mptt, Stripe, PostgreSQL, Redis,
Uvicorn (ASGI), Docker / docker-compose, pytest / pytest-django / pytest-factoryboy.

## Запуск локально (Docker)

1. Скопіюйте/перевірте `.env` (POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD,
   POSTGRES_HOST, POSTGRES_PORT, а також `STRIPE_SECRET_KEY`/`STRIPE_PUBLIC_KEY`,
   якщо плануєте тестувати оплату).
2. Підняти сервіси:
   ```bash
   docker compose up --build
   ```
   Це підніме Postgres, Redis і сам застосунок (застосує міграції автоматично
   через `entrypoint.sh`) на `http://localhost:8000`.

## Тести та coverage

```bash
pytest
pytest --cov=payment.models --cov=orders.models --cov=users.models --cov-report=term-missing
```

Детальний coverage-звіт (з поясненням, чому саме ці 3 моделі та звідки взяті
цифри) — у `COVERAGE_REPORT.md`.

## AI Usage

У рамках домашнього завдання "Використати AI для покращення проєкту" AI (Claude,
Anthropic) використовувався для трьох задач:

1. **Code review** трьох найскладніших views/serializers проєкту
   (`PaymentViewSet` + `StripePayment`, cart/order views у `orders/views.py`,
   `PaymentSerializer`) — знайдено й виправлено кілька реальних багів (падіння на
   гостьових замовленнях, невідповідність назв полів моделі й серіалізатора,
   втрату `Payment` при переданому `idempotency_key`, відсутню автентифікацію на
   payment-ендпоінтах, мертвий/непрацюючий код у `order_create`). Повний розбір
   "було / рекомендація AI / стало" — у `AI_REVIEW.md`.
2. **Генерація тестів** для моделей `Payment`, `Order`/`OrderItem` та `User` —
   нові тести (позначені коментарем `# Generated with AI, reviewed and modified`)
   цілять саме в раніше непокриту логіку: властивості `is_success`/
   `can_be_refunded`/`remaining_amount`, `OrderItem.get_total()`, і, найважливіше,
   `UserManager.create_user`/`create_superuser` (раніше взагалі не викликались
   жодним тестом, оскільки фабрики `pytest-factoryboy` створюють користувачів в
   обхід менеджера). Детальніше, включно з реальними цифрами покриття "до" (з
   вашого попереднього `.coverage`) — у `COVERAGE_REPORT.md`.
3. **Документація** — docstrings додано до всіх views/viewset-методів проєкту
   (`books/views.py`, `orders/views.py`, `payment/views.py`, `users/views.py`), і
   оновлено цей README.

Повний список промптів, якими виконувалась кожна з трьох задач — у `AI_PROMPTS.md`.
