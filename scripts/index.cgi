#!/usr/bin/env ruby
require 'cgi'
print "Content-type: text/plain\n\n"
5.times { |i| puts "Hello world #{i}!"}
puts 'So many worlds there. :('

load 'controllers/home.cgi' 