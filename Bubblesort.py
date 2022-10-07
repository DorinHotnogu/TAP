def bubbleSort(list):
  isSwapped = True

  while(isSwapped):
    isSwapped = False
    for i in range(len(list) - 1):
      if(list[i] > list[i + 1]):
        isSwapped = True
        swap(list, i)

def swap(list, curr_index):
   temp = list[curr_index];
   list[curr_index] = list[curr_index + 1];
   list[curr_index + 1] = temp;

list = [ 19, 1, 9, 3, 10, 13, 42, 89 ]

bubbleSort(list)
print('lista sortata este:')
print(list)
