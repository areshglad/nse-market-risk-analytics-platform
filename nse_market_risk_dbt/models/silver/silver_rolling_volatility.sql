select
    price_date,
    ticker,
    daily_return,
    log_return,

    stddev(daily_return) over (
        partition by ticker
        order by price_date
        rows between 20 preceding and current row
    ) as rolling_volatility_21d,

    stddev(daily_return) over (
        partition by ticker
        order by price_date
        rows between 20 preceding and current row
    ) * sqrt(252) as annualized_volatility

from {{ ref('silver_daily_returns') }}