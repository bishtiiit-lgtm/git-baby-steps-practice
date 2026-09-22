import argparse


def calculate_compound_interest(
    principal: float,
    annual_rate_percent: float,
    compounds_per_year: int,
    total_years: float,
) -> tuple[float, float]:
    periodic_rate = (annual_rate_percent / 100) / compounds_per_year
    periods = compounds_per_year * total_years
    final_amount = principal * (1 + periodic_rate) ** periods
    interest_earned = final_amount - principal
    return final_amount, interest_earned


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate compound interest.")
    parser.add_argument("principal", type=float, help="Initial principal amount")
    parser.add_argument(
        "annual_rate",
        type=float,
        help="Annual interest rate as a percentage, such as 7.34",
    )
    parser.add_argument(
        "compounds_per_year",
        type=int,
        help="Number of compounding periods per year",
    )
    parser.add_argument("total_years", type=float, help="Total investment time in years")
    args = parser.parse_args()

    if args.principal < 0:
        parser.error("principal must be non-negative")
    if args.annual_rate < 0:
        parser.error("annual_rate must be non-negative")
    if args.compounds_per_year <= 0:
        parser.error("compounds_per_year must be greater than zero")
    if args.total_years < 0:
        parser.error("total_years must be non-negative")

    final_amount, interest_earned = calculate_compound_interest(
        args.principal,
        args.annual_rate,
        args.compounds_per_year,
        args.total_years,
    )
    print(f"Final amount: ${final_amount:,.2f}")
    print(f"Interest earned: ${interest_earned:,.2f}")


if __name__ == "__main__":
    main()
