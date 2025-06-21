import pandas as pd

# Load the dataset with labels
df = pd.read_csv("data/phishing_data.csv")

# Drop the 'class' column
df.drop(columns=["class"], inplace=True)

# Save the test dataset
df.to_csv("data/test_data.csv", index=False)

print("✅ Test CSV created: data/test_data.csv")
