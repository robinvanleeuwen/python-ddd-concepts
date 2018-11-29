import uuid
from datetime import datetime
from typing import List

from domain.entities import AuctionItem
from domain.value_objects import Currency


class AuctionItemsRepository:
    items = []
    def add(self, title, description, starting_price, end_date):
        id = uuid.uuid4().hex
        current_datetime = datetime.now()
        self.items.append((id, AuctionItem(id=id, title=title, description=description, starting_price=starting_price, start_date=current_datetime, end_date=end_date)))

    def get_all(self):
        return list(map(lambda item: item[1], self.items))