import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Upload CSV file
def upload_file():
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)

# Splitting the Data
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Model Selection
def select_model():
    model = RandomForestRegressor()
    return model

# Training the Model
def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model

# Model Evaluation
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    st.write("Mean Squared Error:", mse)

# Prediction
def make_prediction(model, input_data):
    prediction = model.predict(input_data)
    return prediction

# Streamlit App
def main():
    st.title("Machine Learning System")

    # Upload file and display data
    df = upload_file()
    if df is not None:
        st.subheader("Uploaded Data:")
        st.write(df)

        # Select columns
        selected_columns = st.multiselect("Select columns", df.columns)

        # Select target column
        target_column = st.selectbox("Select column to predict", df.columns)

        # Splitting the data
        if st.checkbox("Split Data"):
            X = df[selected_columns]
            y = df[target_column]
            X_train, X_test, y_train, y_test = split_data(X, y)
            st.write("Data split completed!")

            # Model Selection
            if st.checkbox("Select Model"):
                model = select_model()
                st.write("Model selected!")

                # Training the Model
                if st.checkbox("Train Model"):
                    trained_model = train_model(model, X_train, y_train)
                    st.write("Model Training completed!")

                    # Model Evaluation
                    if st.checkbox("Evaluate Model"):
                        evaluate_model(trained_model, X_test, y_test)

                    # Prediction
                    if st.checkbox("Make Prediction"):
                        input_data = {}
                        for col in selected_columns:
                            input_data[col] = st.number_input(f"Enter value for {col}", value=0.0)
                        input_data = pd.DataFrame([input_data])
                        prediction = make_prediction(trained_model, input_data)
                        st.write(f"Predicted Value for {target_column}:", prediction)

if __name__ == "__main__":
    main()
