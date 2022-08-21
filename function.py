def input_user(start, end):
	if start < end:
		end, start = start, end
	return start - end

start_input = int(input())
end_input = int(input())

print(input_user(start_input, end_input))
