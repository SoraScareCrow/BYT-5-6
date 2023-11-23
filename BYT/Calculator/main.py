
class Handler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None
class AddHandler(Handler):
    def handle(self, request):
        if request["operation"] == "add":
            return request["a"] + request["b"]
        return super().handle(request)

class SubtractHandler(Handler):
    def handle(self, request):
        if request["operation"] == "subtract":
            return request["a"] - request["b"]
        return super().handle(request)

class MultiplyHandler(Handler):
    def handle(self, request):
        if request["operation"] == "multiply":
            return request["a"] * request["b"]
        return super().handle(request)

class DivideHandler(Handler):
    def handle(self, request):
        if request["operation"] == "divide":
            return request["a"] / request["b"]
        return super().handle(request)

def main():
    add_handler = AddHandler()
    subtract_handler = SubtractHandler()
    multiply_handler = MultiplyHandler()
    divide_handler = DivideHandler()

    add_handler.set_next(subtract_handler).set_next(multiply_handler).set_next(divide_handler)

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    request = {"a": a, "b": b, "operation": operation}
    result = add_handler.handle(request)

    if result is not None:
        print(f"Result: {result}")
    else:
        print("Operation not supported")

if __name__ == "__main__":
    main()