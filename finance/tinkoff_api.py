import pandas as pd
from tinkoff.invest import Client
from tinkoff.invest.schemas import InstrumentIdType

TOKEN_TINKOF = 't.GvIEAt49s7Jg6vmgqXaFvhKTK7DUwbpJiK1dsC4ZjjK_PXacw2Q0MAjTNHtMRnVFqAeeHBCb0Xm_JFtj_TtiAA'


def format_money_value(value, precision=2):
    """Форматирует объект MoneyValue или Quotation в удобный вид."""
    return round(value.units + value.nano / 1e9, precision)


def get_instrument_info(client, figi, instrument_type):
    """Получает название и тикер инструмента по FIGI и его типу."""
    try:
        instrument_methods = {
            "share": client.instruments.share_by,
            "currency": client.instruments.currency_by,
            "etf": client.instruments.etf_by,
            "bond": client.instruments.bond_by,
            "future": client.instruments.future_by,
            "option": client.instruments.option_by,
            "options": client.instruments.options_by,
        }
        
        if instrument_type in instrument_methods:
            instrument = instrument_methods[instrument_type](id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=figi).instrument
            return instrument.name, instrument.ticker
        else:
            return "Неизвестный инструмент", "N/A"

    except Exception:
        return "Ошибка получения данных", "N/A"


with Client(TOKEN_TINKOF) as client:
    r = client.users.get_accounts()

    # Создаем словарь: имя счета -> ID
    accounts_dict = {account.name: account.id for account in r.accounts}

    total_portfolio_value = 0  # Переменная для хранения общей стоимости портфелей

    for name, account_id in accounts_dict.items():
        portfolio = client.operations.get_portfolio(account_id=account_id)

        total_value = format_money_value(portfolio.total_amount_portfolio)
        expected_yield = format_money_value(portfolio.expected_yield)

        print(f"📊 Портфель: {name} ({account_id})")
        print(f"💰 Общая стоимость: {total_value} rub")
        print(f"📈 Доходность: {expected_yield} ₽\n")

        portfolio_data = []

        for position in portfolio.positions:
            asset_name, ticker = get_instrument_info(client, position.figi, position.instrument_type)
            quantity = format_money_value(position.quantity)
            avg_price = format_money_value(position.average_position_price)  # Средняя цена покупки
            current_price = format_money_value(position.current_price)  # Текущая цена
            yield_rub = format_money_value(position.expected_yield)  # Доходность в рублях
            total_value_asset = round(quantity * current_price, 2)  # Текущая стоимость актива

            # Доходность в %
            if total_value_asset - yield_rub != 0:
                yield_percent = round((yield_rub / (total_value_asset - yield_rub)) * 100, 2)
            else:
                yield_percent = 0  # Если разница нулевая, то доходность в % равна 0

            portfolio_data.append([asset_name, ticker, quantity, avg_price, current_price, total_value_asset, yield_rub, yield_percent])

        # Создание DataFrame и сортировка по убыванию доходности в %
        df = pd.DataFrame(portfolio_data, columns=["Название", "Тикер", "Количество", "Средняя цена", "Текущая цена", "Текущая стоимость (₽)", "Доходность (₽)", "Доходность (%)"])
        df = df.sort_values(by="Доходность (%)", ascending=False)  # Сортировка по доходности в %

        print(df)
        print("=" * 50)

        total_portfolio_value += total_value  # Добавляем стоимость этого портфеля к общей стоимости

    # Вывод общей стоимости всех портфелей
    print(f"💼 Общая стоимость всех портфелей: {total_portfolio_value} rub")
