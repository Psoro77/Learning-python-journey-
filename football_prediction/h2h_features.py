import pandas as pd

def get_h2h_stats(df, home_team, away_team, current_date, n_matches=5):
    mask = (
        (((df['HomeTeam'] == home_team) & (df['AwayTeam'] == away_team)) |
         ((df['HomeTeam'] == away_team) & (df['AwayTeam'] == home_team))) &
        (df['Date'] < current_date)
    )
    h2h = df[mask].sort_values('Date', ascending=False).head(n_matches)

    if h2h.empty:
        return 0, 0, 0

    home_wins = 0
    goals_for_home = 0

    for _, row in h2h.iterrows():
        if row['HomeTeam'] == home_team:
            goals_for_home += row['FTHG']
            if row['FTR'] == 'H':
                home_wins += 1
        elif row['AwayTeam'] == home_team:
            goals_for_home += row['FTAG']
            if row['FTR'] == 'A':
                home_wins += 1

    return len(h2h), goals_for_home / len(h2h), home_wins / len(h2h)


def add_h2h_features(df, n_matches=5):
    """
    Ajoute les colonnes H2H_matches, H2H_avg_goals_home, H2H_home_win_rate
    """
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    h2h_counts = []
    h2h_avg_goals = []
    h2h_win_rate = []

    for idx, row in df.iterrows():
        count, avg_goals, win_rate = get_h2h_stats(
            df, row['HomeTeam'], row['AwayTeam'], row['Date'], n_matches
        )
        h2h_counts.append(count)
        h2h_avg_goals.append(avg_goals)
        h2h_win_rate.append(win_rate)

    df['H2H_matches'] = h2h_counts
    df['H2H_avg_goals_home'] = h2h_avg_goals
    df['H2H_home_win_rate'] = h2h_win_rate

    return df
