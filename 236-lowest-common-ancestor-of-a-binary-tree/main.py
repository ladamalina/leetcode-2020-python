import logging
from typing import List, Optional, Union

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        logging.info("-" * 40)
        logging.info(f"{p=}, {q=}")
        mid = self.traverseNode(root, p, q)
        logging.info(f"{mid=}")

        return mid

    def traverseNode(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Union[TreeNode, bool]:
        if root is None:
            return False

        if root.val == p.val or root.val == q.val:
            if self.traverseNode(root.left, p, q) is True:
                return root  # found middle in the root
            if self.traverseNode(root.right, p, q) is True:
                return root  # found middle in the root
            return True  # just found p or q node

        found_at_left: Union[TreeNode, bool] = self.traverseNode(root.left, p, q)
        if isinstance(found_at_left, TreeNode):
            return found_at_left  # found middle on the left side

        found_at_right: Union[TreeNode, bool] = self.traverseNode(root.right, p, q)
        if isinstance(found_at_right, TreeNode):
            return found_at_right  # found middle on the right side

        if found_at_left and found_at_right:
            return root  # found middle in the root
        found_something = found_at_left or found_at_right

        return found_something

    def lowestCommonAncestor_too_slow(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        logging.info("-" * 40)
        logging.info(f"{p=}, {q=}")
        p_track = self.trackNode(root, p)
        q_track = self.trackNode(root, q)
        logging.info(f"{p_track=}, {q_track=}")
        min_track = p_track if len(p_track) < len(q_track) else q_track
        max_track = p_track if len(p_track) > len(q_track) else q_track
        logging.debug(f"{min_track=}, {max_track=}")
        for i in range(len(min_track) - 1, -1, -1):
            if p_track[i].val == q_track[i].val:
                lca = p_track[i]
                logging.info(f"{lca=}")
                return lca


    def trackNode(self, root: TreeNode, n: TreeNode) -> List[TreeNode]:
        if root is None:
            return []
        if root.val == n.val:
            return [root]
        left_track = self.trackNode(root.left, n)
        if left_track:
            return [root] + left_track
        right_track = self.trackNode(root.right, n)
        if right_track:
            return [root] + right_track


def main():
    # logging.info(Solution().trackNode(
    #     root=TreeNode(val=1,
    #                   left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)),
    #                   right=TreeNode(val=3)
    #     ),
    #     n=TreeNode(val=4)
    # ))

    assert str(Solution().lowestCommonAncestor(
        root=TreeNode(val=1,
                      left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)),
                      right=TreeNode(val=3)
        ),
        p=TreeNode(val=5),
        q=TreeNode(val=4)
    )) == "2"
    assert str(Solution().lowestCommonAncestor(
        root=TreeNode(val=3,
                      left=TreeNode(val=5,
                                    left=TreeNode(val=6),
                                    right=TreeNode(val=2, left=TreeNode(7), right=TreeNode(4))),
                      right=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=8))
        ),
        p=TreeNode(val=5),
        q=TreeNode(val=4)
    )) == "5"


if __name__ == '__main__':
    main()
