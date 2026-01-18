# LPL Match Winner Predictor

This project uses Machine Learning to predict the winner of Lanka Premier League (LPL) matches based on historical data. It specifically analyzes the impact of the first inning score and the participating team matchups.

---

## Overview

The application processes historical LPL data, standardizes team names to their respective cities to account for seasonal franchise rebranding, and uses a [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) model to calculate the probability of a win for either the batting or bowling side.

---

## Data Source

The dataset used for training this model is derived from [Cricsheet](https://cricsheet.org/), which provides structured ball-by-ball and match-level data for cricket formats worldwide.

---

## Features

- **Data Standardization**: Automatically converts historical franchise names (e.g., "Dambulla Aura", "Dambulla Sixers") to a consistent city-based identity ("Dambulla").

- **Binary Classification**: Predicts whether Team A (Batting first) or Team B (Bowling first) will win.

- **Preprocessing**: Implements [LabelEncoding](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) for categorical team data and [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) for numerical feature normalization.

- **Interactive CLI**: Allows users to input specific matchups and first-inning scores to get real-time predictions.

---

## Requirements

To run this project, you need [Python](https://www.python.org/) installed along with the following libraries:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

---

## Project Structure

- `app.py`: The main execution script containing the data processing pipeline, model training, and interactive prediction function.
- `lpldata`:Contain all json Data Files
- `total_json_retrun.py`: Convert json files data to single unit
- `data_frame.py`: The module responsible for loading and initial formatting of the raw dataset.
- `win_mark.py`: Core of the Machine Learning module
- `README.md`: Project documentation.

You can place your data files (e.g., from Cricsheet) in a dedicated folder such as `data/` and load them in `data_frame.py`.

---

## How to Run

Once you have installed the requirements, execute the application by running the following command in your terminal:

```bash
python app.py
```

Make sure you run this command from the root directory of the project (where `app.py` is located).

---

## Model Performance

The current model utilizes Logistic Regression and achieves an accuracy of approximately 71%.

**Evaluation Metrics:**

- **Precision**: Measures the accuracy of the win predictions.
- **Recall**: Measures the model's ability to identify actual wins for a specific class.
- **Confusion Matrix**: Generated during execution to visualize True Positives and False Positives.

---

## Usage

Upon running `app.py`, the system will:

1. Clean and encode the historical data.
2. Train the model.
3. Display a classification report.
4. Prompt you to select two teams and enter a first-inning score to generate a prediction.
