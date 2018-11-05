library(rstan)

stan_fit <- readRDS("large_fit.rds",NULL)

stan_fit_theta <- summary(stan_fit, pars = c("theta"))$summary

stan_ests <- stan_fit_theta[, c("mean")]

salmon_fit <- read.csv(file="/mnt/scratch2/mohsen/stan-test/salmon-output/quant.sf", header=TRUE, sep="\t")

salmon_ests <- salmon_fit$NumReads

cor.test(salmon_ests, stan_ests, method="spearman")