from models import Card
from threads import Transaction

print(f'Начальный баланс - {Card.balance}')
card1 = Card(1234, 'Коля Колин')
card2 = Card(5678, 'Иван Иванов')

tran1 = Transaction(550000, card1)