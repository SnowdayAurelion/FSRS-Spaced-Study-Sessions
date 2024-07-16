from fsrs import *
from datetime import datetime, timedelta, timezone


class FSRSCalculations:
    def __init__(self, parameters = (0.4000, 0.5100, 1.0000, 2.0000, 1.0000, 0.9400, 0.8600, 0.0100, 1.3900, 0.1400, 0.9400, 2.1800, 0.0500, 0.3400, 1.2600, 0.2500, 1.5200)):
        self.f = FSRS()
        self.f.p.w = parameters # your custom parameters, default are ones I found that work well with iCS
    
    def create_card(self,dates,reviews): # simulates flashcard
        card = Card()
        card.due = dates[0] # initial date encoded

        reviews_dates = zip(reviews,dates) # review difficulty + date reviewed

        for grade, date in reviews_dates:
            scheduling_cards = self.f.repeat(card, date)
            card = scheduling_cards[grade].card

            if (card.state != State.Review):
                card.state = State.Review
                interval = self.f.next_interval(card.stability)
                card.due = date + timedelta(days=interval)

        return card

    def process_data(self,data):
        processed_data = {}

        for topic, sub_data in data.items():
            dates = sub_data[0]
            difficulties = sub_data[1]
            card = self.create_card(dates, difficulties)
            
            new_sub_data = [0 for i in range(5)] # dates, difficulties, due date, days since studied, lapses

            new_sub_data[0] = dates # history of study dates
            new_sub_data[1] = difficulties[-1] # latest difficulty
            new_sub_data[2] = card.due # when next study session is due
            new_sub_data[3] = (card.due - card.last_review).days # days from last study session to due date
            new_sub_data[4] = len(difficulties)-1 # number of retrieval study sessions
            processed_data[topic] = new_sub_data # processed data per topic
            
        return processed_data

        
             
            
