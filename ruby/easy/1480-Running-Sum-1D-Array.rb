def running_sum(nums)
  result = [nums[0]]
  index = 1
  while index < nums.length
    result.push(result[index - 1] + nums[index])
    index += 1
  end
  result
end

puts running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
puts running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
