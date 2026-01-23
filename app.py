from logistic_reg_model import logistic_reg_model
import data_frame
import threading
import time

import threading
from logistic_reg_model import logistic_reg_model
import data_frame

# Global variables
model_instance = None
is_ready = False

def silent_trainer():
    global model_instance, is_ready
    model_instance = logistic_reg_model(data_frame.df)
    is_ready = True

# Start the background thread 
bg_thread = threading.Thread(target=silent_trainer, daemon=True)
bg_thread.start()

# --- Main Menu ---
while True:
    print("\n--- Main Menu ---")
    print("1. Predict Future Match")
    print("2. Classification Report")
    print("3. View Data Frame")
    print("0. Exit")
    
    choice = input("\nSelect Option: ")

    if choice == "1":
        if is_ready:
            model_instance.predict_future()
        else:
            print("(!) Feature not ready yet. Still analyzing data...")

    elif choice == "2":
        if is_ready:
            model_instance.reportgen()
        else:
            print("(!) Report is being generated. Please try again in a moment.")

    elif choice == "3":
        data_frame.show_dataframe()

    elif choice == "0":
        print("Exiting...")
        break
