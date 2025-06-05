# Evaluating F1-score function
def f1_score (tp, fn, fp):

    # check input's condition
    inp = {'tp_value': tp, 'fn_value': fn, 'fp_value': fp}
    for key, value in inp.items():
        if type(value) is not int:
            print(f'{key} must be an integer')
            return
        elif value < 0:
            print(f'{key} must be greater than or equal to 0')
            return
    # When tp = 0 f1-score does not exist but to avoid raising error return 0 value for all.
    if tp == 0:
        return (0, 0, 0)
    if (tp + fp) == 0 or (tp +fn):
        print('precision/ recall does not exist')
   
    #evaluate precision, recall, f1-score
    precision = tp/(tp +fp)
    recall = tp/ (tp + fn)
    f1 = 2*precision*recall/(precision + recall)
    return(round(precision,3), round(recall,3), round(f1,3))
    

#Test case f1_score function
tp = 2
fn = 5
fp = 4

output = f1_score(tp, fn, fp)
print(output)

print('=====================================================')
print('=====================================================')

# Define some activation functions

def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True

#Test
print(is_number('a'))

import math

#define activation functions: sigmoid, reLu, eLu
def activate (x, func):
    if is_number(x) == False:
        print ('x must be a number')
        return
    func_lst = ['sigmoid', 'relu', 'elu']
    if func not in func_lst:
        print(f'{func} is not supported')
        return
    
    if func == 'sigmoid':
        return 1/(1+math.exp(-x))
    
    if func == 'relu':
        if x <= 0:
            return 0
        else:
            return x
        
    if func == 'elu':
        if x <= 0:
            return 0.01*(math.exp(x)-1)
        else:
            return x
    

#Test
func = 'elu'
x = -1

print(activate(x, func))
    
print('=====================================================')
print('=====================================================')

#Loss function MSE, MAE, RMSE
import random
def loss_function(name = 'mse', samples = 5):
    if type(samples) != int and samples <= 0:
        print ('samples must be positive integer')
        return
    else:
        print(f'Note: There are {samples} pair y and y hat:')
    
    #Create y and y_hat by random in range (0, 10)
    y = []
    y_hat = []
    
    for i in range(samples):
        y.append(random.uniform(0,10))
        y_hat.append(random.uniform(0, 10))
    
    for k in range(samples):
        print(f'Sample {k+1}: y: {y[k]:.3f} - y hat : {y_hat[k]:.3f}')
    
    #Caculate:
    different = [(y[m] - y_hat[m]) for m in range(samples)]
    # print(different)
    total = 0
            
    if name == 'mse':
        for j in range(samples):
            total += different[j]**2
        return (f'MSE loss value: {(1/samples*total):.3f}')
    
    if name == 'mae':
        for l in range(samples):
            total += math.fabs(different[l])
        return (f'MAE loss value: {(1/samples*total):.3f}')
    
    if name == 'rmse':
        for n in range(samples):
            total += different[n]**2
        return (f'RMSE loss value: {(math.sqrt(1/samples*total)):.3f}')
    


#Test
n_samples = 5
func_name = 'rmse'

print(loss_function(func_name, n_samples))

print('=====================================================')
print('=====================================================')
print('ESTIMATE sin(x), cos(x), sinh(x), cosh(x)\n')


def factorial(x):
    result = 1
    for i in range(1, (x+1)):
        result *= i
    return result

#Test
print(factorial(0))

def estimate_cos(x, n = 10):
    result = 0
    for i in range(n+1):
        result += (-1)**i * x**(2*i)/factorial(2*i)
    return round(result, 3)


#test
print(estimate_cos(3.14, 5))

def estimate_sin(x, n = 10):
    result = 0
    for i in range(n + 1):
        result += (-1)**i* x**(2*i+1)/factorial(2*i +1)
    return round(result, 5)

#test
print(estimate_sin(3.14))


def estimate_sinh(x, n = 10):
    result = 0
    for i in range(n+1):
        result += x**(2*i +1)/factorial(2*i+1)
    return round(result, 3)

def estimate_cosh(x, n = 10):
    result = 0
    for i in range (n + 1):
        result += x**(2*i)/factorial(2*i)
    return round(result, 3)

#test
print(estimate_cosh(3.14))






