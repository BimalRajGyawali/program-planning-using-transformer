The paper [Iterative Student Program Planning using
Transformer-Driven Feedback](https://cs.brown.edu/~sk/Publications/Papers/Published/rsfk-planning-w-gpt-feedback/paper.pdf) highlights an area of improvement:
`Testing is not enough - Students wanted high-level feedback about their plans, not just testing results`. This repository is an attempt to extend the work done by the authors of the paper to accommodate high-level feedback on students' plans.

- [Extended Workflow](#extended-workflow)
- [Original Workflow](#original-workflow)
- [Why Testing Is Not Enough](#why-testing-is-not-enough)
- [Providing High-Level Feedback on a Plan Using LLMs Is Challenging](#providing-high-level-feedback-on-a-plan-using-llms-is-challenging)
- [An Attempt to Extend](#an-attempt-to-extend)
- [Drawbacks of This Approach](#drawbacks-of-this-approach)

### [Extended workflow]
![alt experimental](https://github.com/BimalRajGyawali/program-planning-using-transformer/blob/main/experiment.png)


### [Original workflow]
![alt original](https://github.com/BimalRajGyawali/program-planning-using-transformer/blob/main/original.png)


### Why testing is not enough

A correct plan can still fail a unit test because the LLM might generate incorrect code, particularly with return types.

For example: 

Student plan: `If there is no seat available, cancel reservation.`

LLM generated code: `return "cancelled reservation"`

Expected Unit Test: `return False`

So, it would be very useful for students to understand why their plan failed, rather than just seeing that the unit test failed (as mentioned in the paper).

<br>

### But, providing high-level feedback on a plan using LLMs is challenging
Because:

1. LLMs are non-deterministic, so we can't fully control what they generate.
2. To provide plan-specific feedback, the LLM needs to understand the task, but this could lead to the LLM generating code from the plan instead.

<br>


### An attempt to extend
To address this, the feedback mechanism was adapted to the final stage — when the unit test fails. After several prompt iterations, the following feedback was provided by the LLM:

```
Your plan has several issues that need to be addressed:

1. **Row Boundary Check**: Ensure that your plan includes checking whether the specified starting seat and the number of requested seats fit within the bounds of the current row. Failing to do this can lead to attempting to reserve seats that are out of the index range of the row.

2. **Abort Conditions**: For the condition where more than one seat is requested, your plan should mention a clear abort if **any** seat in the specified range is already reserved. This is critical to prevent partial reservations when not all seats can be allocated.

These are the primary areas where your plan might be leading to failures. Addressing these concerns should help you refine your approach. Focus on ensuring all conditions and constraints are explicitly handled in your plan.
```
<br>


### Drawbacks of this approach
1. Extra LLM call can result in increased cost
2. LLM may not come up with useful feedback in the first try. [Student can regenerate the feedback to solve this]



