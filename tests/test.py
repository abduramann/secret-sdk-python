import pytest
from secret_sdk.key.mnemonic import MnemonicKey
from secret_sdk.core.coins import Coins


@pytest.fixture
def mnemonics():
    # Initialize genesis accounts
    return [
        "grant rice replace explain federal release fix clever romance raise often wild taxi quarter soccer fiber love must tape steak together observe swap guitar",
        "jelly shadow frog dirt dragon use armed praise universe win jungle close inmate rain oil canvas beauty pioneer chef soccer icon dizzy thunder meadow",
        "chair love bleak wonder skirt permit say assist aunt credit roast size obtain minute throw sand usual age smart exact enough room shadow charge",
        "word twist toast cloth movie predict advance crumble escape whale sail such angry muffin balcony keen move employ cook valve hurt glimpse breeze brick",
    ]


def test_setup_accounts(mnemonics):
    #setup_localsecret()
    #secret = LCDClient(url='http://localhost:1317', chain_id='secretdev-1')
    secret = pytest.secret
    accounts = []

    for mnemonic in mnemonics:
        wallet = secret.wallet(MnemonicKey(mnemonic))
        accounts.append({
          'address': wallet.key.acc_address,
          'mnemonic': mnemonic,
          'wallet': wallet,
          'secret': secret
        })

    # Generate a bunch of accounts because tx.staking tests require creating a bunch of validators
    for i in range(4, 20):
        wallet = secret.wallet(MnemonicKey())
        accounts.append({
            'address': wallet.key.acc_address,
            'mnemonic': mnemonic,
            'wallet': wallet,
            'secret': secret
        })

    # Send 100k SCRT from account 0 to each of accounts 1 - 20
    for account in accounts:
        account['balances'], _ = account['wallet'].lcd.bank.balance(account['address'])

    transfer_amount = int(100 * 1e6)
    try:
        tx = accounts[0]['wallet'].send_tokens(
            recipient_addr=accounts[1]['address'],
            transfer_amount=Coins({'uscrt': transfer_amount})
        )
        print(tx)
    except Exception as e:
        raise Exception(f'MsgSend failed: {e}')
    if tx.code != 0:
        raise Exception(f'MsgSend failed: {tx.raw_log}')

    try:
        tx = accounts[0]['wallet'].multi_send_tokens(
            recipient_addrs=[account['address'] for account in accounts[2:]],
            transfer_amounts=[Coins({'uscrt': transfer_amount}) for _ in accounts[2:]]
        )
        print(tx)
    except Exception as e:
        raise Exception(f'MsgMultiSend failed: {e}')

    if tx.code != 0:
        raise Exception(f'MsgMultiSend failed: {tx.raw_log}')

    def update_balance(accounts):
        old = {i: account['balances'].to_dict().get('uscrt', 0) for i, account in enumerate(accounts)}
        for account in accounts:
            account['balances'], _ = account['wallet'].lcd.bank.balance(account['address'])
        new = {i: account['balances'].to_dict().get('uscrt', 0) for i, account in enumerate(accounts)}
        return {i: new[i]-old[i] for i, _ in enumerate(accounts)}

    balance_changes = update_balance(accounts)
    print(balance_changes)
    for i in range(1, 20):
        assert balance_changes[i] == transfer_amount

    pytest.accounts = accounts


def test_accounts():
    all_accounts, pagination = pytest.secret.auth.accounts()

    # 20 accounts with a balance and 7? module accounts - ordering of tests can affect this.
    #  it 's more robust to check eq&gt rather than flat equality
    assert len(all_accounts) >= 27
    assert len([acc for acc in all_accounts if acc.type_url == '/cosmos.auth.v1beta1.ModuleAccount']) >= 7
    addrs = [pytest.accounts[0]['address'], pytest.accounts[1]['address']]
    assert len([acc for acc in all_accounts if acc.type_url == '/cosmos.auth.v1beta1.BaseAccount' and acc.address in addrs]) == 2


def test_account():
    addr = pytest.accounts[1]['address']
    account = pytest.secret.auth.account_info(address=addr)
    if not account:
        raise Exception(f'Account {addr} should exist')

    assert account.type_url == '/cosmos.auth.v1beta1.BaseAccount'
    assert account.address == addr
    assert account.account_number == 1
    assert account.sequence == 0
