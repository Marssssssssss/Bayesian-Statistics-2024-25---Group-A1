setwd("C:/Users/pasca/OneDrive/Desktop/progetto")
library(readxl)
library(openxlsx)
library(tidyr)
library(dplyr)
library(lubridate)
library(dplyr)
library(CausalImpact)
library(zoo)
library(stringr)
library(reshape2)

# upload csv for confrontation
high<-read.csv("Final models/Beta_per_cat/high.csv", row.names = NULL)
high <- high[, -1]
med<-read.csv("Final models/Beta_per_cat/med.csv", row.names = NULL)
med <- med[, -1]
low<-read.csv("Final models/Beta_per_cat/low.csv", row.names = NULL)
low <- low[, -1]

# upload and normalize variables
complete<-read_excel("final.xlsx")

vars_to_standardize <- c("Valore", "temperature_2m_mean", "sunshine_duration", 
                         "daylight_duration", "wind_speed_10m_max", "et0_fao_evapotranspiration")
complete$Valore <- (complete$Valore - mean(complete$Valore, na.rm = TRUE)) / sd(complete$Valore, na.rm = TRUE)
complete$temperature_2m_mean <- (complete$temperature_2m_mean - mean(complete$temperature_2m_mean, na.rm = TRUE)) / sd(complete$temperature_2m_mean, na.rm = TRUE)
complete$sunshine_duration <- (complete$sunshine_duration - mean(complete$sunshine_duration, na.rm = TRUE)) / sd(complete$sunshine_duration, na.rm = TRUE)
complete$daylight_duration <- (complete$daylight_duration - mean(complete$daylight_duration, na.rm = TRUE)) / sd(complete$daylight_duration, na.rm = TRUE)
complete$wind_speed_10m_max <- (complete$wind_speed_10m_max - mean(complete$wind_speed_10m_max, na.rm = TRUE)) / sd(complete$wind_speed_10m_max, na.rm = TRUE)
complete$et0_fao_evapotranspiration <- (complete$et0_fao_evapotranspiration - mean(complete$et0_fao_evapotranspiration, na.rm = TRUE)) / sd(complete$et0_fao_evapotranspiration, na.rm = TRUE)

# create dataset
complete_dataset<-complete
complete_dataset$date <- as.Date(complete_dataset$Settimana)
impact_list <- list()
results <- list()



for (id in unique(complete_dataset$sensor_id)) {
  print(id)
  sensor_data <- complete_dataset %>% filter(sensor_id == id)

  data_matrix <- sensor_data %>%
    select(date, Valore,  temperature_2m_mean,
           sunshine_duration, daylight_duration, wind_speed_10m_max, 
           et0_fao_evapotranspiration) 
  data_matrix <- data_matrix %>%
    arrange(date)

  data_matrix$date_num <- as.numeric(data_matrix$date)
  
  # Causal Impact on R to perform the comparison
  pre_period <- c(which(data_matrix$date_num == as.numeric(as.Date("2018-02-05"))), 
                  which(data_matrix$date_num == as.numeric(as.Date("2021-01-18"))))
  
  post_period <- c(which(data_matrix$date_num == as.numeric(as.Date("2021-01-25"))), 
                   which(data_matrix$date_num == as.numeric(as.Date("2024-01-01"))))
  
  data_matrix_impact <- data_matrix[, c("date", "Valore", "temperature_2m_mean", "sunshine_duration", "daylight_duration", 
                                        "wind_speed_10m_max", "et0_fao_evapotranspiration")]
  times<-data_matrix$date
  data <- zoo(data_matrix_impact[, -1], times)
  
  #apply the package to every station
  if(length(pre_period)==2&&length(post_period)==2){
    impact <- CausalImpact(data, times[pre_period], times[post_period])
    observed <- coredata(impact$series$response)
    predicted <- coredata(impact$series$point.pred)
    point_effect <- coredata(impact$series$point.effect)
    cumulative <- coredata(impact$series$cum.effect)
    results <- rbind(results, data.frame(
      time = seq_along(cumulative),
      observed = observed,
      predicted = predicted,
      point_effect = point_effect,
      cumulative = cumulative,
      Utm_Est = sensor_data$UTM_Est[1],
      Utm_Nord = sensor_data$Utm_Nord[1],
      sensor = id,
      lower=coredata(impact$series$cum.effect.lower),
      upper=coredata(impact$series$cum.effect.upper)
    ))
    
  }
  else{
    print("non funziona")
    print(sensor_data$UTM_Est[1])
  }
}


#filter CausalImpact results
filtered_data <- results %>% 
  filter(time >= 161)

results_impact <- filtered_data %>%
  group_by(sensor)
print(results_impact)
results_impact<-results_impact[,c(6,7,9,5,10)]
results_impact$Utm_Est<-results_impact$Utm_Est/1000
results_impact$Utm_Nord<-results_impact$Utm_Nord/1000
low<-low[,1:152]
high<-high[,1:152]
med<-med[,1:152]

low_long <- low %>%
  pivot_longer(cols = starts_with("X"), names_to = "Time", values_to = "Value") %>%
  mutate(Time = as.numeric(str_remove(Time, "X")))

