def ticket_informathion(number_of_ticket):
      ticket_price = 0
      sum_price = list()
      for i in range(number_of_tickets):
            age = int(input('Введите возраст посетителя: '))
            if 0 <= age < 18:
                  ticket_price = 0
            elif 18 <= age < 25:
                  ticket_price = 990
            else:
                  ticket_price = 1390
            sum_price += [ticket_price]
      return sum(sum_price)
number_of_tickets = int(input('Введите количество билетов: '))
price = ticket_informathion(number_of_tickets)
discount = 0
if number_of_tickets >= 3:
      discount = int(price - price*0.1)
      print('Вы получили скидку 10%')
      print('Стоимость билетов: ',discount, 'руб.')
else:
      print('Стоимость билетов: ', price, 'руб.')

