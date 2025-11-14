from dataclasses import dataclass

@dataclass
class FXRate:
    currency_pair: str
    rate: float
@dataclass
class FXQuote:
    currency_pair: str
    bid: float
    ask: float 
@dataclass
class FXTransaction:
    currency_pair: str
    amount: float
    transaction_type: str  # 'buy' or 'sell'
@dataclass
class FXPortfolio:
    holdings: dict  # key: currency_pair, value: amount
@dataclass
class FXMarketData:
    timestamp: str
    rates: dict  # key: currency_pair, value: FXRate    
@dataclass
class FXOrder:
    order_id: str
    currency_pair: str
    amount: float
    order_type: str  # 'market' or 'limit'
    price: float = None  # Only for limit orders
@dataclass
class FXSettlement:
    transaction_id: str
    settlement_date: str
    amount: float
@dataclass
class FXHedgingStrategy:
    strategy_name: str
    details: str    
@dataclass
class FXRiskMetrics:
    currency_pair: str
    value_at_risk: float
    expected_shortfall: float
@dataclass
class FXHistoricalData:
    currency_pair: str
    historical_rates: list  # List of FXRate
@dataclass
class FXNewsEvent:
    event_id: str
    description: str
    impact: str  # 'high', 'medium', 'low'
@dataclass
class FXAnalyticsReport:
    report_id: str
    summary: str
    insights: list  # List of strings   
@dataclass
class FXComplianceRecord:
    record_id: str
    details: str
    status: str  # 'compliant' or 'non-compliant'
@dataclass
class FXLiquidityProfile:
    currency_pair: str
    liquidity_score: float
@dataclass
class FXTransactionCost:
    currency_pair: str
    cost_percentage: float
@dataclass
class FXVolatilityIndex:
    currency_pair: str
    volatility_value: float
@dataclass
class FXMarketSentiment:
    currency_pair: str
    sentiment_score: float
@dataclass
class FXForecast:
    currency_pair: str
    forecasted_rate: float
    confidence_interval: tuple  # (lower_bound, upper_bound)
@dataclass
class FXArbitrageOpportunity:
    currency_pair: str
    profit_potential: float
@dataclass
class FXSwapAgreement:
    agreement_id: str
    currency_pair: str
    notional_amount: float
    start_date: str
    end_date: str
@dataclass
class FXOptionContract:
    contract_id: str
    currency_pair: str
    strike_price: float
    expiration_date: str
    option_type: str  # 'call' or 'put'
@dataclass
class FXForwardContract:
    contract_id: str
    currency_pair: str
    forward_rate: float
    settlement_date: str
@dataclass
class FXInterestRateDifferential:
    currency_pair: str
    differential_value: float
@dataclass
class FXCrossCurrencyRate:
    base_currency: str
    quote_currency: str
    cross_rate: float
@dataclass
class FXEconomicIndicator:
    indicator_name: str
    value: float
    impact_level: str  # 'high', 'medium', 'low'    
@dataclass
class FXTradeExecution:
    trade_id: str
    currency_pair: str
    execution_time: str
    price: float
    amount: float
@dataclass
class FXSettlementInstruction:
    instruction_id: str
    currency_pair: str
    settlement_details: str
@dataclass
class FXCounterparty:
    counterparty_id: str
    name: str
    credit_rating: str
@dataclass
class FXRegulatoryReport:
    report_id: str
    content: str
    submission_date: str
@dataclass
class FXTechnologyInfrastructure:
    system_name: str
    uptime_percentage: float
    latency_ms: float
@dataclass
class FXCustomerProfile:
    customer_id: str
    name: str
    risk_tolerance: str  # 'low', 'medium', 'high'
@dataclass
class FXMarketTrend:
    currency_pair: str
    trend_direction: str  # 'upward', 'downward', 'sideways'
    trend_strength: float