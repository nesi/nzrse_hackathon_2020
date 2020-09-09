library(dplyr)
library(ggplot2)
library(caret)

setwd("/Users/phicau/Dropbox (Uni of Auckland)/python/Hackathon/NeSI/")

# Load data
df_train = read.csv('emod3d_train_x.csv')
aux = read.csv('emod3d_train_y.csv')

# Prepend y
df_train <- data.frame(y = aux$core_hours, df_train)

# Clean data
# Remove y == 0
mask <- df_train$y <= 0.001
df_train <- df_train[!mask,]

# Remove y%%1 == 0
mask <- df_train$y%%1 == 0
df_train <- df_train[!mask,]

# Build new variables
df_train$n_cells <- df_train$nx*df_train$ny*df_train$nz
df_train <- within(df_train, rm(nx, ny, nz))

df_train$n_cellTimesSub <- df_train$n_cells*df_train$n_sub
df_train$n_cellPerCore <- df_train$n_cells/df_train$n_cores

df_train$n_cost <- df_train$n_cells*df_train$nt*df_train$n_cores
df_train$n_costTimesSub <- df_train$n_cost*df_train$n_sub

# Custom loss function
customMetric <- function(yActual,yPred) mean(max((yActual - yPred)*0.9,(yPred - yActual)*0.1))

set.seed(100)

lm1 <- train(y = df_train$y, x = df_train[,-1], method = "lm")
lm1$results

predict_lm1 <- predict(lm1,  df_train)
customMetric(df_train$y, predict_lm1)

rf1 <- train(y = df_train$y, x = df_train[,-1], method = "rf")
rf1$results

predict_rf1 <- predict(rf1,  df_train)
customMetric(df_train$y, predict_rf1)

# Read, build new variables and predict
df_test = read.csv('emod3d_test_x.csv')

df_test$n_cells <- df_test$nx*df_test$ny*df_test$nz
df_test <- within(df_test, rm(nx, ny, nz))

df_test$n_cellTimesSub <- df_test$n_cells*df_test$n_sub
df_test$n_cellPerCore <- df_test$n_cells/df_test$n_cores

df_test$n_cost <- df_test$n_cells*df_test$nt*df_test$n_cores
df_test$n_costTimesSub <- df_test$n_cost*df_test$n_sub

sol <- predict(rf1,  df_test)
write.csv(sol, 'emod3d_test_y.csv')












