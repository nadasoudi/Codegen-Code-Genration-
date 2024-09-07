def mod_even_odd(head):
    odd_list = []
    even_list = []
    odd_list_index = 0
    even_list_index = 0
    while head:
        if head.data % 2 == 0:
            even_list.append(head.data)
            even_list_index += 1
        else:
            odd_list.append(head.data)
            odd_list_index +=