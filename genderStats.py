import csv

files = [ 'data/2013_entrants.csv',
          'data/2013_runners.csv',
          'data/2014_entrants.csv',
          'data/2014_runners.csv',
          'data/2015_entrants.csv',
          'data/2015_runners.csv',
          'data/2016_entrants.csv',
          'data/2016_runners.csv',
          'data/2017_entrants.csv',
          'data/2017_runners.csv',
          'data/2018_entrants.csv',
          'data/2018_runners.csv',
          'data/2019_entrants.csv',
          'data/2019_runners.csv',
          'data/2020_entrants.csv',
          'data/2020_runners.csv' ]

for file in files:
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        totals = {'M':{'entries':0, 'tickets':0}, 'F':{'entries':0, 'tickets':0}}
        for row in csv_reader:
            totals[row['gender']]['entries'] += 1
            if 'tickets' in row:
                totals[row['gender']]['tickets'] += int(row['tickets'])

        m_entries = totals['M']['entries']
        f_entries = totals['F']['entries']
        total_entries = m_entries + f_entries
        m_entries_percent = round(m_entries / total_entries * 100,1)
        f_entries_percent = round(f_entries / total_entries * 100,1)

        m_tickets = totals['M']['tickets']
        f_tickets = totals['F']['tickets']
        total_tickets = m_tickets + f_tickets

        print(f'{file}: RUNNERS (M/F): {m_entries}/{f_entries} ({m_entries_percent}%/{f_entries_percent}%) TOTAL: {total_entries} ')

        if total_tickets > 0:
            m_tickets_percent = round(m_tickets / total_tickets * 100,1)
            f_tickets_percent = round(f_tickets / total_tickets * 100,1)

            print(f'{file}: TICKETS (M/F): {m_tickets}/{f_tickets} ({m_tickets_percent}%/{f_tickets_percent}%) TOTAL: {total_tickets} ')
