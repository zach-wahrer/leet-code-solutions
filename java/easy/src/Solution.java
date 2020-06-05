
public class Solution {
	public int[] twoSum(int[] nums, int target) {
		if (nums.length == 2) {
			int[] solution = {0, 1};
			return solution;
		}
		
		int[] solution = {-1, -1};
		int p1 = 0;
		int p2 = 1;
		
		while (p1 < nums.length - 1) {
			while (p2 < nums.length) {
				if (nums[p1] + nums[p2] == target) {
					solution[0] = p1;
					solution[1] = p2;
					return solution;
				}
				p2 += 1;
			}
			p1 += 1;
			p2 = p1 + 1;
			
		}
		
		return solution;
	}
}
