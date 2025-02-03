README for Quicksort Implementation and Analysis
Overview
The Quicksort algorithm's deterministic and randomised implementations are also included in this repository. Quicksort is a very effective sorting algorithm that divides an array into subarrays and then uses a divide-and-conquer tactic to sort the components. This README outlines how to run the code and summarizes the findings from the performance analysis of both versions under various conditions.
Running the Code
To run the provided Quicksort implementations, you will need Python installed on your system. The code is compatible with Python 3.x. Here are the steps to execute the scripts:
1.	Clone the Repository: First, clone this repository to your local machine using Git commands or by downloading the zip file.
2.	Navigate to the Repository Folder: Change your directory to the folder containing the cloned repository.
3.	Run the Scripts:
o	Open a terminal or command prompt.
o	Execute the command python quicksort.py to run the deterministic version.
o	Execute the command python randomized_quicksort.py to run the randomized version.
Each script will sort a predefined array and print the sorted output to the terminal. You can modify the arrays directly in the script to test different data sets.
Summary of Findings
The performance analysis revealed the following insights:
•	Deterministic Quicksort: This version consistently chooses the last element as the pivot. The analysis showed that while this approach is straightforward and performs well on random data, its performance degrades to O(n2)O(n^2)O(n2) in the worst-case scenarios, such as when the input array is already sorted or reverse sorted. This occurs because the chosen pivot does not effectively divide the array into two nearly equal parts, leading to a higher number of recursive calls.
•	Randomized Quicksort: By introducing randomization in the pivot selection, this version mitigates the risk of hitting the worst-case performance on any specific input order. The average-case time complexity remains O(nlog⁡n)O(n \log n)O(nlogn), similar to the deterministic version, but the worst-case scenario is much less likely due to the randomization. Empirical tests across various input types (random, sorted, and reverse-sorted) demonstrated more consistent performance close to the average-case time complexity.
Conclusion
Because the randomised version of Quicksort reduces the effect of input order on efficiency, it often offers more reliable performance over a range of datasets. Because of this, it is especially useful in situations when the input circumstances are uncertain. Due to the recursive stack, both variants of the method operate in O(log⁡n)O(\log n)O(logn) space, making them space-efficient. However, the randomised version has negligible extra overheads for random number generation. 
These results highlight how crucial it is to take input properties and worst-case situations into account when selecting a sorting algorithm for real-world uses. 



