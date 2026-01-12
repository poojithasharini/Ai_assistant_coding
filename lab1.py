'''n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print(0)
else:
    a, b = 0, 1
    print(a, end=" ")
    for i in range(n - 1):
        print(b, end=" ")
        a, b = b, a + b
    print()'''

'''n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number")
else:
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()'''


def fibonacci_terms(n):
    #Return the first n terms of the Fibonacci sequence as a list.
    """AI-assisted: Logic:
    Start from a=0, b=1 and iterate n times. On each iteration append the
    current value of a to the result list, then update a,b to the next pair
    using the simultaneous assignment a, b = b, a + b. This uses a single loop
    and avoids nested loops or repeated computations.
    """
    '''if n <= 0:
        return []
    seq = []
    a, b = 0, 1
    for _ in range(n):          # single loop, n iterations
        seq.append(a)
        a, b = b, a + b         # update to next Fibonacci pair
    return seq

if __name__ == "__main__":
    # Accept user input for n in the main program
    try:
        n = int(input("Enter the number of terms: "))
    except ValueError:
        print("Please enter a positive number")
    else:
        if n <= 0:
            print("Please enter a positive number")
        else:
            terms = fibonacci_terms(n)
            # Print terms on one line separated by spaces (trailing space preserved)
            if terms:
                print(*terms, end=" ")
            print()'''
    
    # Comparative Analysis Report: Fibonacci Implementations
    '''comparison_report = """
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║         FIBONACCI IMPLEMENTATIONS: COMPARATIVE ANALYSIS REPORT              ║
    ╚════════════════════════════════════════════════════════════════════════════╝

    ┌─────────────────────────────────────────────────────────────────────────────┐
    │ COMPARISON CRITERIA        │ TASK 1 (Direct Loop)  │ TASK 3 (Function-Based)│
    ├─────────────────────────────────────────────────────────────────────────────┤
    │ Code Clarity              │ ⭐⭐⭐                 │ ⭐⭐⭐⭐⭐             │
    │ (Readability & Structure) │ Simple but inline     │ Well-documented,       │
    │                           │ logic scattered       │ logical separation     │
    ├─────────────────────────────────────────────────────────────────────────────┤
    │ Reusability               │ ⭐⭐                   │ ⭐⭐⭐⭐⭐             │
    │ (Code Reuse & DRY)        │ Must rewrite logic    │ Call function multiple │
    │                           │ for each use          │ times without duplication│
    ├─────────────────────────────────────────────────────────────────────────────┤
    │ Ease of Debugging         │ ⭐⭐⭐                 │ ⭐⭐⭐⭐⭐             │
    │ (Error Tracking)          │ Debug inline code     │ Isolated function scope│
    │                           │ mixed with I/O        │ simplifies bug isolation│
    ├─────────────────────────────────────────────────────────────────────────────┤
    │ Suitability for Larger    │ ⭐⭐                   │ ⭐⭐⭐⭐⭐             │
    │ Systems (Scalability)     │ Poor modularity       │ Highly modular,        │
    │                           │ difficult integration │ easy to integrate      │
    ├─────────────────────────────────────────────────────────────────────────────┤
    │ Testing Capability        │ ⭐⭐                   │ ⭐⭐⭐⭐⭐             │
    │ (Unit Testing)            │ Hard to unit test     │ Easily testable via    │
    │                           │ (I/O coupled)        │ function calls         │
    ├─────────────────────────────────────────────────────────────────────────────┤
    │ Maintenance               │ ⭐⭐                   │ ⭐⭐⭐⭐⭐             │
    │ (Long-term Support)       │ Changes scatter       │ Single point of change │
    │                           │ across code           │ maintains consistency  │
    └─────────────────────────────────────────────────────────────────────────────┘

    KEY FINDINGS:

    ✓ Task 1 Strengths:
        • Quick implementation for simple scripts
        • Minimal abstraction overhead
        • Suitable for one-off calculations

    ✗ Task 1 Weaknesses:
        • Logic tightly coupled with I/O
        • Difficult to test independently
        • Poor code reuse across modules
        • Maintenance nightmare in larger projects

    ✓ Task 3 Strengths:
        • Clean separation of concerns (logic vs. I/O)
        • Highly reusable function
        • Easy unit testing without side effects
        • Scalable to larger systems
        • Self-documenting via docstrings
        • Single responsibility principle

    ✗ Task 3 Weaknesses:
        • Slight overhead in function calls
        • May be overkill for trivial scripts

    RECOMMENDATION:

    For software engineering best practices, Task 3 (Function-Based) is SUPERIOR.
    It adheres to SOLID principles (Single Responsibility, DRY), enables testing,
    and scales effectively. Task 1 is acceptable only for throwaway scripts.
    """

    print(comparison_report)'''

    # ITERATIVE IMPLEMENTATION
    def fibonacci_iterative(n):
        """
        Iterative Fibonacci: O(n) time, O(1) space.
        Execution: Start with a=0, b=1, iterate n times updating pair.
        """
        if n <= 0:
            return []
        seq = []
        a, b = 0, 1
        for _ in range(n):
            seq.append(a)
            a, b = b, a + b
        return seq


    # RECURSIVE IMPLEMENTATION
    def fibonacci_recursive(n):
        """
        Recursive Fibonacci: O(2^n) time, O(n) space (call stack).
        Execution: Base cases (0→0, 1→1), else fib(n-1) + fib(n-2).
        WARNING: Exponential complexity; avoid for n > 35.
        """
        if n <= 0:
            return []
        
        def fib(k):
            if k <= 1:
                return k
            return fib(k - 1) + fib(k - 2)
        
        return [fib(i) for i in range(n)]


    # COMPARATIVE ANALYSIS
    analysis = """
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║            ITERATIVE vs RECURSIVE FIBONACCI: ALGORITHM COMPARISON           ║
    ╚════════════════════════════════════════════════════════════════════════════╝

    ITERATIVE APPROACH:
      • Time Complexity:  O(n) - single pass through n iterations
      • Space Complexity: O(1) auxiliary (or O(n) if storing result list)
      • Performance: Linear growth, handles n=1000000 instantly
      • Strengths: Efficient, predictable, no stack overflow risk

    RECURSIVE APPROACH:
      • Time Complexity:  O(2^n) - exponential branching, massive redundant calls
      • Space Complexity: O(n) call stack depth + O(n) for memoization
      • Performance: Exponential slowdown; n=40 takes ~seconds, n=50 impractical
      • Weaknesses: Redundant computations (fib(3) calculated 5+ times for fib(5))

    WHEN TO AVOID RECURSION:
      ✗ Large n values (n > 35): Stack overflow or timeout
      ✗ Real-time systems: Unpredictable performance
      ✗ No memoization available: Exponential complexity explodes

    RECOMMENDATION: Use iterative for Fibonacci. Recursion only viable with
    memoization/dynamic programming for medium n (≤40).
    """

    print(analysis)
    print("\nExample - n=10:")
    print(f"Iterative:  {fibonacci_iterative(10)}")
    print(f"Recursive:  {fibonacci_recursive(10)}")



    