**1. What is the root?**  
The root is node #0, where every student’s prediction starts. It asks, “Did the student study for 3.05 hours or less?”

**2. What questions does the tree ask?**  
The next question depends on the answer at the root.

- If study hours are 3.05 or less, node #1 asks whether the previous score is 97.5 or less. If yes, node #2 asks whether the assignment score is 92.5 or less. If no, the tree reaches leaf #5 and predicts Pass.
- If study hours are above 3.05, node #6 asks whether they are 5.25 or less. If yes, node #7 checks whether the assignment score is 58.5 or less. If no, node #10 checks whether the assignment score is 44.5 or less.

**3. What are the leaf nodes?**  
Leaf nodes are the endpoints that give the final prediction. This tree has seven leaves. Nodes #3, #4, and #8 predict **Fail**. Nodes #5, #9, #11, and #12 predict **Pass**.

**4. How does the tree reach a Pass/Fail decision?**  
The tree starts at the root and checks the student’s values against each question. A “yes” takes the left branch, and a “no” takes the right branch. At the leaf, the tree predicts the most common result among the training students who reached it.

For example, student 245 studied for 6.6 hours and had an assignment score of 44. The study hours were above both 3.05 and 5.25, and the assignment score was below 44.5. The path was **#0 → #6 → #10 → #11**. At leaf #11, 16 training students passed and 6 failed, so the tree predicted **Pass**. This matched the student’s actual result.