import pandas as pd
import numpy as np
from data_frame import df
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split ,GridSearchCV
from sklearn.linear_model import LogisticRegression

 
# -- Logical Regression Model --


class logistic_reg_model: #(le ,sc , all_team_names, y_test, X_test,model_cv, best_model)

  def __init__(self,df):
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
    self.le = LabelEncoder()
    self.le.fit(all_team_names)
    self.all_team_names = all_team_names 

    # TRANSFORM the main dataframe
    df_clean["Team_A_ID"] = self.le.transform(df_clean["Team A"])
    df_clean["Team_B_ID"] = self.le.transform(df_clean["Team B"])

    # Standard ML Steps
    X = df_clean[["Team_A_ID", "Team_B_ID", "First Inning"]]

      # Team A won = 1  Team B Won = 0 
    y = (df_clean['Winner'] == df_clean['Team A']).astype(int) 

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)
    self.y_test = y_test

    # Scaling
    self.sc = StandardScaler()
    self.X_train = self.sc.fit_transform(X_train)
    self.X_test = self.sc.transform(X_test)

    # Training and Testing
    model = LogisticRegression()

    # Defining ParameterGrid
    param_grid = {
                    'C' : [0.01, 0.1, 1, 10, 100]
                 }

    # Setup GridsearchCV
    self.model_cv = GridSearchCV(model, param_grid, cv=5, scoring= 'precision')

    self.model_cv.fit(self.X_train, y_train)

     # best model
    self.best_model = self.model_cv.best_estimator_
    


  # Report function
  def reportgen(self):
      pred_log =self.best_model.predict(self.X_test)
      print(classification_report(self.y_test, pred_log))
      print(confusion_matrix(self.y_test, pred_log))


  # Predict Function
  def predict_future(self):

    # Input
    print("Select two Teams to check : ")
    i=1
    for team_x in self.all_team_names:
        print(f"{i} : {team_x}")
        i+=1
    
    try:
        team_a = int(input("Enter the number of team who play first: "))-1
        team_b = int(input("Enter the number of team who ball first: "))-1
        first_inning_score = int(input("Enter the first team batting Score : "))

        team_a_name = self.all_team_names[team_a]
        team_b_name = self.all_team_names[team_b]

        # Automatically get the correct IDs from the encoder
        t_a_id = self.le.transform([team_a_name])[0]
        t_b_id = self.le.transform([team_b_name])[0]

        new_match = pd.DataFrame([[t_a_id, t_b_id, first_inning_score]], 
                                columns=["Team_A_ID", "Team_B_ID", "First Inning"])

        Xnew = self.sc.transform(new_match)
        ynew = self.best_model.predict(Xnew)

        # Output
        winner_result = team_a_name if ynew[0] == 1 else team_b_name
        print(f"The predicted winner between {team_a_name} and {team_b_name} is: {winner_result}")

    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number from the list.")
