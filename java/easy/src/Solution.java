import java.util.HashMap;

public class Solution {
	
	
	public int[] twoSum(int[] nums, int target) {
		int[] solution = {-1, -1};
		HashMap<Integer, Integer> hash = new HashMap<>();
		
		
		for (int i = 0; i < nums.length; i++) {
			int complement = target - nums[i];
			
			if (hash.get(complement) == null) {
				hash.put(nums[i], i);
			} else {
				solution[0] = hash.get(complement);
				solution[1] = i;
				return solution;
			}
		}
		
		return solution;
	}
	
	public int[] twoSumSlow(int[] nums, int target) {
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
