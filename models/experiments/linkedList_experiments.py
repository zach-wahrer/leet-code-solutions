from experimental_linkedList import CircleNode, ListNode

# nums = [i for i in range(10)]
#
# list_of_list_nodes = ListNode.build([ListNode.build(nums),
#                                      ListNode.build(nums),
#                                      ListNode.build(nums),
#                                      ListNode.build(nums),
#                                      ListNode.build(nums)])
#
# print(list_of_list_nodes.val.next.next.to_list())
# print(list_of_list_nodes.next.next.val.length())

# circle = CircleNode.build([1, 2, 3])
# circle2 = CircleNode.build([1, 2, 3])
# print(circle == circle2)

circle_list = CircleNode.build([i for i in range(100)])
linked_list = ListNode.build([i for i in range(100)])


def check_for_circular(head: ListNode) -> bool:
    move_one = head
    move_two = head.next.next
    while True:
        if not move_one or not move_two:
            return False
        elif move_one == move_two:
            return True
        else:
            move_one = move_one.next
            move_two = move_two.next.next


print("Linked list: " + str(check_for_circular(linked_list)))
print("Circle list: " + str(check_for_circular(circle_list)))
