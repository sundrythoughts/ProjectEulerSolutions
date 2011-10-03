#!/usr/bin/env ruby

#SOLVED

#PROBLEM 1 (05 October 2001):
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we
#get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

class Array
    def sum
        self.inject{|sum,x| sum + x }
    end
end

def method1
    ans = 0
    (3...1000).each do |n|
        if n % 3 == 0 or n % 5 == 0
            ans += n
        end
    end
    puts "Method 1: " + ans.to_s
end

def method2
    ans = ((3...1000).step(3).to_a + (5...1000).step(5).to_a).uniq.sum
    puts "Method 2: " + ans.to_s
end

def method3
    ans = (3...1000).step(3).to_a.sum + (5...1000).step(5).to_a.sum - (15...1000).step(15).to_a.sum
    puts "Method 3: " + ans.to_s
end

method1
method2
method3