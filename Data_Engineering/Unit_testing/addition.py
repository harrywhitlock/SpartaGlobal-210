def Add(a: str):


    if len(a) == 0:
        return 0
    if a[-1] == ',':
        return 'Error'

    b = a.replace('\n', '')
    c = b.replace(',', '')
    nums = [int(x) for x in c]
    print(nums)

    counter = 0
    for i in nums:
        counter += i

    print(counter)
    return counter

Add('5,4\n')