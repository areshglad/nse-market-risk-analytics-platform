with portfolio_returns as (

    select
        price_date,
        avg(daily_return) as portfolio_daily_return
    from {{ ref('silver_daily_returns') }}
    group by price_date

),

portfolio_stats as (

    select
        count(*) as trading_days,
        avg(portfolio_daily_return) * 252 as annual_return,
        stddev(portfolio_daily_return) * sqrt(252) as annual_volatility,
        min(portfolio_daily_return) as worst_daily_return
    from portfolio_returns

),

stock_count as (

    select
        count(distinct ticker) as number_of_stocks
    from {{ ref('silver_daily_returns') }}

)

select
    s.trading_days,
    c.number_of_stocks,
    s.annual_return,
    s.annual_volatility,
    s.worst_daily_return,
    (s.annual_return - 0.065) / s.annual_volatility as sharpe_ratio

from portfolio_stats s
cross join stock_count c