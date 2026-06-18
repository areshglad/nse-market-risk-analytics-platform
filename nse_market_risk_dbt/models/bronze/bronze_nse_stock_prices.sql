select
    cast(Date as date) as price_date,
    ticker,

    cast(Open as double) as open_price,
    cast(High as double) as high_price,
    cast(Low as double) as low_price,
    cast(Close as double) as close_price,

    cast(Volume as bigint) as volume,

    cast(adj_close as double) as adj_close_price

from {{ source('raw', 'raw_nse_stock_prices') }}

where ticker is not null