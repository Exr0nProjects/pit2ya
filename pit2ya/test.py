class gen(): # https://stackoverflow.com/q/34073370
    def __iter__(self):
        for i in range(20):
            yield i

# I want to partially consume in the first loop and finish in the second
my_gen_2 = gen().__iter__()
for i in my_gen_2:  # imagine this is the internal implementation of the library function
    print(i)
    if i > 10:      # the real break condition is when iterfzf recieves user input
        break

for i in my_gen_2:  # i'd like to process the remaining elements instead of starting over
    print('p2', i)

# # the confusion boils down to this
# my_gen = gen()
# for i in my_gen.__iter__():
#     print(i)    # prints 1 through 20 as expected
# for i in my_gen.__iter__():
#     print('part two', i)    # prints something, even though the generator should have been "consumed"?

