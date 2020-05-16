def prep_data(df):

    df = df.assign(hw=(df["Height"] * df["Width"] * df["Width"]) / 830)

    X = df[["Height", "Width", "hw"]].values
    y = df["Weight"].values

    return X, y