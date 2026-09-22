# Calculate Compound Interest

- Use this instruction when a user needs compound interest calculated with the `tools/compound_interest.py` command-line tool.
- Run the command from the project root with four positional arguments in this order:
  - `principal`: initial amount.
  - `annual_rate`: annual interest rate as a percentage, such as `7.34`.
  - `compounds_per_year`: number of compounding periods per year, such as `12` for monthly compounding.
  - `total_years`: duration in years; use a decimal for partial years.
- Invoke the tool with:
  - `python tools/compound_interest.py <principal> <annual_rate> <compounds_per_year> <total_years>`
- Example:
  - `python tools/compound_interest.py 15847 7.34 12 8.583333333333333`
- Confirm that the inputs are non-negative and that `compounds_per_year` is greater than zero.
- Present the tool output exactly as two currency values:
  - `Final amount: $...`
  - `Interest earned: $...`
- State the input assumptions when reporting results, especially the annual-rate units, compounding frequency, and duration.
- Do not present unrounded intermediate calculations unless the user requests them.
