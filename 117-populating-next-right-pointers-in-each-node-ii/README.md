# 117. Populating Next Right Pointers in Each Node II

You are given **a binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

* You may only use constant extra space.
* Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Constraints:

* The number of nodes in the given tree is less than 6000.
* -1000 <= node.val <= 1000

<https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/>
