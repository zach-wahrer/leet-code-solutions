import unittest
from circular_queue import MyCircularQueue


class TestCircularQueue(unittest.TestCase):

    def test_instantiation(self):
        cir_queue = MyCircularQueue(3)
        self.assertEqual(cir_queue.length, 3)

    def test_empty_front(self):
        cir_queue = MyCircularQueue(3)
        self.assertEqual(cir_queue.Front(), -1)

    def test_empty_rear(self):
        cir_queue = MyCircularQueue(3)
        self.assertEqual(cir_queue.Front(), -1)

    def test_front(self):
        cir_queue = MyCircularQueue(3)
        cir_queue.enQueue('a')
        cir_queue.enQueue('b')
        self.assertEqual(cir_queue.Front(), 'a')

    def test_rear(self):
        cir_queue = MyCircularQueue(3)
        cir_queue.enQueue('a')
        cir_queue.enQueue('b')
        cir_queue.enQueue('c')
        self.assertEqual(cir_queue.Rear(), 'c')

    def test_is_empty(self):
        cir_queue = MyCircularQueue(3)
        self.assertTrue(cir_queue.isEmpty())

    def test_is_empty_false(self):
        cir_queue = MyCircularQueue(3)
        test = cir_queue.enQueue('a')
        self.assertFalse(cir_queue.isEmpty())

    def test_enqueue(self):
        cir_queue = MyCircularQueue(3)
        test = cir_queue.enQueue('a')
        self.assertTrue(test)
        self.assertEqual(cir_queue.queue[0], 'a')

    def test_too_many_enqueue(self):
        cir_queue = MyCircularQueue(3)
        cir_queue.enQueue('a')
        cir_queue.enQueue('a')
        cir_queue.enQueue('a')
        test = cir_queue.enQueue('a')
        self.assertFalse(test)

    def test_dequeue(self):
        cir_queue = MyCircularQueue(3)
        cir_queue.enQueue('a')
        cir_queue.enQueue('b')
        cir_queue.enQueue('c')
        test = cir_queue.deQueue()
        self.assertTrue(test)
        self.assertEqual(cir_queue.queue[0], None)
        self.assertEqual(cir_queue.current_size, 2)
        self.assertEqual(cir_queue.head, 1)
        self.assertEqual(cir_queue.tail, 0)

    def test_too_many_dequeue(self):
        cir_queue = MyCircularQueue(3)
        cir_queue.enQueue('a')
        cir_queue.enQueue('b')
        cir_queue.enQueue('c')
        cir_queue.deQueue()
        cir_queue.deQueue()
        cir_queue.deQueue()
        test = cir_queue.deQueue()
        self.assertFalse(test)

    def test_leet_test(self):
        test_results = []

        queue = MyCircularQueue(10)
        test_results.append(queue.enQueue(6))
        test_results.append(queue.Rear())
        test_results.append(queue.Rear())
        test_results.append(queue.deQueue())
        test_results.append(queue.enQueue(5))
        test_results.append(queue.Rear())
        test_results.append(queue.deQueue())
        test_results.append(queue.Front())
        test_results.append(queue.deQueue())
        test_results.append(queue.deQueue())
        test_results.append(queue.deQueue())

        self.assertEqual(test_results, [True, 6, 6, True, True, 5, True, -1, False, False, False])


if __name__ == "__main__":
    unittest.main()
