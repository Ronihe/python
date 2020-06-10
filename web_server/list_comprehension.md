## deep understanding of list comprehension
https://www.analyticsvidhya.com/blog/2016/01/python-tutorial-list-comprehension-examples/



definition:
`It is proposed to allow conditional construction of list literals using for and if clauses. They would nest in the same way for loops and if statements nest now.`
Python List Comprehension is an inline way of writing logic to search the existing list, do some operations on it, and return a new list.


LC will always return a result, whether you use the result or nor.
The iteration and conditional expressions can be nested with multiple instances.
Even the overall LC can be nested inside another LC.
Multiple variables can be iterated and manipulated at same time.



why:
1. you would start writing shorter and effective codes
2. your code will be executed faster

*List comprehension is 35% faster than normal for loop and 45% faster than map function*
when:

```
def eg2_for(sentence):
    vowels = 'aeiou'
    filtered_list = []
    for l in sentence:
        if l not in vowels:
            filtered_list.append(l)
    return ''.join(filtered_list)

def eg2_lc(sentence):
    vowels = 'aeiou'
    return ''.join([ l for l in sentence if l not in vowels])
```

```
def eg3_for(keys, values):
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = values[i]
    return dic

def eg3_lc(keys, values):
    return { keys[i] : values[i] for i in range(len(keys)) }

```


practice:


Nested list by list comprehension:
```
non_flat = [ [1,2,3], [4,5,6], [7,8] ]
[y for x in non_flat if len(x) > 2 for y in x]
result : [1,2,3,4,5,6]
```

COMPARE WITH FOR-LOOP AND MAP
- iterate through the list

        RunTime: FOR-loop is fastest. This is because in a for-loop, we need not return an element and just move onto next iteration using “pass”. In both LC and map, returning an element is necessary. The codes here return None. But still map takes more than twice the time. Intuitively, we can think that map involves a definite function call at each iteration which can be the reason behind the extra time. Let’s explore this at later stage.


- modify each element

RunTime: Here we see a similar trend as before. So, till the point of iterating and making slight modifications, for-loop is clear winner. LC is close to for-loop but again map takes around twice as much time. Note that here the difference between time will also depend on the complexity of the function being applied to each element.


- storing the result




- summary:
1. LC is fast and elegant in cases where simple expressions are involved. But if complex functions are required, map and LC would perform nearly the same
2. FOR-loop is bulkier in general, but it is fastest if storing is not required. So should be preferred in cases where we need to simply iterate and perform operations.





# Generator:
use very low memory requirements as they return numbers on the fly
```
def sum_list(N):
    return sum([x for x in range(N)])
def sum_gen(N):
    return sum((x for x in range(N)))
```

1. For small N, GE are relatively slower than LC. This is because of high multiple calls are required in GE but LC doesn’t require much space in memory.
2. For moderate N, GE perform almost the same as LC. GE requires high number of calls and LC needs large memory block.
3. For very high N, generators are drastically powerful as LC takes ~70 times of the time taken by GE. This is because LC uses up a very large chunk of RAM and processing becomes very slow.












