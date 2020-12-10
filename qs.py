class QS:

    @staticmethod
    def test(elements, start, end):
        if start >= end:
            return
        split_index = QS.split(elements, start, end)
        QS.test(elements, start, split_index-1)
        QS.test(elements, split_index+1, end)

    @staticmethod
    def split(elements, start, end):
        if start >= end:
            return
        pivot = elements[end]
        lower_val_index = start
        if elements[start] < pivot:
            lower_val_index += 1
        for i in range(start+1, end):
            if elements[i] < pivot:
                temp = elements[i]
                elements[i] = elements[lower_val_index]
                elements[lower_val_index] = temp
                lower_val_index += 1

        temp = elements[lower_val_index]
        elements[lower_val_index] = pivot
        elements[end] = temp
        return lower_val_index


data = [3, 5, 9, 0, 1, 2, 4]
QS.test(data, 0, 6)

print(data)












