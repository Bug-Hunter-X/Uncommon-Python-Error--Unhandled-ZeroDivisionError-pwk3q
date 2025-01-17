def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return 1 / a  # Potential ZeroDivisionError
        return a + b
    except ZeroDivisionError:
        return float('inf')  # Handle the error gracefully
    except Exception as e:
      return f"An unexpected error occurred: {e}"