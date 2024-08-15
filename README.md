The paper [Iterative Student Program Planning using
Transformer-Driven Feedback](https://cs.brown.edu/~sk/Publications/Papers/Published/rsfk-planning-w-gpt-feedback/paper.pdf) describes a negative opinion:
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

LLM can mark the plan as failed even though the plan is correct due to various reasons, one of which is return types. Students might not explicitly define return types as they might not be familiar to coding, or might describe the plan in plain high level english. Due to which LLM might confuse/generate return types on its own.

For example: 

Student plan: `If there is no seat available, cancel reservation.`

LLM generated code: `return "cancelled reservation"`

Expected Unit Test: `return False`

<br>

### Providing high-level feedback on a plan using LLMs is challenging

So, it would be very useful if students knew the reason why the plain failed instead of knowing only unit test failed. [The paper also mentions this]. But it is challenging due to:
1. LLMs are non-deterministic and we cannot absolutely control what they generate.
2. To give a plan specific feedback, LLM should have the knowledge of task. But it risks in LLM generating the code from the plan due to (Point 1).

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



