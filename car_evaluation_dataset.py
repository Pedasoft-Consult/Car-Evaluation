import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Define ETL functions
def extract(file_path):
    """
    Extract step: Load the dataset from the file.
    """
    data = pd.read_csv(file_path, header=None)
    return data

def transform(data):
    """
    Transform step: Preprocess the dataset.
    - Add column headers.
    - Remove duplicate rows.
    - Check and handle missing values.
    - Perform basic statistics.
    - Group by 'class' and calculate the most common values for columns.
    - Create a new "Car Quality" feature by combining 'buying' and 'maint'.
    """
    # Add column headers
    columns = ['Buying', 'Maint', 'Doors', 'Persons', 'Lug_Boot', 'Safety', 'Class']
    data.columns = columns

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Check for missing values
    if data.isnull().sum().sum() > 0:
        data = data.fillna(method='ffill')  # Forward fill missing values

    # Basic statistics for numeric columns
    print("\nBasic Statistics:")
    print(data.describe(include='all'))

    # Group by 'Class' and calculate most common values
    grouped_data = data.groupby('Class').agg(
        Most_Common_Buying=('Buying', lambda x: x.mode()[0]),
        Most_Common_Maint=('Maint', lambda x: x.mode()[0])
    )
    print("\nGrouped Data (Most Common Values):")
    print(grouped_data)

    # Encode categorical columns
    label_encoders = {}
    for column in ['Buying', 'Maint', 'Doors', 'Persons', 'Lug_Boot', 'Safety']:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

    # Create a new feature "Car Quality" by combining 'Buying' and 'Maint'
    data['Car_Quality'] = data['Buying'] + data['Maint']

    return data

def load(data, output_file):
    """
    Load step: Save the cleaned and transformed dataset to a CSV file.
    """
    data.to_csv(output_file, index=False)
    print(f"\nTransformed dataset saved to {output_file}")

# ETL Process
file_path = 'car.data'
output_file = 'cleaned_car_evaluation.csv'

# Extract
raw_data = extract(file_path)

# Transform
transformed_data = transform(raw_data)

# Load
load(transformed_data, output_file)
