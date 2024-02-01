import ccxt
import time
import csv

def crypto_data_collector():
    csv_file_path = "./backend/binance_BTCUSDT_4h_data.csv"  # CSV 檔案的路徑
    exchange = ccxt.binance()

    symbol = 'BTCUSDT'  # 交易對
    timeframe = '4h'     # K線時間粒度
    since = 1577811600000   # 從指定時間戳記開始
    limit = 1000  # 獲取的數據條數上限

    with open(csv_file_path, 'a', newline='') as file:  # 以追加模式打開 CSV 檔案
        writer = csv.writer(file)
        
        while True:
            klines = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
            if not klines:
                break
            
            for kline in klines:
                writer.writerow(kline)
            
            since = klines[-1][0] + 1

            if since >= int(time.time() * 1000):
                break

            print(f"{since} 已保存到 {csv_file_path}")
            time.sleep(0.5)
    
    return f"Data collected and stored in {csv_file_path}"

if __name__ == "__main__":
    crypto_data_collector()
