# Load necessary libraries
library(dplyr)
library(ggplot2)
library(readr)
library(tidyr)
library(reshape2)
library(corrplot)

# Load the dataset
data <- read_csv("sample_data.csv")
# Check for missing values
sum(is.na(data))

# Basic Data Analysis

# Age distribution
ggplot(data, aes(x = Age)) +
  geom_histogram(binwidth = 5, fill = "blue", color = "black") +
  labs(title = "Age Distribution", x = "Age", y = "Frequency") +
  theme_minimal()

# Gender distribution
ggplot(data, aes(x = Gender)) +
  geom_bar(fill = "purple", color = "black") +
  labs(title = "Gender Distribution", x = "Gender", y = "Count") +
  theme_minimal()

# Department distribution
ggplot(data, aes(x = Department)) +
  geom_bar(fill = "green", color = "black") +
  labs(title = "Department Distribution", x = "Department", y = "Count") +
  theme_minimal()

# Score distribution
ggplot(data, aes(x = Score)) +
  geom_histogram(binwidth = 5, fill = "orange", color = "black") +
  labs(title = "Score Distribution", x = "Score", y = "Frequency") +
  theme_minimal()

# Boxplot of Scores by Gender
ggplot(data, aes(x = Gender, y = Score)) +
  geom_boxplot(fill = "cyan", color = "black") +
  labs(title = "Boxplot of Scores by Gender", x = "Gender", y = "Score") +
  theme_minimal()

# Boxplot of Scores by Department
ggplot(data, aes(x = Department, y = Score)) +
  geom_boxplot(fill = "pink", color = "black") +
  labs(title = "Boxplot of Scores by Department", x = "Department", y = "Score") +
  theme_minimal()

# Mean Score by Gender
mean_score_gender <- data %>%
  group_by(Gender) %>%
  summarize(mean_score = mean(Score), .groups = 'drop')

print(mean_score_gender)

# Visualization of Mean Score by Gender
ggplot(mean_score_gender, aes(x = Gender, y = mean_score)) +
  geom_bar(stat = "identity", fill = "lightblue", color = "black") +
  labs(title = "Mean Score by Gender", x = "Gender", y = "Mean Score") +
  theme_minimal()

# Mean Score by Department
mean_score_department <- data %>%
  group_by(Department) %>%
  summarize(mean_score = mean(Score), .groups = 'drop')

print(mean_score_department)

# Visualization of Mean Score by Department
ggplot(mean_score_department, aes(x = Department, y = mean_score)) +
  geom_bar(stat = "identity", fill = "lightgreen", color = "black") +
  labs(title = "Mean Score by Department", x = "Department", y = "Mean Score") +
  theme_minimal()

# Correlation Matrix
# correlation_matrix <- data %>%
#   select(Age, Score) %>%
#   cor()

# print(correlation_matrix)

# Visualization of Correlation Matrix
# melted_correlation_matrix <- melt(correlation_matrix)
# ggplot(melted_correlation_matrix, aes(x = Var1, y = Var2, fill = value)) +
#   geom_tile() +
#   geom_text(aes(label = round(value, 2)), color = "white") +
#   scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1)) +
#   labs(title = "Correlation Matrix", x = "", y = "") +
#   theme_minimal()

# Scatter plot of Age vs. Score
ggplot(data, aes(x = Age, y = Score, color = Gender)) +
  geom_point() +
  labs(title = "Scatter Plot of Age vs. Score", x = "Age", y = "Score") +
  theme_minimal()

# Scatter plot of Age vs. Score with regression line
ggplot(data, aes(x = Age, y = Score, color = Gender)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Scatter Plot of Age vs. Score with Regression Line", x = "Age", y = "Score") +
  theme_minimal()

# Pair plot (scatterplot matrix)
# pairs(data %>% select(Age, Score), main = "Scatterplot Matrix")

# Save the summary statistics to a CSV file
summary_stats <- data %>%
  summarise(
    mean_age = mean(Age),
    median_age = median(Age),
    sd_age = sd(Age),
    mean_score = mean(Score),
    median_score = median(Score),
    sd_score = sd(Score)
  )

write_csv(summary_stats, "summary_statistics.csv")

# Save mean scores by gender and department to CSV files
write_csv(mean_score_gender, "mean_score_gender.csv")
write_csv(mean_score_department, "mean_score_department.csv")