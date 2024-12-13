class Stack:
    def __init__(self):
        # ایجاد یک لیست خالی برای نگهداری داده‌ها
        self.items = []
    
    def push(self, item):
        # اضافه کردن عنصر به پشته
        self.items.append(item)
    
    def pop(self):
        # حذف و بازگشت آخرین عنصر پشته
        if not self.is_empty():
            return self.items.pop()
        else:
            return "پشته خالی است"
    
    def peek(self):
        # مشاهده آخرین عنصر پشته بدون حذف آن
        if not self.is_empty():
            return self.items[-1]
        else:
            return "پشته خالی است"
    
    def is_empty(self):
        # بررسی اینکه آیا پشته خالی است
        return len(self.items) == 0

# استفاده از پشته
stack = Stack()

# اضافه کردن عناصر به پشته
stack.push(1)
stack.push(2)
stack.push(3)

# نمایش آخرین عنصر پشته
print(stack.peek())  # خروجی: 3

# حذف آخرین عنصر پشته
print(stack.pop())  # خروجی: 3

# نمایش وضعیت خالی بودن پشته
print(stack.is_empty())  # خروجی: False
