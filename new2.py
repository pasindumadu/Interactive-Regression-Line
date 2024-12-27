import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit App Title
st.title("Interactive Linear Regression with Total Error")

# Instructions
st.write("Use the controls below to adjust the slope and intercept of the regression line. The interface adapts to mobile and desktop screens.")

# Responsive layout for controls
col1, col2 = st.columns(2)

with col1:
    slope = st.slider("Slope", min_value=-10.0, max_value=10.0, value=1.0, step=0.01)  # Step size 0.01 for second decimal
with col2:
    intercept = st.slider("Intercept", min_value=-20.0, max_value=20.0, value=1.0, step=0.01)  # Step size 0.01 for second decimal

# Generate data
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = 3 * x + 5 + np.random.normal(0, 2, size=x.shape)

# Calculate regression line and total error
def calculate_regression_line(x, slope, intercept):
    return slope * x + intercept

def calculate_total_error(y_true, y_pred):
    return np.sum((y_true - y_pred) ** 2)

y_pred = calculate_regression_line(x, slope, intercept)
total_error = calculate_total_error(y, y_pred)

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Scatter and regression lines
ax1.scatter(x, y, color='blue', label='Data Points')
ax1.plot(x, y_pred, color='red', label=f"Interactive: y = {slope:.2f}x + {intercept:.2f}")
best_slope, best_intercept = np.polyfit(x, y, 1)
ax1.plot(x, best_slope * x + best_intercept, color='purple', linestyle='--', label=f"Best Fit: y = {best_slope:.2f}x + {best_intercept:.2f}")
ax1.legend()
ax1.set_title("Interactive Regression Plot")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")

# Total error bar
ax2.barh(["Total Error"], [total_error], color='green', height=0.5)
ax2.set_title("Total Error")
ax2.set_xlim(0, max(total_error + 50, 500))

# Display plot
st.pyplot(fig)

# Display total error as text
st.write(f"**Total Error:** {total_error:.2f}")
