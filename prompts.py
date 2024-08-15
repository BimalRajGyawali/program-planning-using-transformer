task = """
First, write a function reserve-seats that takes four parameters: i) the theater hall, ii) the row in which the seats are, iii) the first seat that should be reserved, and iv) the number of seats that should be reserved overall. Starting from the row specified as the second parameter, all required seats (fourth parameter) should be reserved to the right of the specified seat (third parameter). In the given example, the first parameter is 4 (fourth row), the second is 2 (starting with a seat in column 2), and the number of seats that should be reserved is 2. The seats should be marked as reserved if available (see exceptions below). This function returns the modified theater hall after the reservation. Even if the reservation is not possible (see exceptions below), the input lecture hall should be returned.

You should consider the following cases:

- The reservation cannot be processed if one of the requested seats is unavailable (= already reserved).
- If there are not enough seats in a row, no seats should be reserved (for example, if seven seats should be reserved beginning with seat 5).
"""

llm_problem_statement = """

<p> A theater hall may have the following structure</p>
<p>
[[1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 1, 0, 0, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [2, 2, 2, 2, 2, 2, 2]] </p>

<p>For this problem, a 0 represents a reserved seat, a 1 represents an available regular seat, and a 2 represents an available premium seat. Students might assume a different representation of seats, please adapt their assumed representation to the one given here.</p>

<p>A student is providing a programming plan for a function called <code>student_plan</code></p>
"""

# This plan fails test as it does not check the edge case: If there are not enough seats in a row, no seats should be reserved
plan = """
Go through each row. 

For each row:
- Goto a seat s
- If a single seat is requested and the requested seat is reserved, abort.
- When more than one seats are requested, check from seat s to s + count, if any is reserved, abort.
- Reserve a seat if both above mentioned conditions failed.
"""

PLAN_TO_PY_INSTRUCTIONS = """
Translate each and every step of the student's plan into a step within a single function.

Format your output as a Python *.py file.
Each code block that corresponds to a step should be preceded by a comment that contains only the step number, e.g., "# Step 1".
If your output spans multiple messages, please ensure that the next message begins with the correct indentation.
Do not include any text that breaks this format. Be sure to not include invalid escape sequences.
End the file with the string ---END OF PY FILE--- on its own line.

DO NOT FIX STUDENT ERRORS. If student errors are corrected, the student will be put to death.
You may only output correct code if the student's plan is completely correct.

The function MUST produce incorrect code unless the student's plan is completely correct.

DO NOT INCLUDE ANY FUNCTIONS THAT THE STUDENT DOESNT DIRECTLY MENTION. DO NOT OUTPUT TEST CODE OR EXAMPLE OR USAGE.

"""


def build_prompt_for_plan_feedback_on_failure(student_plan, llm_generated_code, failed_unit_test_output):
    return f"""
Here is the programming plan a student wrote.
=============
{student_plan}
=============

The corresponding code generated by LLM for the student's plan is given below.
==============
{llm_generated_code}
=============

While running the code, the unit test failed. The failed unit test is given below.
=============
{failed_unit_test_output}
=============

The unit test failed because the plan might have missed some edge cases or the entire plan was wrong. Here is the task for which the student wrote the plan.
=============
{task}
==========

Take a deep breath and proceed.

Act like a programming teacher, and give feedback to the student on their plan. 

REMEMBER IF YOU PROVIDE THE SOLUTION, THE STUDENT WILL BE EXPELLED FROM THE SCHOOL.

Provide the FEEDBACK only on the work done by the student. DO NOT GIVE FEEDBACK ON RIGHT THINGS. 
Student should be able to iterate on plan after knowing the mistakes.


Don't give any hints or solution or code. JUST PLAIN FEEDBACK ON PLAN, NOT ON THE CODE. STUDENT IS UNAWARE OF CODE.

Don't praise on the right things. Be clear and concise on what went wrong.

DO NOT EXPOSE ANY CODING DETAILS. 

"""


# We can parse it to select only relevant areas
test_error = """
Error
Traceback (most recent call last):
  File , line 33, in test_multiple_seat_reservation_failure_not_enough_space
    self.assertFalse(reserve_seats(theater_hall, 2, 2, 4))  # Not enough space at the end
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File , line 15, in reserve_seats
    if theater_hall[row][j] == 1:
       ~~~~~~~~~~~~~~~~~^^^
IndexError: list index out of range
"""
