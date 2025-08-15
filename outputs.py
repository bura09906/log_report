from prettytable import PrettyTable


def get_pretty_table(results):
    table = PrettyTable()
    table.field_names = (
        'handler',
        'total',
        'avg_response_time',
    )
    table.align = 'l'
    table.add_rows(results)
    print(table)
