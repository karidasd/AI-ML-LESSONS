# Μια απλή αναπαράσταση του πώς η AI "βλέπει" έναν αριθμό
# Το 1 μοιάζει με μια κάθετη γραμμή στο κέντρο

digit_1 = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

def recognize_digit(matrix):
    # Απλός αλγόριθμος που μετράει τα "1" στην κεντρική στήλη
    center_column_sum = sum(matrix[row][2] for row in range(5))
    
    if center_column_sum == 5:
        return "Η AI αναγνώρισε τον αριθμό: 1"
    else:
        return "Ο αριθμός δεν αναγνωρίστηκε."

print(recognize_digit(digit_1))
