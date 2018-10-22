// Stan model for simple linear regression

data {
 int < lower = 1 > N; // eq classes count
 int < lower = 1 > M; // transcripts count
 int < lower = 1 > Q; // total weighs count
 vector[Q] weights; // eq class conditional probs
 int columns[Q]; // weight vector column indicator
 int row_starts[N+1]; // weight vector row starts
 vector[N] counts; // number of fragments in each eq class
 vector[N] y; // Outcome
}

parameters {
 vector[M] theta; // transcript_counts
}

transformed parameters {
 vector[N] likelihood_1;
 vector[N] likelihood;
 likelihood_1 = csr_matrix_times_vector(N, M, weights, columns, row_starts, theta);
 likelihood = likelihood_1 .* counts;
}

model {
 target += sum(likelihood);
}

generated quantities {
} // The posterior predictive distribution
