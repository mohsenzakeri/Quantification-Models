library(rstan)

row_starts <- read.csv("row_starts.csv", header=FALSE, sep=",")
weights <- read.csv("weights.csv", header=FALSE, sep=",")
columns <- read.csv("columns.csv", header=FALSE, sep=",")
counts <- read.csv("parse_eq_classes_file/counts.csv", header=FALSE, sep=",")

stan_data <- list(weights = weights, columns = columns, row_starts = row_starts, counts = counts)

stan_model <- "stan_model_eq_classes.stan"

fit <- stan(file = stan_model, data = stan_data, warmup = 500, iter = 1000, chains = 4, cores = 2, thin = 1)
