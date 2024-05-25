library(dplyr)
library(tidyr)

# Assuming 'df' is your data frame
df %>%
  summarise(across(where(is.numeric), .fns = list(mean = mean, sd = sd)))