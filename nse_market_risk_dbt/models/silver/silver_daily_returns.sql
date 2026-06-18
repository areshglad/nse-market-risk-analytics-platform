with prices as (

    select
        price_date,
        ticker,
        close_price
    from {{ ref('bronze_nse_stock_prices') }}

),

returns as (

    select
        price_date,
        ticker,
        close_price,

        lag(close_price) over (
            partition by ticker
            order by price_date
        ) as previous_close_price

    from prices

)

select
    price_date,
    ticker,
    close_price,
    previous_close_price,

    (close_price - previous_close_price) / previous_close_price as daily_return,

    ln(close_price / previous_close_price) as log_return

from returns

where previous_close_price is not null