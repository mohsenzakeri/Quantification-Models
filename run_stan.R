library(rstan)
require("reticulate")

#row_starts <- read.csv("row_starts.csv", header=FALSE, sep=",")
#weights <- read.csv("weights.csv", header=FALSE, sep=",")
#columns <- read.csv("columns.csv", header=FALSE, sep=",")
#counts <- read.csv("parse_eq_classes_file/counts.csv", header=FALSE, sep=",")

#stan_data <- list(weights = weights, columns = columns, row_starts = row_starts, counts = counts)

source_python("pickle_reader.py")

stan_model <- "stan_model_eq_classes.stan"
stan_data <- read_pickle_file("stan_data_large.p")

rstan_options(auto_write = TRUE)
options(mc.cores = parallel::detectCores())

fit <- stan(file = stan_model, data = stan_data, warmup = 500, iter = 1000, chains = 4, cores = 16, include = TRUE, pars="theta")

saveRDS(fit, file = "/mnt/scratch2/mohsen/stan-test/parse_eq_classes_file/QuantificationModels/large_fit_no_prior_1000iter.rds")
