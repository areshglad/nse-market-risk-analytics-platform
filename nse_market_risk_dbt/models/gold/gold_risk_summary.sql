with portfolio_returns as (

    select
        price_date,
        avg(daily_return) as portfolio_daily_return
    from {{ ref('silver_daily_returns') }}
    group by price_date

),

risk_metrics as (

    select
        avg(portfolio_daily_return) * 252 as annual_return,
        stddev(portfolio_daily_return) * sqrt(252) as annual_volatility,
        min(portfolio_daily_return) as worst_daily_return
    from portfolio_returns

)

select
    annual_return,
    annual_volatility,
    worst_daily_return,
    (annual_return - 0.065) / annual_volatility as sharpe_ratio
from risk_metrics