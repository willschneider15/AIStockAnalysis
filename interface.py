import alpaca_trade_api as tradeapi

api = tradeapi.REST(
    key_id='PKZOGDQK7YPWDPWQB2OP',
    secret_key='bnXup12lnLL90ROBCNJYfUrZIgD3JcJTrZusQ9x0',
    base_url='https://paper-api.alpaca.markets')

order = api.submit_order(
    symbol='AAPL',
    qty=15,
    side='buy',
    time_in_force='day',
    type='market'
)
