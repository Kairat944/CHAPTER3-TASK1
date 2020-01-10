str_ = input("Введите текст:")
len_ = len(str_)
text_s = text_b = 0
for i in str_:
    if 'a' <= i <= 'z':
        text_s +=1
    elif 'A' <= i <='Z':
        text_b +=1
print("%% строчных букв: %.2f" % (text_s/len_ * 100))
print("%% прописные букв: %.2f" % (text_b/len_ * 100))