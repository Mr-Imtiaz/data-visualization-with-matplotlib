
2. **Create `basic_plots.py`:**
   - Create a new file named `basic_plots.py`.
   - Add the following content:

```python
# basic_plots.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the sample data
data = pd.read_csv('sample_data_for_visualization.csv')

# Line Plot
plt.figure(figsize=(10, 5))
plt.plot(data['x'], data['y'], label='Line Plot', color='blue')
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()

# Bar Plot
plt.figure(figsize=(10, 5))
plt.bar(data['category'], data['value'], color='orange')
plt.title('Bar Plot Example')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Histogram
plt.figure(figsize=(10, 5))
plt.hist(data['value'], bins=10, color='green', alpha=0.7)
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

