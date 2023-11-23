#!/usr/bin/env python3

class CashRegister:
   
  def __init__(self, discount_percentage=0):
    self.items = []
    self.total = 0.0
    self.last_transaction_amount = 0.0
    self.discount_percentage = discount_percentage


  def add_item(self, item_name, item_price, quantity=1):
    item_total = item_price * quantity
    self.items.extend([item_name] * quantity)
    self.total += item_total
    self.last_transaction_amount = item_total

  def void_last_transaction(self):
    if self.items:
      self.total -= self.last_transaction_amount
      self.last_transaction_amount = 0.0
    else:
      print("There are no transactions to void.")

  def apply_discount(self):
    discount = float(self.discount_percentage) / 100
    if discount > 0:
      discount_amount = self.total * discount
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${self.total:.2f}.")
    else:
      print("There is no discount to apply.")



