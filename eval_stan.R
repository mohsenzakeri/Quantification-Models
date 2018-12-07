#test existing branch
library(rstan)
library(ggplot2)

stan_fit <- readRDS("small_fit_no_prior_1000iter.rds",NULL)

stan_fit_theta <- summary(stan_fit, pars = c("theta"))$summary

stan_ests <- stan_fit_theta[, c("mean")]

salmon_fit <- read.csv(file="/mnt/scratch2/mohsen/stan-test/salmon-0.11.3-linux_x86_64/sample_data/salmon-output/quant.sf", header=TRUE, sep="\t")

salmon_ests <- salmon_fit$NumReads

stan_ests <-stan_ests * sum(salmon_ests)

cor.test(salmon_ests, stan_ests, method="spearman")

qplot(log(salmon_ests),log(stan_ests),alpha=0.5)
ggsave("cor.pdf", plot = last_plot())
