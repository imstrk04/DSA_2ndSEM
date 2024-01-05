import numpy as np

# Given information
mean_original = 19
std_dev_original = 8
n = 7
wrong_observation = 14
corrected_observation = 17

# Placeholder dataset
dataset = [0] * n

# Calculate the sum of the original dataset before correction
sum_original = mean_original * n

# Calculate the sum of the corrected dataset
sum_corrected = sum_original - wrong_observation + corrected_observation

# Calculate the mean of the original dataset
mean_corrected = sum_corrected / n

# Calculate the sum of squared differences from the mean
sum_squared_diff = np.sum((np.array([wrong_observation if obs == corrected_observation else obs for obs in dataset]) - mean_corrected) ** 2)

# Calculate the sample variance of the original dataset
sample_variance_original = sum_squared_diff / (n - 1)

# Print the result
print(f"The estimated sample variance of the original dataset is approximately {sample_variance_original:.2f}")




