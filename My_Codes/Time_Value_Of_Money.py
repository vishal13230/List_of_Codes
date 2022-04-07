from math import exp

def discrete_future_value(x, r, t):
	return x * (1 + r) ** t

def discrete_present_value(x, r, t):
	return x * (1 + r) ** -t

def continuous_future_value(x, r, t):
	return x * exp(r * t)

def continuous_present_value(x, r, t):
	return x * exp(-r * t)

if __name__ == "__main__":
	x = 100  # Value of investment in $
	r = 0.05 # Interest rate
	t = 5    # Years

	print("Future value of $100 in 5 years (Discrete Model): ", discrete_future_value(x, r, t))
	print("Future value of $100 in 5 years (Continuous Model): ", continuous_future_value(x, r, t))
	print("Present value of $100 in 5 years (Discrete Model): ", discrete_present_value(x, r, t))
	print("Present value of $100 in 5 years (Discrete Model): ", continuous_present_value(x, r, t))