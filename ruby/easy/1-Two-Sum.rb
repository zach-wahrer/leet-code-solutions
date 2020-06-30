def two_sums(nums, target)
  compliments = {}
  nums.each_with_index do |num, index|
    return [compliments[num], index] if compliments.has_key?(num)
    compliments[target - num] = index
  end
end

puts two_sums([2, 7, 11, 15], 9) == [0, 1]
puts two_sums([2, 7, 11, 15, 1, 13], 14) == [4, 5]
