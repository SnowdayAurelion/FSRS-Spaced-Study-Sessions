from StudySessions import StudySessions
from FSRSCalculations import FSRSCalculations
from Graph import Graph
import configparser

class main:
    def __init__(self):
        # Settings
        config = configparser.ConfigParser()
        config.read(r"data\settings.txt")
        parameters = config.get("FSRS", "parameters")
        parameters = [float(i) for i in parameters.split(',')]

        # Main
        self.data = StudySessions().table # Collect raw data from table
        self.processed_data = FSRSCalculations(parameters).process_data(self.data) # Calculate next due dates + other useful info
        
        Graph().graph(self.processed_data)
        

if __name__ == "__main__":
    main()