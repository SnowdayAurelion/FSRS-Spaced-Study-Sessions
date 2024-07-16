import plotly.express as px
import datetime as dt
import pandas as pd

class Graph:
    def __init__(self):
        pass

    def graph(self, data):
        dataframe = []

        for topic, sub_data in data.items():
            row = {
                "Topic": topic,
                "Due": sub_data[2].date(), # Due date
                "Due End": sub_data[2].date() + dt.timedelta(days=1),
                "Difficultly": sub_data[1],
                "Days since last Study": sub_data[3],
                "# of Retrieval Study Sessions": sub_data[4]
            }

            dataframe.append(row)

        data = pd.DataFrame(dataframe)



        # data["Due"] = [i.strftime("%A, %B %d") for i in data["Due"]] # reformatting Due
        data["Difficultly"] = [self.convert_difficulty_to_word(i) for i in data["Difficultly"]]

        fig = px.timeline(data, x_start="Due", x_end="Due End", y="Topic", title="Retrieval Sessions", hover_data=
                    { "Due":True,
                        "Topic":True,
                        "Difficultly":True,
                        "Days since last Study":True,
                        "# of Retrieval Study Sessions":True,
                        "Due End":False})
        # fig.update_xaxes(range=[dt.date(2024,5,8),dt.date(2024,8,12)])
        fig.show()


        # data.to_csv(r"C:\Users\light\Downloads\test.csv")

    def convert_difficulty_to_word(self, difficulty):
        if difficulty == 2:
            return "Hard"
        elif difficulty == 3:
            return "Good"
        else:
            return "Easy"

