data {
    int < lower = 1 > N; // eq classes count
    int < lower = 1 > M; // transcripts count
    int < lower = 1 > Q; // total weighs count
    vector[Q] weights; // eq class conditional props
    int columns[Q]; // weight vector column indicator
    int row_starts[N+1]; // weight vector row starts
    vector[N] counts; // number of fragments in each eq class
    vector[M] alpha;
}

parameters{
    simplex[M] theta; // transcript_counts
}

transformed parameters {
    vector[N] likelihood; 
    likelihood = csr_matrix_times_vector(N, M, weights, columns, row_starts, theta) .* counts;
}

model{
    //theta ~ dirichlet(alpha);
    target += log(likelihood) .* counts;
}
