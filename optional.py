import heapq

def merge_k_lists(lists):
    min_heap = []
    
    # Додаємо перші елементи кожного списку в мінімальну купу
    for i in range(len(lists)):
        if lists[i]:  # Переконуємося, що список не порожній
            heapq.heappush(min_heap, (lists[i][0], i, 0))  # (значення, індекс списку, індекс елемента)

    merged_list = []
    
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # Якщо є наступний елемент в тому ж списку, додаємо його в купу
        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1], list_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)