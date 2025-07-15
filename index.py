# Write your code here.
def get_args_and_kwargs(*args, **kwargs):
    
    if 'num' in kwargs:
        print('ayo')
    print((kwargs['num']))
    print(kwargs)
    print(args)

data = {'hello':'world', 'daddy':'come'}
get_args_and_kwargs(1,2,3,num=4)
