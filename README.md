# StudySessionsFSRS
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
## Background
The reason for this code is to make spaced repetition more accessible and convenient for students, especially for study sessions. Usually, spaced algorithms are made for flashcards, such as the FSRS or SM-2 (used by Anki) algorithms. Flashcard spacing is very specific due to isolated fact recall, but study sessions require different spacing due to more consolidation of information.

This code is currently a prototype for demonstration and is quite simple and limited. If future development permits, I might continue to update this code with more features, such as grouping topics by subjects or allowing more flexible ways to input data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
This project uses the [FSRS Algorithm](https://github.com/open-spaced-repetition/py-fsrs), which is an open-source project. Thanks to the contributors of the FSRS Algorithm.
