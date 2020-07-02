

def contains_duplicate(nums)
  require 'set'
  nums_set = nums.to_set
  return !(nums.length == nums_set.length)
end

puts contains_duplicate([1, 2, 3, 1]) == true
puts contains_duplicate([1, 2, 3, 4]) == false
puts contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == true
