# Algorithms to solve the word and conjugacy problem in free groups
I coded these algorithms as part of my thesis work for the King's College London module 6CCM345A Third Year Project to decide the word and conjugacy problems in free groups.

In our algorithms, we adopt a specific representation for words. A word is expressed in the form:
$$w = x_{i_1}^{\varepsilon_1}x_{i_2}^{\varepsilon_2}\cdots x_{i_k}^{\varepsilon_k}$$
where $x_{i_j}$ is an element of the set $X \cup \{x^{-1} : x\in X\}$ and $\varepsilon_h \in \{ -1,1\}.$ We represent this word using an array:
$$w = [[i_1, \varepsilon_1], [i_2, \varepsilon_2], \ldots, [i_k, \varepsilon_k]].$$
We have opted for this representation in Python because utilising letters from the alphabet would impose limitations on the number of generators permitted in our group.

In this coding scheme, uppercase letters represent the inverse elements. For instance, the inverse of $x_i$ is denoted as $X_i$. When prompted to input words using this code, each letter must be separated by whitespace. For example, if we wish to input the word $w=x_1^{-1} x_2 x_3^{-1} x_4$, it should be written as: X1 x2 X3 x4.
