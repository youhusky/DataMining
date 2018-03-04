# DataMining
### This is my code from INF 553 class in Fall 2015 semester
> 
Version: 1.0
Author: Joshua Li  
P.S. I saw some people fork my repo but just remind that some code may not be meet the requirment of latest task in the session INF 553  
You can find more detail in each finder
## Assignment 1 Algorithms in MapReduce  
---
### Problem 1 (tf-df)
Background: Given a document, tf (term frequency) of a term in the document is the number of occurrences of the term in the document.  
Task: Write a MapReduce program, tf_df.py, that finds unique tokens in a given collection of documents, and for each token, computes its term frequency in each documents, and also its document frequency.

---
### Problem 2 (frequent itemsets)  
In this problem, you are given a set of transactions. Each transaction contains a set of items purchased by some customer. Items are represented as integers.
In this problem, you are asked to find all 2-itemsets that appear in a given set of transactions at least 100 times. 

---
### Problem 3 (squaring matrix, one-phase)  
In this problem, you are provided with a matrix, say A, and asked to write a MapReduce program to compute its square (A2). You may assume the matrix is 5x5.  
In this problem, we ask you to implement a MapReduce program, squared_one.py, using the one-phase approach, that is, the reducer will be responsible for both multiplication of corresponding elements (both from the same matrix in this case) and addition of products.  

---
### Problem 4 (squaring matrix, two-phase)  
This problem is similar to Problem 3, but you are asked to write a two-phase program. Recall that in the first phase, multiplication results of corresponding elements from the matrices are obtained. Then, in the second phase, individual products are added together to produce the final element in the output (squared) matrix. Again, you may assume the matrix is 5x5. 

---
## Assignment 2
---
### Problem 1 PCY Algorithm 
Implement PCY algorithm using a single hash and print all frequent itemsets. You can use a hashing function of your choice.

---
### Problem 2: Multi­Hash Algorithm
Implement the multi­hash algorithm to generate frequent itemsets. You need to use 2 independent hashing functions for this. Make sure that all candidates are hashed to both the hashing functions to generate 2 different bit vectors. Both the hashes will have the same number of buckets.

---
### Problem 3: Toivonen Algorithm
Implement the Toivonen algorithm to generate frequent itemsets. For this algorithm you need to use a sample size of less than 60% of your entire dataset. Use an appropriate sampling method to get the random sample set. Also perform a simple Apriori algorithm with the random sample set. Check for negative borders and run the algorithm again with a different sample set if required till there are no negative borders that have frequency > support.

---
## Assignment 3: User-based Collaborative Filtering
---
In this assignment you will implement a simple user-based collaborative filtering recommender system for predicting the ratings of an item using the data given. This prediction should be done using k nearest neighbors and Pearson correlation. Finally using the similarity of the k nearest neighbors, you are required to predict the ratings of the new item for the given user.

---
## Assignment 4: Hierarchical Clustering
---
In this assignment, you are asked to implement a hierarchical agglomerative clustering algorithm. As shown in class, the algorithm starts by placing each data point in a cluster by itself and then repeatedly merges two clusters until some stopping condition is met.

---
## Assignment 5: Community Detection
---
In this assignment you will be implementing a community detection algorithm using a divisive hierarchical clustering (Girvan-Newman algorithm). You will be making use of 2 python libraries called networkx and community. The community library will be provided to you and you need to simply import it. The networkx is a python library which can be installed on your machines. The assignment will require making use of the betweenness function and the modularity function which are a part of the networkx and the community libraries respectively. You will also need to use the matplotlib library for plotting the communities.
Do not use the best_partition() function in the community library to obtain the partitions of the input graph.
This assignment also contains a 20% bonus section, which will be explained at the end of the assignment description.