med_long <- med %>%
  pivot_longer(cols = starts_with("X"), names_to = "Time", values_to = "Value") %>%
  mutate(Time = as.numeric(str_remove(Time, "X")))

high_long <- high %>%
  pivot_longer(cols = starts_with("X"), names_to = "Time", values_to = "Value") %>%
  mutate(Time = as.numeric(str_remove(Time, "X")))

results_stan<-cbind(low_long[,c(1,2,5)], med_long[,5],  high_long[,5])
colnames(results_stan) <- c("Utm_Est", "Utm_Nord","lower", "cumulative", "upper")

differenze1 <- setdiff(results_stan$Utm_Est, results_impact$Utm_Est)
differenze2 <- setdiff(results_impact$Utm_Est, results_stan$Utm_Est)

print("Differenze in results$sensor ma non in results_stan$IdSensore:")
print(differenze1)

print("Differenze in results_stan$IdSensore ma non in results$sensor:")
print(differenze2)

results_impact11 <- results_impact[order(results_impact$Utm_Est), ]
results_stan11 <- results_stan[order(results_stan$Utm_Est), ]
results_stan11 <- data.frame(results_stan11,row.names = NULL)



#final confusion matrix and model comparison
library(dplyr)
library(caret) 
library(writexl)

# station classification
classify_station <- function(df) {
  df %>%
    group_by(Utm_Est, Utm_Nord) %>%
    slice_tail(n = 1) %>%  
    mutate(
      category = case_when(
        lower < 0 & upper < 0 ~ "Intervallo < 0",
        cumulative < 0 ~ "Solo cumulative < 0",
        TRUE ~ "Cumulative > 0"
      )
    ) %>%
    select(Utm_Est, Utm_Nord, category)
}
classify_station <- function(df) {
  df %>%
    group_by(Utm_Est, Utm_Nord) %>%
    slice_tail(n = 50) %>%  # Take the last 50 observations for each station
    mutate(
      category = case_when(
        all(lower < 0 & upper < 0) ~ "Intervallo < 0",  # "Intervallo < 0" if 'lower' and 'upper' are < 0 in all last rows
        all(cumulative < 0 & !(upper < 0)) ~ "Solo cumulative < 0",  # "Solo cumulative < 0" if all 'cumulative' < 0 but not "Intervallo < 0"
        TRUE ~ "Cumulative > 0"  # Default to "Cumulative > 0"
      )
    ) %>%
    slice_tail(n = 1) %>%  # Keep only the last observation for each station after classification
    ungroup() %>%
    select(Utm_Est, Utm_Nord, category)  # Select relevant columns
}

# Classification for models
class_stan <- classify_station(results_stan)
class_impact <- classify_station(results_impact)
write_xlsx(class_impact, "class_impact.xlsx")
write_xlsx(class_stan, "class_stan_2.xlsx")

comparison <- left_join(class_stan, class_impact, by = c("Utm_Est", "Utm_Nord"),
                        suffix = c("_stan", "_impact"))

# Confusion matrix
conf_matrix <- table(comparison$category_stan, comparison$category_impact)
print(conf_matrix)

# Confusion matrix with modified order
conf_matrix <- table(factor(comparison$category_stan, 
                            levels = c("Cumulative > 0", "Solo cumulative < 0", "Intervallo < 0")), 
                     factor(comparison$category_impact, 
                            levels = c("Cumulative > 0", "Solo cumulative < 0", "Intervallo < 0")))

print(conf_matrix)

# Merge datasets by sensor_id
merged_data <- cbind(results_impact11, results_stan11[,c(3,4,5)])
colnames(merged_data) <- c("Utm_Est", "Utm_Nord","lower_I", "cumulative_I", "upper_I","lower_S", "cumulative_S", "upper_S")


# Compute confidence interval overlap
merged_data <- merged_data %>%
  
  mutate(overlap = (lower_I <= upper_S) & (lower_S <= upper_I))



# Compute the percentage of sensors where confidence intervals overlap
overlap_percentage <- mean(merged_data$overlap) * 100

# Print the result
cat(sprintf("Percentage of sensors with overlapping confidence intervals: %.2f%%\n", overlap_percentage))


# Perform paired t-test

t_test_result <- t.test(results_stan11$cumulative,results_impact11$cumulative, paired = TRUE)

print(t_test_result)



# Interpretation

if (t_test_result$p.value < 0.05) {
  
  print("The difference between models is statistically significant.")
  
} else {
  
  print("No significant difference between models.")
  
}



# extracting variables
filtered_stan <- class_stan %>%
  filter(category == "Intervallo < 0")
filtered_impact <- class_impact %>%
  filter(category == "Cumulative > 0")


# Common stations
common_stations <- inner_join(filtered_stan, filtered_impact, by = c("Utm_Est", "Utm_Nord"))
print(common_stations)
sensor_data <- complete_dataset %>% filter(sensor_id == 6784)
data_matrix <- sensor_data %>%
  select(date, Valore,  temperature_2m_mean,
         sunshine_duration, daylight_duration, wind_speed_10m_max, 
         et0_fao_evapotranspiration) 




