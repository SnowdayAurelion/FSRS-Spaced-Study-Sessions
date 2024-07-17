# FSRS Spaced Study Sessions
## Usage
### Topic Encoded
Open the `data` folder to access your `SpacingTable.xlsx`. Under **Topic**, write your topics per row. Under **Encoded**, write the date when you first learned the topic. A topic could be considered encoded after covering it in a lecture or from a self-study session. Use the `CTRL + ;` hotkey to insert a date.

Then rate your confidence in the study session by highlighting the cell using Excel's standard colors:

![image](https://github.com/user-attachments/assets/14cf9c1a-75eb-4de2-91bd-074c50b45d2e)

- Green for Easy
- Yellow for Good
- Red for Hard

To see the recommended due date for your next review, run `run.bat` to generate a Gantt chart of all your topics. Hover over the interactive graph to see due date and additional data.

### Retrieval Study Sessions
When you review your topic, open `SpacingTable.xlsx` again to add a date next to the previous date. Add the date using the hotkey and make sure to rate it by highlighting.

If confused, refer to `SpacingTable Example.xlsx` in the `data` folder.

### Custom Parameters
The code uses the [FSRS Algorithm](https://github.com/open-spaced-repetition/py-fsrs), which spaces the retrieval sessions based on difficulty and review date. I have customized the parameters to follow an approximately 1-7-30 review day pattern. This spacing is inspired by [iCanStudy](icanstudy.com), which is part of why I created the code to help the iCS community. 

The see the intervals based on a specific combination of sequential study sessions, open [FSRS Visualizer](https://open-spaced-repetition.github.io/anki_fsrs_visualizer/) and paste my default parameter to replace the horizontal list of numbers directly over the "Reset parameters" button.
```
0.4000, 0.5100, 1.0000, 2.0000, 1.0000, 0.9400, 0.8600, 0.0100, 1.3900, 0.1400, 0.9400, 2.1800, 0.0500, 0.3400, 1.2600, 0.2500, 1.5200
```
You may hover over a point to see how many days after the study session until you should retrieve.

To customize your parameters, use the [FSRS Visualizer](https://open-spaced-repetition.github.io/anki_fsrs_visualizer/) and copy the list of numbers and paste into `settings.txt` in the `data` folder.

## Install
### Prerequisties
- [Python](https://www.python.org/downloads/)

### Instructions
#### Windows
1. Download this GitHub respository by [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or download it as a ZIP.
2. Double click `setup_Windows.bat` to install virtual Python environment and dependencies.
3. To run the code, double click `run.bat`. You can make this as a short-cut for easier access.

#### Mac
1. Download this GitHub respository by [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or download it as a ZIP.
2. Open a terminal and navigate to project's directory. Run the lines below:
```sh
chmod +x setup_Mac.sh
./setup_Mac.sh
```
3. To run the code, open a terminal and navigate to the project's directory and run the lines below:
```sh
chmod +x run.sh
./run.sh
```

## Background
The reason for this code is to make spaced repetition more accessible and convenient for students, especially for study sessions. Usually, spaced algorithms are made for flashcards, such as the FSRS or SM-2 (used by Anki) algorithms. Flashcard spacing is very specific due to isolated fact recall, but study sessions require different spacing due to more consolidation of information.

I've been using a similar code for around 2 months now, and I found it extremely helpful in keeping track of when I should study. Plus, with the adaptability of the FSRS algorithm, I can study a subject a day earlier or later if needed, based on my schedule and prioritizes. The spacing does not have to be strict; it's a guideline. The algorithm helps you stay organized. I know exactly what I have to study and can schedule and prioritize based on the Gantt chart created by the FSRS code. After using it for 2 months, I thought this organization system could be useful for other students, especially in the [iCS](https://icanstudy.com/) community, so I made this code more accessible. One of the many advantages I found is that it allows you to focus on studying the topics you find hardest by spacing them more frequent.

The original personalized code I created is integrated with Obsidian, so I document my study sessions in an Obsidian table. I hope in the future, I can turn this code into an app to allow for more flexibility in how data is stored. Below is an image from my Obsidian personal system,
![image](https://github.com/user-attachments/assets/3ab3e3fe-e8a2-4a95-a584-b857deb4b89a)

and here's an image showing how this prototype could potentially look in the future with subjects being coloured and such. **Note: These images are from my personal code and not features of this prototype.**
![image](https://github.com/user-attachments/assets/fb50b728-85eb-4eee-a496-32aacf325170)

This code is currently a prototype for demonstration and is quite simple and limited. If future development permits, I might continue to update this code with more features, such as grouping topics by subjects or allowing more flexible ways to input data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
This project uses the [FSRS Algorithm](https://github.com/open-spaced-repetition/py-fsrs), which is an open-source project. Thanks to the contributors of the FSRS Algorithm.
