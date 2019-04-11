# SGO-FIG

Repository for the paper **High dimensional optimal design using the Fisher information gain and gradient descent** by [Dennis Prangle](github.com/dennisprangle/), [Colin Gillespie](github.com/csgillespie/), \& [Sophie Harbisher](github.com/SophieHarbisher).
The paper can be found on [arXiv](.).

### Abstract

Finding high dimensional designs is increasingly important in applications of experimental design, but is computationally demanding under existing methods.
We introduce an efficient approach applying recent advances in stochastic gradient optimisation methods.
To allow rapid gradient calculations we work with a computationally convenient utility function, the trace of the Fisher information.
We provide a decision theoretic justification for this utility, analogous to work by Bernardo (1979) on the Shannon information gain.
Due to this similarity we refer to our utility as the Fisher information gain.
We compare our optimisation scheme, SGO-FIG, to existing state-of-the-art methods and show our approach is quicker at finding designs which maximise expected utility, allowing designs with hundreds of choices to be produced in under a minute.

### Repository structure

 * [```examples```](./examples): jupyter notebooks to implement SGO-FIG for the examples in the paper


 * [```figures```](./figures): contains data and python scripts to generate figures in the paper


 [comment]: <> (* ```paper???```: LaTeX files to produce the paper)
