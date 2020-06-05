import java.util.Arrays;

import org.junit.Assert;

import org.junit.jupiter.api.Test;

class TwoSumTest {
	
	@Test
	void testFourNums() {
		int[] nums = {2, 7, 11, 15};
		int target = 9;
		int[] solution = {0, 1};
		
		Solution solve = new Solution();
		int[] proposedSolution = solve.twoSum(nums, target);
		Assert.assertArrayEquals(proposedSolution, solution);
	}
	
	@Test
	void testTwoNums() {
		int[] nums = {3, 3};
		int target = 6;
		int[] solution = {0, 1};
		
		Solution solve = new Solution();
		System.out.println(Arrays.toString(solve.twoSum(nums, target)));
		int[] proposedSolution = solve.twoSum(nums, target);
		Assert.assertArrayEquals(proposedSolution, solution);
	}
	
	@Test
	void testTenNums() {
		int[] nums = {1, 4, 8, 13, 19, 3, 8, 2, 99, 66};
		int target = 100;
		int[] solution = {0, 8};
		
		Solution solve = new Solution();
		int[] proposedSolution = solve.twoSum(nums, target);
		Assert.assertArrayEquals(proposedSolution, solution);
	}
	
	@Test
	void testSixNums() {
		int[] nums = {10, 13, 1, 2, 3, 7};
		int target = 10;
		int[] solution = {4, 5};
		
		Solution solve = new Solution();
		int[] proposedSolution = solve.twoSum(nums, target);
		Assert.assertArrayEquals(proposedSolution, solution);
	}

}
