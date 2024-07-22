import os
import openpyxl as op
import datetime as dt
import sys


class StudySessions:
    def __init__(self,file_location = r"data\SpacingTable.xlsx"):
        script_path = os.path.abspath(__file__) # location of table
        self.file_location = os.path.join(os.path.dirname(script_path),file_location)

        self.table = self.process(self.load())

    def load(self):
        # data = pd.read_excel(self.file_location, engine= "openpyxl")
        # return data

        wb = op.load_workbook(self.file_location)
        data = wb.active

        return data

    def process(self, data):
        table = {} # processed data

        for index,row in enumerate(data.iter_rows(min_row = 2, values_only=True)): # iterate through table
            # collect topic and dates
            topic = row[0]
            dates = list(row[1:])
            colour = []
            difficulty = []

            
            if all(i is None for i in dates): # Remove empty rows
                continue

            if dates[0] == None: # Remove topics without encoded date
                continue

            # collect colours to be turned into difficulty
            for cell in data[index+2]:
                colour.append((cell.fill.fgColor.rgb))

            # remove cells without dates
            dates = [i for i in dates if i != None]
            colour = colour[1:len(dates)+1]

            # convert colours to difficulty
            def colour_to_difficulty(colour):
                if colour == "FFFF0000" or colour == "FFC00000": # red for hard
                    return 2
                elif colour == "FFFFFF00": # yellow for good
                    return 3
                elif colour == "FF00B050" or colour == "FF92D050": # green for easy
                    return 4
                else:
                    print(f"Error: A cell is not coloured for topic {topic}")
                    sys.exit(1)
                    return 2 # default is good
                
            difficulty = [colour_to_difficulty(i) for i in colour]

            # Add UTC timezone to dates as required by FSRS code
            dates = [date.astimezone(dt.timezone.utc) for date in dates] # ensure datetimes are set to UTC as required by FSRS module

            # add topic with data to table
            table[topic] = [dates,difficulty]

        if not table:
            print("Error: No data in spacing table. Please go in the data folder and add your topics to the SpacingTable.xlsx")
            sys.exit(1)
        
        return table

if __name__ == "__main__":
    StudySessions()
