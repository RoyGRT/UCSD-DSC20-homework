

def square(x):
    return x*x

def negate(x):
    return -x

def identity(x):
    return x

def triple(x):
    return 3*x

def increment(x):
    return x+1

def increment_by(x, step):
    return x+step


# Question 1.1
def name_in_order(names):
    """ Return a list where each 'Bruno' is followed by 'Mars'
    >>> name_in_order(["I", "Bruno", "like", "Mars"])
    ['I', 'Bruno', 'Mars', 'like']
    >>> name_in_order(["Marina", "Langlois"])
    ['Marina', 'Langlois']
    >>> name_in_order(["Rock", "Bruno", "Stars", "Bruno", "Paper",\
     "Mars", "Scissors", "Mars"])
    ['Rock', 'Bruno', 'Mars', 'Bruno', 'Mars', 'Stars', 'Scissors', 'Paper']
    >>> name_in_order(["Roy", "loves", "Bruno", "the", "Mars", "most"])
    ['Roy', 'loves', 'Bruno', 'Mars', 'the', 'most']
    >>> name_in_order(["Bruno", "magic", "twenty", "four", "k", "Mars"])
    ['Bruno', 'Mars', 'twenty', 'four', 'k', 'magic']
    >>> name_in_order(["who", "is", "Bruno", "anyway", "Mars"])
    ['who', 'is', 'Bruno', 'Mars', 'anyway']
    """
    bruno_pos = 0
    mars_pos = 0
    for i in range(len(names)):
    	if names[i]=='Bruno':
    		bruno_pos = i
    		for j in range(len(names)-i):
    			if names[i+j]=='Mars':
    				mars_pos = i+j
    				if names[i+1]!='Mars':
    					temp = names[i+1]
    					names[i+1] = names[j+i]
    					names[j+i] = temp
    					
    return names



# Question 1.2
def pick_sort(lst):
    """Returns a sorted version of lst.
    >>> pick_sort([5, 1, 7, 3])
    [1, 3, 5, 7]
    >>> pick_sort([5, 1, 5, 7, 3])
    [1, 3, 5, 5, 7]
    >>> pick_sort([3, 9, 2, 0, 10])
    [0, 2, 3, 9, 10]
    >>> pick_sort([-1, -10, 0, -3, 2])
    [-10, -3, -1, 0, 2]
    >>> pick_sort([10320, 9482, 21023, -2034, 3233, 394])
    [-2034, 394, 3233, 9482, 10320, 21023]
    """

    list_end = 0-1
    for i in range(len(lst)-1,list_end,-1):
    	max_num = i
    	for j in range(i):
    		if lst[j] > lst[max_num]:
    			max_num = j
    	temp = lst[i]

    	lst[i] = lst[max_num]
    	
    	lst[max_num] = temp
    return lst




# Functions as Arguments

# Question 2.1:

def apply_twice(f, x):
    """Apply f to the result of applying f to x"
    >>> apply_twice(square, 3)
    81
    >>> apply_twice(square, 5)
    625
    >>> apply_twice(triple, 5)
    45
    >>> apply_twice(increment, 24)
    26
    >>> apply_twice(square,6)
    1296
    >>> apply_twice(triple, 20)
    180
    >>> apply_twice(increment, -1)
    1
    >>> apply_twice(square, 2)
    16

    """
    assert callable(f),'f must be a function!'
    assert isinstance(x,int),"x must be an integer!"

    return f(f(x))


# Question 2.2:

def apply_n_times(f, x, n, step=None):
    """Apply function f to x n times.

    >>> apply_n_times(increment_by, 2, 1, 10)
    12
    >>> apply_n_times(increment_by, 2, 3, 5)
    17
    >>> apply_n_times(increment_by, 3, 4, 7)
    31
    >>> apply_n_times(square, 2, 3)
    256
    >>> apply_n_times(triple, 3, 4)
    243
    >>> apply_n_times(square, 5, 3)
    390625
    >>> apply_n_times(increment_by, 5, 29, 45)
    1310
    >>> apply_n_times(increment_by, 8, 2, 10)
    28
    >>> apply_n_times(triple, 1, 4)
    81
    >>> apply_n_times(square, 2, 0)
    2
    """
    assert callable(f),'f must be a function!'
    assert isinstance(x,int),"x must be an integer!"
    assert isinstance(n,int),"n must be an integer!"


    for i in range(n):
    	if f == increment_by:
    		x = f(x,step)
    	else:
    		x = f(x)
    return x


