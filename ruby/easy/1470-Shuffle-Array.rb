def shuffle(nums, n)
  shuffled = []
  pointer1 = 0
  pointer2 = n
  while pointer1 < n && pointer2 < nums.length
    shuffled.push(nums[pointer1])
    shuffled.push(nums[pointer2])
    pointer1 += 1
    pointer2 += 1
  end
  shuffled
end

puts shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
puts shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
puts shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
