import pandas as pd
from sklearn.preprocessing import LabelEncoder

def extract(file_path):
    """
    Extract step: Load the dataset from the file.
    """
    data = pd.read_csv(file_path, header=None)
    return data

def transform(data):
    """
    Transform step: Preprocess the dataset.
    - Standardize column names by converting to lowercase and replacing spaces with underscores.
    - Remove duplicate rows.
    - Check and handle missing values.
    - Encode all categorical variables, including the target variable 'class'.
    - Calculate basic statistics for specific columns.
    - Group by 'class' and calculate the most common values for 'buying' and 'maint'.
    - Create a new "Car Quality" feature by combining 'buying' and 'maint'.
    """
    # Add column headers
    columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
    data.columns = columns

    # Standardize column names (already lowercase and snake_case in this case)

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Check for missing values
    if data.isnull().sum().sum() > 0:
        data = data.fillna(method='ffill')  # Forward fill missing values

    # Basic statistics for specific columns
    print("\nBasic Statistics:")
    print(data[['buying', 'maint', 'doors', 'persons']].describe(include='all'))

    # Group by 'class' and calculate most common values for 'buying' and 'maint'
    grouped_data = data.groupby('class').agg(
        most_common_buying=('buying', lambda x: x.mode()[0]),
        most_common_maint=('maint', lambda x: x.mode()[0])
    )
    print("\nGrouped Data (Most Common Values):")
    print(grouped_data)

    # Encode categorical columns
    label_encoders = {}
    for column in ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

    # Create a new feature "Car Quality" by combining 'buying' and 'maint'
    data['car_quality'] = data['buying'] + data['maint']

    return data, label_encoders

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
transformed_data, label_encoders = transform(raw_data)

# Load
load(transformed_data, output_file)