# Functions as Returned Values
# Question 2.3

def king_argument(f, x):
    """Returns a function that returns a string indicating what
    function is a "king of the argument".

    >>> num1 = king_argument(identity, 1)
    >>> num1(increment)
    'Second function is a king of the argument: 1'
    >>> num1(triple)
    'King cannot be determined'
    >>> num2 = king_argument(increment, 1)
    >>> num2(square)
    'First function is a king of the argument: 1'
    >>> num3 = king_argument(triple, 6)
    >>> num3(square)
    'Second function is a king of the argument: 6'
    >>> num4 = king_argument(increment, 5)
    >>> num4(square)
    'King cannot be determined'
    >>> num5 = king_argument(increment, 1)
    >>> num5(triple)
    'King cannot be determined'
    """

    assert callable(f),'f must be a function!'
    assert isinstance(x,int),"x must be an integer!"

    def second_argument(sec):
    	assert callable(sec),"second argument must be a function!"

    	if sec(x) == f(x)*2:
    		return 'Second function is a king of the argument: '+ str(x)

    	elif sec(x)*2 == f(x):
    		return 'First function is a king of the argument: '+ str(x)

    	else:
    		return 'King cannot be determined'

    return second_argument




# Question 2.4

def picky_function(f, g, num):
    """Returns the function h where:

    h(x) = f(x) if x > num,
           g(x) otherwise

    >>> abs_value = picky_function(negate, identity, 0)
    >>> abs_value(1)
    -1
    >>> abs_value(-87)
    -87
    >>> trip_sq = picky_function(triple, square, 3)
    >>> trip_sq(4)
    12
    >>> trip_sq(2)
    4
    >>> id_square = picky_function(identity, square, 9)
    >>> id_square(11)
    11
    >>> id_square(8)
    64
    >>> incre_square = picky_function(increment, square, 1)
    >>> incre_square(11)
    12
    """
    assert callable(f),'f must be a function!'
    assert callable(g),'g must be a function!'
    assert isinstance(num,int),"num must be an integer!"

    def inner_function(x):
    	if x > num:
    		return f(x)
    	else:
    		return g(x)
    return inner_function


# Question 2.5

def higher_order_input(x):
    """ Return functions given the guidelines in the hw2 write-up

    >>> string_func = higher_order_input('Halicioglu')
    >>> string_func(6)
    HALICIoglu
    HALICIoglu
    HALICIoglu
    HALICIoglu
    HALICIoglu
    HALICIoglu
    'HALICIoglu'
    >>> string_func(12)
    'Halicioglu'
    >>> int_func = higher_order_input(15)
    >>> int_func(increment, 6)
    '$16000000'
    >>> list_func = higher_order_input([1, 2, 3, 6, 9])
    >>> list_func(square, 3)
    [1, 4, 9, 6, 9]
    >>> rand_func = higher_order_input(True)
    >>> rand_func(increment, 5)
    6
    >>> rand_func = higher_order_input(False)
    >>> rand_func(square, 6)
    36
    >>> rand_func = higher_order_input(True)
    >>> rand_func(increment, 5)
    6
    >>> list_func = higher_order_input([2, 5, 7, 2, 1])
    >>> list_func(increment, 5)
    [3, 6, 8, 3, 2]
    """
    
    if type(x) == str:
        def upper_case_and_print(n):
        	if n <= len(x):
        		string_list = list(x)
        		for i in range(n):
        			string_list[i] = string_list[i].upper()

        		new_str = ''.join(string_list)
        		for i in range(n):
        			print(new_str)
        		return new_str
        	return x

        return upper_case_and_print

    elif type(x) == int:
        def data_science_salary(f, n):
            num = f(x)
            for i in range(n):
            	num = num*10
            return '$'+str(num)
        return data_science_salary

    elif type(x) == list:
        def apply_f_to_elements(f, n):
            if n <= len(x):
            	for i in range(n):
            		x[i] = f(x[i])
            	return x
            else:
            	return x[::-1]
        return apply_f_to_elements

    else:
        def other(f, n):
            return f(n)
        return other

    
