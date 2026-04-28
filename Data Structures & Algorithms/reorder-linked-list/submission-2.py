class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # index nodes
        dic = {}
        i, curr = 0, head
        while curr:
            dic[i] = curr
            curr = curr.next
            i += 1

        left, right = 0, i - 1
        while left < right:
            leftnode = dic[left]
            rightnode = dic[right]

            # Save next of left BEFORE we change pointers
            temp = leftnode.next

            # Put right after left
            leftnode.next = rightnode

            if left + 1 == right:
                # Adjacent case: ... left -> right -> ...
                # right should end the list
                rightnode.next = None
                break
            else:
                # Normal case: right -> temp
                rightnode.next = temp
                # IMPORTANT: break the old link from the node before right
                # so it doesn't still point to right and create cycles.
                dic[right - 1].next = None

            left += 1
            right -= 1
