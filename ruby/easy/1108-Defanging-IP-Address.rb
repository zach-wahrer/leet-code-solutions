def defang_i_paddr(address)
  defanged = ''
  address.split('').each do |char|
    char != '.' ? defanged += char : defanged += '[.]'
  end
  defanged
end

puts defang_i_paddr('1.1.1.1') == '1[.]1[.]1[.]1'
puts defang_i_paddr('255.100.50.0') == '255[.]100[.]50[.]0'
