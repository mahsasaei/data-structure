class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []  # پشته ورودی
        self.stack_out = []  # پشته خروجی

    def enqueue(self, item):
        # اضافه کردن عنصر به پشته ورودی
        self.stack_in.append(item)

    def dequeue(self):
        # اگر پشته خروجی خالی است، تمام عناصر پشته ورودی را منتقل می‌کنیم
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # اگر پشته خروجی هنوز خالی است، یعنی صف خالی است
        if not self.stack_out:
            raise IndexError("dequeue from empty queue")
        
        # برداشتن عنصر از پشته خروجی
        return self.stack_out.pop()

# مثال استفاده
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
queue.enqueue(4)
print(queue.dequeue())  # 3
print(queue.dequeue())  # 4
