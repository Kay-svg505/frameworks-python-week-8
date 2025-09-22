CORD-19 Data Explorer Assignment

Overview

This project provides a basic analysis of the CORD-19 research dataset using Python and Streamlit. The focus is on exploring COVID-19 research papers, performing simple data cleaning,
creating visualizations, and building an interactive web application for easy exploration.The dataset used is metadata.csv from the CORD-19 research challenge, which contains information about 
paper titles, abstracts, authors, journals, publication dates, and sources.
Learning Objectives Achieved

By completing this assignment, the following objectives were accomplished:

1.Data Loading and Exploration
Loaded the metadata.csv file into a pandas DataFrame.
Checked the shape, column types, and missing values.
Examined a sample of the data to understand its structure.

2.Data Cleaning and Preparation
Converted the publish_time column to datetime format.
Extracted the publication year for time-based analysis.
Created a new column abstract_word_count to analyze abstract lengths.
Removed rows missing essential information such as title or publish_time.

3.Data Analysis and Visualization
Counted the number of publications per year.
Identified the top journals publishing COVID-19 research.
Created a word cloud of frequent words in paper titles.
Visualized the distribution of papers by source (source_x).
Plotted the distribution of abstract lengths.

4.Streamlit Application
Built an interactive app with a title and description.
Added a slider to filter papers by year.
Displayed all visualizations within the app.
Provided a sample of the dataset for inspection.

Key Insights
The number of COVID-19 research papers increased sharply in 2020–2021, reflecting global research activity during the pandemic.
Top journals include widely recognized medical and scientific publications.
The most frequent words in titles highlight research focus areas such as “COVID,” “SARS-CoV-2,” and “vaccine.”
The distribution of sources shows that most papers were published in academic journals and preprint servers.
Abstract lengths vary widely, providing insight into the diversity of reporting styles in the dataset.

How to Run the App

1.Install the required packages:
pip install pandas matplotlib seaborn streamlit wordcloud
2.Ensure metadata.csv is in the project directory.
3.Run the Streamlit app:
streamlit run analysis.py
4.Open the browser link provided by Streamlit (e.g., http://localhost:8506) to explore the app.

Challenges and Reflections

Memory Issues: The dataset is very large, which initially caused MemoryError when loading. This was resolved by selectively loading only necessary columns and using sampling when needed.
Data Cleaning: Handling missing values and inconsistent date formats required careful preprocessing.
Visualization Choices: Choosing meaningful visualizations for text-heavy columns (like titles and abstracts) required using a word cloud and histogram for clarity.
Overall, this project provided practical experience with real-world data analysis, data cleaning, and building an interactive web app with Streamlit.

Conclusion

This project demonstrates fundamental data analysis skills, effective visualization techniques, and the ability to create an interactive Python web application. It successfully meets all the
assignment requirements and provides a clear, insightful exploration of the CORD-19 research papers.


**Note:** The full metadata.csv is too large to include in this repository. 
A sample file (`metadata_sample.csv`) is included for testing and demonstration purposes. 
If you want to use the full dataset, download it from Kaggle:
https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge

