# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

# ETL
# Read the dataset
diabetes_indicator_no_clean = pd.read_csv('diabetes_healt_final_project/archive/diabetes_012_health_indicators_BRFSS2015.csv')
#let's see information about our dataset,information are visible on read_me file
print(diabetes_indicator_no_clean.head())
print(diabetes_indicator_no_clean.info())
#we could decide to encode some data to reduce the space data occuped or to change categorical data into ordinal data

#CLEANING DATA
#-let's check there aren't missing data
#missing_data=diabetes_indicator_no_clean.isnull().sum()
#print(missing_data)#there aren't missing so we don't have to do interpolation

#-let's check there aren't Outlier or non-compliant data
#for BMI we could calculate the z-score beacuase it's a non categorical data
z_score_colonna = np.abs(stats.zscore(diabetes_indicator_no_clean['BMI']))
outlier_threshold = 3
outlier_mask = z_score_colonna > outlier_threshold
#delete row with outliers-> we could do that beacause we have a lot of data
diabetes_indicator_no_clean = diabetes_indicator_no_clean[~outlier_mask]
#for the other features the values were collected taking into account a future analysis and therefore we have a coding for each feature,
# instead of calculating the z-score we check that the values are within their range and eliminate any values anomalous
condition = (
    'Diabetes_012 in [0, 1, 2] and HighBP in [0, 1] and HighChol in [0, 1] and '
    'CholCheck in [0, 1] and Smoker in [0, 1] and Stroke in [0, 1] and '
    'HeartDiseaseorAttack in [0, 1] and PhysActivity in [0, 1] and Fruits in [0, 1] and '
    'Veggies in [0, 1] and HvyAlcoholConsump in [0, 1] and AnyHealthcare in [0, 1] and '
    'NoDocbcCost in [0, 1] and GenHlth in [1, 2, 3, 4, 5] and '
    '0 <= MentHlth & MentHlth < 30 and 0 <= PhysHlth & PhysHlth < 30 and '
    'DiffWalk in [0, 1] and Sex in [0, 1] and 1 <= Age & Age <= 13 and '
    '1 <= Education & Education <= 6 and 1 <= Income & Income <= 8'
)
diabetes_indicator = diabetes_indicator_no_clean.query(condition)
#-Normalizzation data:it is necessary to normalize the data of our dataset because they have values on different scales, we prefer to apply a Min-Max because if you want to maintain the relative distance between the values, especially for binary variables and already arranged the outlier
# Identify the main variables
y = diabetes_indicator['Diabetes_012'].astype(int)
X = diabetes_indicator.drop(columns=['Diabetes_012'])

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

# Data Preprocessing: MinMaxScaler for numerical columns
preprocessor = ColumnTransformer(transformers=[
    ('num', MinMaxScaler(), X.columns)
])

# Create a pipeline
pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('classifier', RandomForestClassifier(random_state=0))
])

# Define the search space for GridSearchCV
search_space = [
    {'classifier': [RandomForestClassifier(random_state=0)],
     'classifier__n_estimators': [10, 50, 100, 200],  # Number of trees
     'classifier__max_depth': [None, 10, 20, 30],  # Maximum depth of trees
     'classifier__min_samples_split': [2, 5, 10],  # Minimum samples required to split a node
     'classifier__min_samples_leaf': [1, 2, 4]}  # Minimum samples required in a leaf node
]

# Initialize GridSearchCV
gs = GridSearchCV(pipeline, search_space, scoring='accuracy', cv=5)

# Cross-validation for model evaluation
cross_val_scores = cross_val_score(gs, X, y, cv=5, scoring='accuracy')
print("Cross-Validation Scores:", cross_val_scores)
print("Mean CV Accuracy:", np.mean(cross_val_scores))

# Train the model on the training set
gs.fit(x_train, y_train)

# Get the best model and its parameters
best_pipeline = gs.best_estimator_
best_model = best_pipeline.named_steps['classifier']
best_model_params = best_model.get_params()

print('Best Model:', best_model)
print('Best Model Parameters:', best_model_params)

# Make predictions on the test set
y_pred = best_pipeline.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

# Calculate the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', conf_matrix)

# Calculate the classification report
class_report = classification_report(y_test, y_pred)
print('Classification Report:\n', class_report)

# Calculate ROC AUC score if applicable
# Check if the model supports 'predict_proba'
if hasattr(best_pipeline.named_steps['classifier'], 'predict_proba'):
    y_proba = best_pipeline.predict_proba(x_test)[:, 1]
    auc_score = roc_auc_score(y_test, y_proba)
    print(f'ROC AUC Score: {auc_score:.4f}')
else:
    print("The selected model does not support ROC AUC calculation")

# Model performance on the training set
y_train_pred = best_pipeline.predict(x_train)
train_accuracy = accuracy_score(y_train, y_train_pred)

# Model performance on the test set
test_accuracy = accuracy_score(y_test, y_pred)

print(f'Train Accuracy: {train_accuracy:.4f}')
print(f'Test Accuracy: {test_accuracy:.4f}')

# Compare performances to assess overfitting
if train_accuracy > test_accuracy:
    if train_accuracy - test_accuracy > 0.1:  # Arbitrary threshold
        print("Possible overfitting detected.")
    else:
        print("Performances are consistent enough between train and test.")
else:
    print("No obvious overfitting detected.")

# Tuning Parameters: You can explore additional parameter options or models for better performance.
# Example of an alternative parameter grid to explore
alternative_search_space = [
    {'classifier': [RandomForestClassifier(random_state=0)],
     'classifier__n_estimators': [100, 150, 200],  # Modify the number of trees
     'classifier__max_depth': [15, 20, 25],  # Modify maximum depth of trees
     'classifier__min_samples_split': [2, 3, 4],  # Modify minimum samples to split a node
     'classifier__min_samples_leaf': [1, 2, 3]}  # Modify minimum samples in a leaf node
]

# Initialize an alternative grid search
alternative_gs = GridSearchCV(pipeline, alternative_search_space, scoring='accuracy', cv=5)

# Train the model with the alternative grid search
alternative_gs.fit(x_train, y_train)

# Get the best alternative model and its parameters
best_alternative_model = alternative_gs.best_estimator_
best_alternative_model_params = best_alternative_model.named_steps['classifier'].get_params()

print('Best Alternative Model:', best_alternative_model)
print('Best Alternative Model Parameters:', best_alternative_model_params)

# Confusion Matrix Plot: To visualize classification errors
from sklearn.metrics import plot_confusion_matrix

plt.figure(figsize=(8, 6))
plot_confusion_matrix(best_pipeline, x_test, y_test, cmap=plt.cm.Blues, display_labels=["No Diabetes", "Yes Diabetes"])
plt.title('Confusion Matrix')
plt.show()
