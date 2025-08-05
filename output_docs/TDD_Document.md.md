# Technical Design Document: Iterative Factorial Calculation

## 1. Introduction

This document outlines the technical design for a Python function that calculates the factorial of a non-negative integer using an iterative approach. It details the function's purpose, components, data models, API, dependencies, and constraints.

## 2. Purpose

The primary purpose of this component is to provide a reliable and efficient function for calculating the factorial of a non-negative integer. This function can be used as a building block in other mathematical or computational tasks.

## 3. Components

### 3.1 `factorial_iterative` Function

This function is the core component of the design. It takes a non-negative integer as input and returns its factorial.

#### 3.1.1. Function Signature

```python
def factorial_iterative(n):
    pass
```

#### 3.1.2. Input Parameters

*   `n` (int): The non-negative integer for which to calculate the factorial.

#### 3.1.3. Return Value

*   int or str: The factorial of `n` as an integer. Returns an error message string if n is negative.

#### 3.1.4. Algorithm

1.  **Input Validation:** Check if `n` is negative. If so, return "Factorial is not defined for negative numbers."
2.  **Base Case:** If `n` is 0 or 1, return 1.
3.  **Iterative Calculation:**
    *   Initialize `result` to 1.
    *   Iterate from `i = 1` to `n`:
        *   Multiply `result` by `i`.
4.  **Return:** Return the calculated `result`.


## 4. Data Models

There are no complex data models for this function. The primary data type used is the integer (`int`).

## 5. API

The API consists of a single function, `factorial_iterative`, as described in Section 3.

## 6. Dependencies

This function has no external dependencies. It relies only on standard Python features.

## 7. Constraints

*   The input 'n' must be an integer.
*   The function should handle negative integer inputs gracefully by returning an appropriate error message.
*   The function must be able to accurately compute factorials for non-negative integers within the representable range of the integer data type.

## 8. Error Handling

*   **Negative Input:** If the input `n` is negative, the function returns the string "Factorial is not defined for negative numbers."

## 9. Example Usage

```python
number = 5
print(f"The factorial of {number} is {factorial_iterative(number)}")
```

## 10. Future Considerations

*   **Exception Handling:**  Implement more robust error handling using exceptions instead of returning error messages as strings.
*   **Large Numbers:**  For very large values of `n`, consider using a library that supports arbitrary-precision arithmetic to avoid integer overflow.
*   **Recursion:** A recursive implementation could be provided as an alternative, offering a different approach to the problem. However, iterative approach avoids stack overflow for large values of n.