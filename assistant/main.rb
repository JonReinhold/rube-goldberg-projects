# take arguments from CLI to determine process

puts "Debug start."

name = `ls`
puts name

cli_args = ARGV
puts cli_args

class CLI
	def run_py
	
	end
	
	def run_ahk
	
	end
	
	def test_function
	return "CLI.test_function works!"
	end
end

inst = CLI.new
puts inst.test_function()

puts "Debug end."


