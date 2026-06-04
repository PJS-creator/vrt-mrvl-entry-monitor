# Daily Signal Monitor

- 데이터 기준일(주가): **2026-06-04**
- 실행시간(UTC): **2026-06-04 15:00:41**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.71 / 4주 변화 -6.0 bp
- IG OAS (BAMLC0A0CM): 0.74 / 4주 변화 -5.0 bp
- 10Y Real Yield (DFII10): 2.07 / 4주 변화 16.0 bp
- VIX (VIXCLS): 16.05
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.203981
- MA60: 9.025035
- gap: 1.98%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.486031
- MA60: 0.301027
- gap: 61.46%
- MA60_slope_proxy: 0.048549
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH
