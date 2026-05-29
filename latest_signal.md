# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-28**
- 실행시간(UTC): **2026-05-29 03:00:39**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED BAMLH0A0HYM2 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED BAMLC0A0CM failed (504 Server Error: Gateway Time-out for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLC0A0CM), using cached values if available.
- FRED DFII10 failed (504 Server Error: Gateway Time-out for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10), using cached values if available.
- FRED VIXCLS failed (504 Server Error: Gateway Time-out for url: https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 -11.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 -7.0 bp
- 10Y Real Yield (DFII10): 2.1 / 4주 변화 18.0 bp
- VIX (VIXCLS): 16.29
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.020384
- MA60: 8.89749
- gap: 1.38%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.34148
- MA60: 0.283852
- gap: 20.30%
- MA60_slope_proxy: 0.041853
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH
