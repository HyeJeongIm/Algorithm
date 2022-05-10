def solution(phone_book):
  phone_book.sort()

  for i in range(len(phone_book)):
    num = phone_book[i]

    for j in range(i + 1, len(phone_book)):
      if num == phone_book[j][:len(num)]:
        return False
  return True
