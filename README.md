### **Dataset:**

* **Car Evaluation Dataset**  
  You can download it from the UCI Machine Learning Repository:  
  [Car Evaluation Dataset](https://archive.ics.uci.edu/ml/datasets/car+evaluation)  
  ---

  ### **Exercise: Data Extraction and Transformation \- Car Evaluation Dataset**

  #### **Objective:**

### **Practice extracting data, cleaning, and transforming the **Car Evaluation Dataset**.

---

### **Steps for the Exercise:**

#### **1\. Data Extraction**

* Download the `car.data` file from the UCI Machine Learning Repository.  
* Load the dataset into a Pandas DataFrame.

  #### **2\. Data Cleaning and Transformation**

* **Standardize column names** by converting to lowercase and replacing spaces with underscores.  
* **Encode categorical columns**:  
  * Use label encoding or one-hot encoding for the target variable (`class`), which has values like "unacceptable", "acceptable", "good", "very good".  
  * Perform the same encoding for other categorical variables like `buying`, `maint`, `doors`, `persons`, `lug_boot`, and `safety`.  
* **Remove any duplicate rows**.  
* **Check for missing values** and handle them accordingly (though this dataset generally doesn't have missing values).

  #### **3\. Data Analysis and Transformation**

* **Calculate basic statistics** for columns like `buying`, `maint`, `doors`, and `persons`.  
* **Group by 'class'** and calculate the most common value for other columns like `buying` and `maint`.  
* **Create a new feature** by combining 'buying' and 'maint' to make a "Car Quality" feature.

  #### **4\. Save the Transformed Dataset**

* Save the cleaned and transformed dataset to a new CSV file (`cleaned_car_evaluation.csv`).


