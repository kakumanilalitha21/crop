The website is live - https://crop-prediction-11.streamlit.app/

This project implements a machine learning model to predict crop yield based on various agricultural parameters. 
The model utilizes data preprocessing techniques and an XGBoost regressor to provide accurate yield predictions, 
aiding farmers in making informed decisions about their crops.

**Features**

Predicts crop yield based on multiple input parameters.
User-friendly web interface built with Streamlit.
Supports various crops and regions.
Provides insights into how different factors affect crop yield

**Technologies Used**

- Python                                                                                                                                                                     
- Pandas                                                                                                                                                                     
- Scikit-learn                                                                                                                                                               
- XGBoost     																																																																																
-Streamlit																																																																																	
-Joblib (for model persistence)

**Installation***
To set up the project locally, follow these steps:

- Clone the repository:																																							
    git clone https://github.com/yourusername/crop-yield-prediction.git
  																
- Navigate to the project directory							

    cd crop-yield-prediction
  										
- Install the required packages

    pip install -r requirements.txt

- Run the train.ipynb file (Model Traning)

    The pkl(pikle files) will be generated.
    After that run app.py file using streamlit command (streamlit run app.py).

- Dataset download Link

  Link --> https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield/data?select=crop_yield.csv

  
**Model Training and Evaluation**

The model is trained using an XGBoost regressor with a preprocessing pipeline that includes one-hot encoding for categorical features. The training process involves splitting the dataset into training and testing sets, fitting the model on training data, and saving both the model and preprocessed data for future use.

**Evaluation Metrics**

The following metrics are used to evaluate model performance:

Mean Absolute Error (MAE)																																																																									
,Mean Squared Error (MSE)																																																																									
,Root Mean Squared Error (RMSE)																																																																						
and R² Score.

**Results**

Once evaluated, the model provides various metrics indicating its performance on unseen data. The predictions can be visualized through the Streamlit app interface.
 

- **Command to run app.py File**

  streamlit run app.py

