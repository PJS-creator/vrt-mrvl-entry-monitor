# Daily Signal Monitor

- 데이터 기준일(주가): **2026-05-29**
- 실행시간(UTC): **2026-05-30 15:00:36**

## ⚠️ DATA WARNING
일부 데이터 수집에 실패하여 최근 사용 가능한 값(캐시 포함)을 사용했습니다.

- FRED DFII10 failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED VIXCLS failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.
- FRED NFCI failed (HTTPSConnectionPool(host='fred.stlouisfed.org', port=443): Read timed out. (read timeout=20)), using cached values if available.

## MacroGreen
- **MacroGreen**: **True**

### 핵심 수치
- HY OAS (BAMLH0A0HYM2): 2.72 / 4주 변화 -11.0 bp
- IG OAS (BAMLC0A0CM): 0.73 / 4주 변화 -8.0 bp
- 10Y Real Yield (DFII10): 2.06 / 4주 변화 12.0 bp
- VIX (VIXCLS): 15.74
- NFCI: -0.51

## VRT 신규진입 룰
- ratio (VRT/SRVR): 9.090412
- MA60: 8.921317
- gap: 1.90%
- **VRT_ENTRY**: **True**

## MRVL 신규진입 룰 (확인형)
- ratio (MRVL/SMH): 0.342277
- MA60: 0.286297
- gap: 19.55%
- MA60_slope_proxy: 0.042031
- **MRVL_ENTRY**: **True**

## Verdict
✅ Entry condition met: BOTH
