import pandas as pd
import numpy as np
from data_frame import df
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Remove draw matches
df_clean = df[df["Winner"] != "tie"].copy()

# Some name cleanup

  # Extract the first word from every team name
df_clean["Team A"] = df_clean["Team A"].str.split().str[0]
df_clean["Team B"] = df_clean["Team B"].str.split().str[0]
df_clean["Winner"] = df_clean["Winner"].str.split().str[0]

  # Special fix for B-Love Kandy (if it exists in your data)
df_clean["Team A"] = df_clean["Team A"].replace("B-Love", "Kandy")
df_clean["Team B"] = df_clean["Team B"].replace("B-Love", "Kandy")
df_clean["Winner"] = df_clean["Winner"].replace("B-Love", "Kandy")

# Encoding Process for all team 
all_team_names = pd.concat([df_clean["Team A"], df_clean["Team B"]]).unique()
le = LabelEncoder()
le.fit(all_team_names) 

# TRANSFORM the main dataframe
df_clean["Team_A_ID"] = le.transform(df_clean["Team A"])
df_clean["Team_B_ID"] = le.transform(df_clean["Team B"])

# Standard ML Steps
X = df_clean[["Team_A_ID", "Team_B_ID", "First Inning"]]
y = (df_clean['Winner'] == df_clean['Team A']).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

# Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training and Testing
model = LogisticRegression()
model.fit(X_train, y_train)
pred_log =model.predict(X_test)


# Report function
def reportgen():
    print(classification_report(y_test, pred_log))
    print(confusion_matrix(y_test,pred_log))


# Predict Function
def predict_future():

    # Input
    print("Select two Teams to check : ")
    i=1
    for team_x in all_team_names:
        print(f"{i} : {team_x}")
        i+=1
    
    try:
        team_a = int(input("Enter the number of team who play first: "))-1
        team_b = int(input("Enter the number of team who ball first: "))-1
        first_inning_score = input("Enter the first team batting Score : ")

        team_a_name = all_team_names[team_a]
        team_b_name = all_team_names[team_b]

        # Automatically get the correct IDs from the encoder
        t_a_id = le.transform([team_a_name])[0]
        t_b_id = le.transform([team_b_name])[0]

        new_match = pd.DataFrame([[t_a_id, t_b_id, first_inning_score]], 
                                columns=["Team_A_ID", "Team_B_ID", "First Inning"])

        Xnew = sc.transform(new_match)
        ynew = model.predict(Xnew)

        # Output
        winner_result = team_a_name if ynew[0] == 1 else team_b_name
        print(f"The predicted winner between {team_a_name} and {team_b_name} is: {winner_result}")

    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number from the list.")

