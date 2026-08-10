func isValid(s string) bool {
	if len(s)%2 != 0 {
		return false
	}

	tokens := []rune(s)
	var stack []rune
	for _, t := range tokens {
		switch t {
		case '(', '[', '{':
			stack = append([]rune{t}, stack...)
		case ')', ']', '}':
			if len(stack) == 0 {
                return false
            }
			if t == ')' && stack[0] != '(' {
				return false
			}
			if t == ']' && stack[0] != '[' {
				return false
			}
			if t == ')' && stack[0] != '(' {
				return false
			}
			stack = stack[1:]
		}
	}
	return len(stack) == 0
}
