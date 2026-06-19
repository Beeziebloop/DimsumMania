# DimsumMania

This repository contains the Python implementation of **Dimsum Mania**, a Dynamic Programming-based optimization program developed to determine the optimal selection of dimsum varieties under budget and dietary constraints.

The program models the group dimsum ordering scenario as a modified **0/1 Knapsack Problem**, where the objective is to maximize the number of distinct dimsum varieties that can be sampled while ensuring that every group member receives at least one piece of each selected menu item. The optimization process also considers dietary restrictions such as shrimp allergies, vegetarian diets, vegan diets, and gluten intolerance.

It should be noted that this program was developed as part of a paper for the IF2211 Strategy of Algorithms course and serves primarily as a proof-of-concept implementation of the proposed methodology. Several assumptions were made in order to simplify the problem formulation, including the estimation of serving quantities for menu items and the use of a predefined menu dataset derived from the HAKA Dimsum menu.

The implementation applies a preprocessing stage to calculate the effective cost of each menu item based on group size and serving requirements before solving the optimization problem using Dynamic Programming. As a result, the recommendations produced by the program should be interpreted as theoretical approximations rather than exact real-world dining recommendations.