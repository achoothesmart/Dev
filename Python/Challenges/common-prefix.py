
def common_prefix(lst: list):
    common = lst.pop(0)
    for s in lst:
        common = common[:len(s)]
        for i, c in enumerate(s):
            if (len(common) > i and common[i] != c) :
                common = common[:i]
                break
    return(common)

def test(test_name: str, in_lst: list, exp_str: str):
    act_res = common_prefix(in_lst)
    if exp_str == act_res:
        print(f'- Test "{test_name}" => Success')
    else:
        print(f'x Test "{test_name}" => Failure | Exp: {exp_str}, Act: {act_res}')
    
def run_tests():
     test(test_name='test1', in_lst=['welcome', 'welldone', 'wealth'], exp_str='we')
     test(test_name='test2', in_lst=['Alph', 'All', 'Ave'], exp_str='A')
     test(test_name='test3', in_lst=['wear', 'welldone', 'nice'], exp_str='')
     test(test_name='test4', in_lst=['kind', 'kindle', 'kill'], exp_str='ki')
     test(test_name='test5', in_lst=['ab', 'a'], exp_str='a')


if __name__ == '__main__':
    run_tests()
