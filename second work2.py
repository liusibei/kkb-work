def print_string(*string1,sep = ' ',end = '\n'):
    string_list = list(string1)
    string2 = sep.join(string_list)
    return string2+end

print(print_string('This is a test')) #返回This is a test\n

print(print_string('This', 'is', 'a', 'test', sep = '-')) #返回This-is-a-test\n

print(print_string('This', 'is', 'a', 'test', sep = '-')) #返回This-is-a-test\n

print(print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.')) #返回This_is_a_test_,_Yes.
